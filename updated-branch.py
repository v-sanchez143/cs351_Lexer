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
        if re.match("(int|float|if|else)", new_code):
            tt = "keyword"
            token = re.match("(int|float|if|else)", new_code)
        elif re.match("[(]|[)]|:|;", new_code):
            tt = "separator"
            token = re.match("[(]|[)]|:|;", new_code)
        elif re.match("[+]|[=]|[>]|[*]", new_code):
            tt = "operators"
            token = re.match("[+]|[=]|[>]|[*]", new_code)
        elif re.match(r"\d+\.\d+", new_code):
            tt = "float_literal"
            token = re.match(r"\d+\.\d+", new_code)
        elif re.match("[a-zA-Z]\\d*", new_code):
            tt = "identifier"
            token = re.match("[a-zA-Z]\\d*", new_code)
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
            self.output_box.delete("1.0", END)
            for token in tokens:
                self.output_box.insert(END, token + "\n")
            self.current_line+=1
            self.line_label.config(
                text="Current Line : " + str(self.current_line)
            )


if __name__ == "__main__":
    myTKRoot=Tk()
    myTKgui=LexerGUI(myTKRoot)
    myTKRoot.mainloop()
