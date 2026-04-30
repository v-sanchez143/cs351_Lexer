##Purpose = Building a lexer to break down a line of code into tokens (listed above)

#This is a simple lexer gui
import re
from tkinter import *


def CutOneLineTokens(code):
    tokenList = []
    new_code = code.strip()
    # copying str to new_str so it doesnt mess up str when rmving chopped pts

    while len(new_code) > 0:  # loops until int count has reached the last index of code str
        # prints what count were at
        new_code = new_code.lstrip()
        # will single out the part of text to later figure out token type it is
        # specimen = re.search("\\w+\\s", new_code)
        #  sample = specimen.group() #assigns the singled out word to sample to find out what it is
        # print("sample: " + sample)
        # will now figure out what token type it is
        if re.match("(int|float|if|else|print)", new_code):
            tt = "keyword"
            token = re.match("(int|float|if|else|print)", new_code)
        elif re.match("[(]|[)]|:|;", new_code):
            tt = "separator"
            token = re.match("[(]|[)]|:|;", new_code)
        elif re.match("[+]|[=]|[>]|[*]", new_code):
            tt = "operators"
            token = re.match("[+]|[=]|[>]|[*]", new_code)
        elif re.match(r"\d+\.\d+", new_code):
            tt = "float_literal"
            token = re.match(r"\d+\.\d+", new_code)
        elif re.match("[a-zA-Z][a-zA-Z0-9]*", new_code):
            tt = "identifier"
            token = re.match("[a-zA-Z][a-zA-Z0-9]*", new_code)
        elif re.match(r"\d+", new_code):
            tt = "int_literal"
            token = re.match(r"\d+", new_code)


        else:
            tt = "UNIDENTIFIED"
            print("Unidentified token:", new_code[0])
            new_code = new_code[1:]
            continue
        ###add the rest later######

        # now add the token type and token to token list

        tokenInput = "<" + tt + ", " + token.group() + ">"
        tokenList.append(tokenInput)
        new_code = new_code[token.end():]
        # display token list
        #print(tokenList)
    return tokenList
        # update new_code to remove id'ed token
    # new_code = re.sub(r'token', "", new_code) #removes the sample str from new_code
    # change using the span of .search so it doesn't remove duplicates

    # update count to move forward in code str index and loop back
    # count += len(token.group())
    # print("looping back...")


def math_exp(tokens):
        output = []
        values = []
        ops = []
        def apply_op():
            b = values.pop()
            a = values.pop()
            op = ops.pop()

            if op == "+":
                result = a + b
            elif op == "-":
                result = a - b
            elif op == "*":
                result = a * b
            else:
                result = 0

            output.append(f"Apply {a} {op} {b} = {result}")
            values.append(result)

        i = 0
        while i < len(tokens):
            token = tokens[i]

            if "int_literal" in token:
                val = int(token.split(",")[1].replace(">","").strip())
                values.append(val)
                output.append(f"Push {val}")
            elif "float_literal" in token:
                val = float(token.split(",")[1].replace(">","").strip())
                values.append(val)
                output.append(f"Push {val}")
            elif "+" in token:
                while ops and ops[-1] == "*":
                    apply_op()
                ops.append("+")
            elif "-" in token:
                ops.append("-")
            elif "*" in token:
                ops.append("*")
            i += 1

        while ops:
            apply_op()
        output.append(f"Final result: {values[0]}")
        return output


def parser(tokens):
    output = []
    #go from first token
    first_token = tokens[0]

    if "if" in first_token:
        output.append("Processing IF statement")
        output.extend(if_exp(tokens))
    elif "identifier" in first_token or "int_literal" in first_token:
        output.append("Processing Math expression")
        output.extend(math_exp(tokens))
    elif "print" in first_token:
        output.append("Processing Print statement")
        output.extend(print_exp(tokens))
    else:
        output.append("Unidentified statement")
    return output


def print_exp(tokens):
    output = []
    i = 0
    output.append("Start <print_exp>")

    if "print" in tokens[i]:
        output.append("Match 'Print'")
        i += 1
    else:
        output.append("Unmatched Print statement")
        return output

    if "(" in tokens[i]:
        output.append("Match '('")
        i += 1
    else:
        output.append("Unmatched '('")
        return output

    if "identifier" in tokens[i]:
        output.append(f"Match {tokens[i]}")
        i += 1
    else:
        output.append("Unmatched Identifier")
        return output

    if ")" in tokens[i]:
        output.append("Match ')'")
        i += 1
    else:
        output.append("Unmatched ')'")
        return output

    output.append("End <print_exp>")
    return output


