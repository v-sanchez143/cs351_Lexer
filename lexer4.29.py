
#This is for parser 4/29

from tkinter import *

class LexerGUI: #class definition
    def __init__(self, root):
        # Master is the default parent object of all widgets.
        # You can think of it as the window that pops up when you run the GUI code.
        self.master = root
        self.master.title("Lexical Analyzer for Tinypie")

        self.current_line=0
        self.lines= []

       # self.currentToken = 0  # index for which token were on, to be compared to len of source line
       # self.tokeLi = []  # empty list to hold all the <type,token>

        #title of headers
        self.input_label = Label(self.master, text="Source code input: ")
        self.input_label.grid(row=0, column=0, sticky=W)

        self.output_label = Label(self.master, text="Lexical Analyzed Result:")
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
            self.output_box.insert(END, line_to_check + "\n")
            self.line_label.config(
               text="Current Line : " + str(self.current_line)

           )
"""
    def tokenList(self): #will create a LIST of <type,token> to be inputed into parser
        #this func should be called each source code
        #line to create a new list each time

        if self.current_line == 0: #if we are on the first line of input box
            text = self.input_box.get(1,END) #variable txt
            self.lines = text.splitlines() #splits lines based on \n

        if self.current_line < len(self.lines): #if the current line index
             line to                                   #is less than the number of lines
            if self.currentToken == 0: #if we are at the first token

"""

class ParserGUI(LexerGUI): #class def for parser
    #self.lines holes all type tokens
#creating one more text box to print out the output of parser algorithm
    def __init__ (self, root):
        LexerGUI.__init__ (self,root)
        #header
        self.parser_label = Label(self.master, text="Parser Output: ")
        self.parser_label.grid(row=0, column=3, sticky=W)
        #text boxes#
        self.parser_box = Text(self.master, width=40, height=15)
        self.parser_box.grid(row=1, column=3, padx=5, pady=5)
    def parser(self):

        Mytokens = [("keyword", "float"), ("id", "myVar"), ("id", "mynum"), ("op", "="), ("op", "+"), ("op",
                                                                                                       "*"),
                    ("int", "6"), ("int", "7"), ("float", "4.3"), ("float", "2.1"), ("float", "3.4"), ("sep", ";")]
        inToken = ("empty", "empty")

        def accept_token():
            global inToken

        print(" accept token from the list:" + inToken[1])

       # def math():
            #if the first word is a keyword go to accepts token to check it



if __name__ == "__main__":
    myTKRoot=Tk()
    myTKgui=ParserGUI(myTKRoot)
    myTKRoot.mainloop()
