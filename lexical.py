from DFA import *

DFAs = [TYPE, INT, CHAR, BOOL, STRING, ID, KEY, ARITH, ASSIGN, COMP, SEMI, BRACKET, BRACE, PAREN, COMMA, WHITESPACE]

def lexicalAnalysis(rawString):
    wordIdx = 0
    lexemes = [] # list of lexeme(string)
    tokens = [] # list of token(string : dfa.name)

    candidateDFAs = [TYPE, INT, CHAR, BOOL, STRING, ID, KEY, ARITH, ASSIGN, COMP, SEMI, BRACKET, BRACE, PAREN, COMMA, WHITESPACE]
    lexeme = '' # lexeme variable

    while wordIdx < len(rawString):

        if len(candidateDFAs) == 1:
            correctDFA = candidateDFAs[0]
            tokens.append(correctDFA.name)
            # until correctDFA makes error and wordIdx within length of rawString, concat word at lexeme
            while correctDFA.is_accept(rawString[wordIdx]) and wordIdx <= len(rawString):
                lexeme += rawString[wordIdx]
                wordIdx += 1
            # add lexeme(string) to lexemes(list of lexeme)
            lexemes.append(lexeme)
            lexeme = ''             # lexeme initialize
            candidateDFAs = DFAs    # candidateDFAs initialize

        else:
            for dfa in DFAs:
                # if current dfa makes error, remove from candidate dfa
                if not dfa.is_not_error(rawString[wordIdx]):
                    candidateDFAs.remove(dfa)
            lexeme += rawString[wordIdx]
            wordIdx += 1


    # Print lexemes+tokens info (except for whitespace)
    for i in range(len(lexemes)):
        if not tokens[i] == 'WHITESPACE':
            print("LEXEME : "+lexemes[i] + " TOKEN : " + tokens[i])



f = open("input.txt",'r')
data = f.read()
print(lexicalAnalysis(data))