def if_exp(tokens):
    output = []
    i = 0
    output.append("Start <if_exp>")

    #expect if
    if "if" in tokens[i]:
        output.append("Match 'if'")
        i += 1
    else:
        output.append("Error: expected 'if'")
        return output

    #expect (
    if "(" in tokens[i]:
        output.append("Match '('")
        i += 1
    else:
        output.append("Error: expected ')'")
        return output

    #call comparison_exp
    comp_output, i = comparison_exp(tokens, i)
    output.extend(comp_output)

    #expect )
    if ")" in tokens[i]:
        output.append("Match ')'")
        i += 1
    else:
        output.append("Error: expected ')'")
        return output

    #expect :
    if ":" in tokens[i]:
        output.append("Match ':'")
        i += 1
    else:
        output.append("Error: expected ':'")
        return output

    output.append("End <if_exp>")
    return output


def comparison_exp(tokens, i):
    output = []
    output.append("Start <comparison_exp>")

    #identifier
    if "identifier" in tokens[i]:
        output.append(f"Match {tokens[i]}")
        i += 1
    else:
        output.append("Error: expected identifier")
        return output, i

    # >
    if ">" in tokens[i]:
        output.append("Match '>'")
        i += 1
    else:
        output.append("Error: expected '>'")
        return output, i

    #identifier
    if "identifier" in tokens[i]:
        output.append(f"Match {tokens[i]}")
        i += 1
    else:
        output.append("Error: expected identifier")
        return output, i

    output.append("End <comparison_exp>")
    return output, i


class LexerGUI: #class definition
    def __init__(self, root):
        # Master is the default parent object of all widgets.
        # You can think of it as the window that pops up when you run the GUI code.
        self.master = root
        self.master.title("Lexical Analyzer for Tinypie")

        self.current_line=0
        self.lines= []

        #title of headers
        self.input_label = Label(self.master, text="Source code input: ")
        self.input_label.grid(row=0, column=0, sticky=W)

        self.output_label = Label(self.master, text="Tokens:")
        self.output_label.grid(row=0, column=1, sticky=W)

        #text boxes#
        self.input_box = Text(self.master, width=40, height=15)
        self.input_box.grid(row=1, column=0, padx=5, pady=5)

        self.output_box = Text(self.master, width=40, height=15)
        self.output_box.grid(row=1, column=1, padx=5, pady=5)

        self.parser_label = Label(self.master, text="Parser: ")
        self.parser_label.grid(row=0, column=2, sticky=W)

        self.parser_box = Text(self.master, width=40, height=15)
        self.parser_box.grid(row=1, column=2, padx=5, pady=5)

        #label for current line
        self.line_label= Label(self.master, text="Line number: 0")
        self.line_label.grid(row=2, column=0, sticky=W)

        #buttons
        self.next_button=Button(self.master, text="Next", command=self.next_line)
        self.next_button.grid(row=2, column=1, pady=10)

        self.quit_button = Button(self.master, text="Quit", command=self.master.quit)
        self.quit_button.grid(row=2, column=2, pady=10)


    def next_line(self):

        #first click will store all the lines
        if self.current_line == 0:
            text=self.input_box.get("1.0", END)
            self.lines=text.splitlines()
        #now it has all the lines the first time and splits them based on new line character#
        if self.current_line < len(self.lines):
            line_to_check=self.lines[self.current_line]
            tokens = CutOneLineTokens(line_to_check)
            parser_output = parser(tokens)
            self.output_box.delete("1.0", END)
            for token in tokens:
                self.output_box.insert(END, token + "\n")
            #to show parser output
            self.parser_box.delete("1.0", END)
            for line in parser_output:
                self.parser_box.insert(END, line + "\n")
            self.current_line+=1
            self.line_label.config(
                text="Current Line : " + str(self.current_line)
            )


if __name__ == "__main__":
    myTKRoot=Tk()
    myTKgui=LexerGUI(myTKRoot)
    myTKRoot.mainloop()