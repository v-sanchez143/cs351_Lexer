
#step 1: define the rules of different tokens
#tokens are only the following:
#Keywords:	if	else	int	float
#Operators:	=	+	>	*
#Separators:	(	)	:	“	;
#Identifiers:	letters, or letters followed by digits
#Int_literal:	only integers
#Float_literal: 	only float
#String_literal:	only strings

#Purpose = Building a lexer to break down a line of code into tokens (listed above)

import re

################
#TOKEN TYPES
################

#TT_OPERATOR = "\+|\=|\>|\*" #find any     +  =  >  *     symbols
#TT_KEYWORDS = "(\\bint\\b|\\bfloat\\b|\\bif\\b|\\belse\\b)" #find any    if  else  int  float   keywords
#TT_SEPARATORS = "\(|\)|\:|\;|:" #find any    (  )  :  "  ;     symbols
#TT_IDENTIFIERS = "[A-Za-z]\w*" #find any letters OR letters followed by digits
#TT_INT_LITERAL = "^[\d]+&" #finds only intergers
#TT_FLOAT_LITERAL = "\d+\.\d+" #finds only floats
#TT_STRING_LITERAL = "\"[a-zA-Z]+\"" #finds only strings



def CutOneLineTokens(code):
        tokenList = []
        count = 0
        new_code = code #copying str to new_str so it doesnt mess up str when rmving chopped pts
        s = str(len(new_code))
        print("len of str: " + s)

        while count < len(code): #loops until int count has reached the last index of code str
            # prints what count were at
            st = str(count)
            print("count: " + st)
            #will single out the part of text to later figure out token type it is
           # specimen = re.search("\\w+\\s", new_code)
          #  sample = specimen.group() #assigns the singled out word to sample to find out what it is
           # print("sample: " + sample)
            #will now figure out what token type it is
            if re.search("(int|float|if|else)", new_code):
                tt = "keyword"
                token = re.match("(int|float|if|else)", new_code)
            elif re.search("[(]|[)]|:|;", new_code):
                tt = "separator"
                token = re.match ("[(]|[)]|:|;", new_code)
            elif re.search("[a-zA-Z]\\d*", new_code):
                tt = "identifier"
                token = re.match("[a-zA-Z]\\d*", new_code)
            elif re.search( "[+]|[=]|[>]|[*]", new_code):
                tt = "operators"
                token = re.match( "[+]|[=]|[>]|[*]", new_code)
            elif re.search("^[\\d]+&" , new_code) :
                tt = "int_literal"
                token = re.match("^[\\d]+&" , new_code)
            else:
                tt = "UNIDENTIFIED"
                token = new_code
            ###add the rest later######

            #now add the token type and token to token list

            tokenInput = "<" + tt + ", " +  token.group() + ">"
            tokenList.append(tokenInput)
            #display token list
            print(tokenList)

            #update new_code to remove id'ed token
            new_code = re.sub(r'token', "", new_code) #removes the sample str from new_code
                                                        #change using the span of .search so it doesn't remove duplicates

            #update count to move forward in code str index and loop back
            count += len(token.group())
            print("looping back...")









def main():
    tester = "int A1=5"
    CutOneLineTokens(tester)

    print("token type identification is working well as well as taking out only the token."
          "Bug in the line of code not removing the previous token so it's getting stuck on the first token "
          "as well as the regex for operator not working right. I think if might have to do with the whitespace but "
          "more likely from the same line of code that is supposed to remove the previous token")



if __name__ == "__main__":
     main()


