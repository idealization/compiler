from DFA import *

DFAs = [TYPE, INT, CHAR, BOOL, STRING, ID, KEY, ARITH, ASSIGN, COMP, SEMI, BRACKET, BRACE, PAREN, COMMA, WHITESPACE]


def priorityDFA(candidateDFAs):
    if (candidateDFAs[0]==TYPE and candidateDFAs[1]==ID) or (candidateDFAs[0]==ID and candidateDFAs[1]==TYPE):
        return TYPE
    return None


def determineDFA(candidateDFAs, finalDFAs, token):
    if len(finalDFAs) == 2 and ID in finalDFAs:
        finalDFAs.remove(ID)
        return list(finalDFAs)
    elif len(finalDFAs) == 2 and token == 'ID':
        finalDFAs.remove(INT)
        return list(finalDFAs)
    elif len(finalDFAs) == 2 and token == 'ARITH':
        finalDFAs.remove(ARITH)
        return list(finalDFAs)
    elif len(candidateDFAs) == 0 and len(finalDFAs) == 1:
        return list(finalDFAs)
    elif len(candidateDFAs) == 0 and len(finalDFAs) == 0:
        return False # return NONE??


def lexicalAnalysis(rawString):
    word_start, word_final = 0, 1
    token = ''
    lexemes = []    # list of lexeme(string)
    tokens = []     # list of token(string : dfa.name)
    correctDFA = None

    candidateDFAs = [TYPE, INT, CHAR, BOOL, STRING, ID, KEY, ARITH, ASSIGN, COMP, SEMI, BRACKET, BRACE, PAREN, COMMA, WHITESPACE]
    finalDFAs = set()

    while word_final <= len(rawString):
        for dfa in candidateDFAs[:]:
            if not dfa.is_not_error(rawString[word_start:word_final]):
                candidateDFAs.remove(dfa)
        if not candidateDFAs:
            correctDFA = determineDFA(candidateDFAs, finalDFAs, token)
            if not correctDFA:
                return 'ERROR'
            lexeme = rawString[word_start:word_final - 1]
            lexemes.append(lexeme)
            token = correctDFA[0].name
            tokens.append(token)
            word_start = word_final - 1
            word_final -= 1
            candidateDFAs = [TYPE, INT, CHAR, BOOL, STRING, ID, KEY, ARITH, ASSIGN, COMP, SEMI, BRACKET, BRACE, PAREN,
                             COMMA, WHITESPACE]
            finalDFAs = set()
            print("현재 lexeme : ", lexeme, "은 ", token, "라는 token으로 판별")
        else:
            finalDFAs = set()
            for dfa in DFAs[:]:
                if dfa.is_accept(rawString[word_start:word_final]):
                    finalDFAs.add(dfa)
        word_final += 1
    print("---------------------")
    # Print lexemes+tokens info (except for whitespace)
    for i in range(len(lexemes)):
        if not tokens[i] == 'WHITESPACE':
            strFormat = '%-10s%-10s'
            strOut = strFormat % (tokens[i], lexemes[i])
            print(strOut)
            # print(f"{token[i]}{lexeme[i]}")
    print("---------------------")


f = open("input.txt",'r')
data=f.read()
lexicalAnalysis(data + ' ')