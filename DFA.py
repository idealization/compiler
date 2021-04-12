class Transition:                               # represent DFA's transition function
    def __init__(self, current_state, input_symbol, next_state):
        self.current_state = current_state
        self.input_symbol = input_symbol
        self.next_state = next_state


class DFA:                                      # represent DFA
    def __init__(self, name, start_state, trans_functions, final_state):
        self.name = name
        self.start_state = start_state
        self.trans_functions = trans_functions
        self.final_state = final_state
        self.token = None

    def is_not_error(self, s):                  # return False when string is rejected by DFA
        current = [0]
        for c in s:
            destination = []
            f = 0
            for trans in self.trans_functions:
                if (c in trans.input_symbol) and (trans.current_state in current):
                    destination.append(trans.next_state)
                    f = 1
            if f == 0:
                return False
            if len(destination):
                current = destination
            else:
                return False
        return current                          # return current states when string is (or will be) accepted by DFA

    def is_accept(self, s):                     # check if string arrives DFA's final state
        temp = self.is_not_error(s)
        if type(temp) is list:
            return self.is_final(temp)
        else:
            return False

    def is_final(self, temp):                   # check if current state is final state
        for i in temp:
            if i in self.final_state:
                self.token = i                  # determine token as current state
                return True
        return False


# define DFA
# DFA's final state is candidate token name of the string
digits = '0123456789'
positive = '123456789'
letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
TYPE = DFA('TYPE', 0, [Transition(0, 'i', 1), Transition(1, 'n', 5), Transition(5, 't', 'VTYPE'),
                       Transition(0, 'c', 2), Transition(2, 'h', 6), Transition(6, 'a', 10), Transition(10, 'r', 'VTYPE'),
                       Transition(0, 'b', 3), Transition(3, 'o', 7), Transition(7, 'o', 11), Transition(11, 'l', 14),
                       Transition(14, 'e', 16), Transition(16, 'a', 18), Transition(18, 'n', 'VTYPE'),
                       Transition(0, 's', 4), Transition(4, 't', 8), Transition(8, 'r', 12),
                       Transition(12, 'i', 15), Transition(15, 'n', 17), Transition(17, 'g', 'VTYPE')], ['VTYPE'])
INT = DFA('INT', 0, [Transition(0, '0', 'INT'), Transition(0, '-', 2), Transition(0, positive, 'INT'),
                     Transition(2, positive, 'INT'), Transition('INT', digits, 'INT')], ['INT'])
CHAR = DFA('CHAR', 0, [Transition(0, "'", 1), Transition(1, digits, 2), Transition(1, letter, 3), Transition(1, ' ', 4),
                       Transition(2, "'", 'CHAR'), Transition(3, "'", 'CHAR'), Transition(4, "'", 'CHAR')], ['CHAR'])
BOOL = DFA('BOOL', 0, [Transition(0, 't', 1), Transition(1, 'r', 3), Transition(3, 'u', 5), Transition(5, 'e', 'BOOL'),
                       Transition(0, 'f', 2), Transition(2, 'a', 4), Transition(4, 'l', 6),
                       Transition(6, 's', 8), Transition(8, 'e', 'BOOL')], ['BOOL'])
STRING = DFA('STRING', 0, [Transition(0, '"', 1), Transition(1, digits, 2), Transition(1, letter, 3), Transition(1, ' ', 4),
                           Transition(2, digits, 5), Transition(2, letter, 6), Transition(2, ' ', 7),
                           Transition(3, digits, 5), Transition(3, letter, 6), Transition(3, ' ', 7),
                           Transition(4, digits, 5), Transition(4, letter, 6), Transition(4, ' ', 7),
                           Transition(2, '"', 'STRING'), Transition(3, '"', 'STRING'), Transition(4, '"', 'STRING'),
                           Transition(5, digits, 5), Transition(5, letter, 6), Transition(5, ' ', 7),
                           Transition(6, digits, 5), Transition(6, letter, 6), Transition(6, ' ', 7),
                           Transition(7, digits, 5), Transition(7, letter, 6), Transition(7, ' ', 7),
                           Transition(5, '"', 'STRING'), Transition(6, '"', 'STRING'), Transition(7, '"', 'STRING')], ['STRING'])
ID = DFA('ID', 0, [Transition(0, letter, 'ID'), Transition(0, '_', 'ID'),
                   Transition('ID', digits, 'ID'), Transition('ID', letter, 'ID'), Transition('ID', '_', 'ID')], ['ID'])
KEY = DFA('KEY', 0, [Transition(0, 'i', 1), Transition(1, 'f', 'IF'), Transition(0, 'e', 2), Transition(2, 'l', 7),
                     Transition(7, 's', 11), Transition(11, 'e', 'ELSE'), Transition(0, 'w', 3), Transition(3, 'h', 8),
                     Transition(8, 'i', 12), Transition(12, 'l', 16), Transition(16, 'e', 'WHILE'), Transition(0, 'c', 4),
                     Transition(4, 'l', 9), Transition(9, 'a', 13), Transition(13, 's', 17), Transition(17, 's', 'CLASS'),
                     Transition(0, 'r', 5), Transition(5, 'e', 10), Transition(10, 't', 14), Transition(14, 'u', 18),
                     Transition(18, 'r', 21), Transition(21, 'n', 'RETURN')], ['IF', 'ELSE', 'WHILE', 'CLASS', 'RETURN'])
ARITH = DFA('ARITH', 0, [Transition(0, '+', 'OP'), Transition(0, '-', 'OP'), Transition(0, '*', 'OP'),
                         Transition(0, '/', 'OP')], ['OP'])
ASSIGN = DFA('ASSIGN', 0, [Transition(0, '=', 'ASSIGN')], ['ASSIGN'])
COMP = DFA('COMP', 0, [Transition(0, '<', 'COMP'), Transition(0, '>', 'COMP'), Transition(0, '!', 3), Transition(0, '=', 4),
                       Transition('COMP', '=', 'COMP'), Transition(3, '=', 'COMP'), Transition(4, '=', 'COMP')], ['COMP'])
SEMI = DFA('SEMI', 0, [Transition(0, ';', 'SEMI')], ['SEMI'])
BRACKET = DFA('BRACKET', 0, [Transition(0, '[', 'LBRACKET'), Transition(0, ']', 'RBRACKET')], ['LBRACKET', 'RBRACKET'])
PAREN = DFA('PAREN', 0, [Transition(0, '(', 'LPAREN'), Transition(0, ')', 'RPAREN')], ['LPAREN', 'RPAREN'])
BRACE = DFA('BRACE', 0, [Transition(0, '{', 'LBRACE'), Transition(0, '}', 'RBRACE')], ['LBRACE', 'RBRACE'])
COMMA = DFA('COMMA', 0, [Transition(0, ',', 'COMMA')], ['COMMA'])
WHITESPACE = DFA('WHITESPACE', 0, [Transition(0, '\t', 'WHITESPACE'), Transition(0, '\n', 'WHITESPACE'),
                                   Transition(0, ' ', 'WHITESPACE')], ['WHITESPACE'])



