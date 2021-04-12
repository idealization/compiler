import argparse
from DFA import *

DFAs = [TYPE, INT, CHAR, BOOL, STRING, ID, KEY, ARITH, ASSIGN, COMP, SEMI, BRACKET, BRACE, PAREN, COMMA, WHITESPACE]


def determineDFA(candidateDFAs, finalDFAs):                     # determine correctDFA
    if len(finalDFAs) == 2 and ID in finalDFAs:                 # ID has low priority when it meets KEY or TYPE
        finalDFAs.remove(ID)
        return list(finalDFAs)
    elif len(candidateDFAs) == 0 and len(finalDFAs) == 1:
        return list(finalDFAs)
    elif len(candidateDFAs) == 0 and len(finalDFAs) == 0:       # input code has error
        return False


def lexicalAnalysis(rawString, input_file_name):                # main algorithm of lexical analyzer
    fw = open(input_file_name + "_output.txt", 'w')             # output file
    word_start, word_final = 0, 1                               # index of the string for lexical analysis
    lexemes = []                                                # list of lexeme(string)
    tokens = []                                                 # list of token(string : dfa.token)

    # set candidate DFA list and final DFA
    candidateDFAs = [TYPE, INT, CHAR, BOOL, STRING, ID, KEY, ARITH, ASSIGN, COMP, SEMI, BRACKET, BRACE, PAREN, COMMA, WHITESPACE]
    finalDFAs = set()

    while word_final <= len(rawString):
        for dfa in candidateDFAs[:]:                            # filter candidate DFA to check error in DFA
            if not dfa.is_not_error(rawString[word_start:word_final]):
                candidateDFAs.remove(dfa)
        if not candidateDFAs:
            correctDFA = determineDFA(candidateDFAs, finalDFAs)     # determine string's correct DFA
            if not correctDFA:                                  # print input code has error
                fw.write('ERROR')
                return 0
            lexeme = rawString[word_start:word_final - 1]       # define lexeme
            lexemes.append(lexeme)                              # append lexeme to list
            token = correctDFA[0].token                         # define token name
            tokens.append(token)                                # append token to list
            word_start = word_final - 1                         # reset index of string and candidate, final DFA
            word_final -= 1
            candidateDFAs = [TYPE, INT, CHAR, BOOL, STRING, ID, KEY, ARITH, ASSIGN, COMP, SEMI, BRACKET, BRACE, PAREN,
                             COMMA, WHITESPACE]
            finalDFAs = set()
        else:
            finalDFAs = set()
            for dfa in DFAs[:]:                                 # filter final DFA to check if string is accepted in DFA
                if dfa.is_accept(rawString[word_start:word_final]):
                    finalDFAs.add(dfa)
        # exception handling : - can be OP or negative sign
        # - is OP when previous token is INT or ID, and negative sign in other situations
        # also the immediately token of - can be blank
        if rawString[word_start:word_final] == '-':
            if tokens[-1] == ' ':
                if tokens[-2] == ('ID' or 'INT'):
                    candidateDFAs.remove(INT)
                else:
                    candidateDFAs.remove(ARITH)
            else:
                if tokens[-1] == ('ID' or 'INT'):
                    candidateDFAs.remove(INT)
                else:
                    candidateDFAs.remove(ARITH)
        word_final += 1
    fw.write("-----------------------\n")                       # print each token and lexeme
    for i in range(len(lexemes)):
        if not tokens[i] == 'WHITESPACE':
            strFormat = '%-12s%-12s'
            strOut = strFormat % (tokens[i], lexemes[i])
            fw.write(strOut + '\n')
    fw.write("-----------------------\n")


parser = argparse.ArgumentParser()
parser.add_argument("input_file_name", help="file name of your input code")
args = parser.parse_args()
fr = open(args.input_file_name, 'r')
data = fr.read()
lexicalAnalysis(data + ' ', args.input_file_name)
