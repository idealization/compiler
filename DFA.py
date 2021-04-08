class Transition:
    def __init__(self, current_state, input_symbol, next_state):
        self.currentState = current_state
        self.input_symbol = input_symbol
        self.nextState = next_state


class DFA:
    def __init__(self, name, start_state, trans_functions, final_state):
        self.name = name
        self.startState = start_state
        self.transFuncs = trans_functions
        self.finalState = final_state

    def is_error(self, s):
        current = set()
        for c in s:
            destination = set()
            for trans in self.trans_functions:
                if c in trans.input and trans.current_state in current:
                    destination.append(trans.next_state)
            if not destination.isEmpty():
                current = destination
            else:
                return True
        return current

    def is_accept(self, s):
        temp = self.isError(s)
        if type(temp) is set:
            return self.is_final(temp)
        else:
            return False

    def is_final(self, current):
        if current in self.final_state:
            return True
        return False


digits = '0123456789'
positive = '123456789'
letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
TYPE = DFA('TYPE', 0, [Transition(0, 'i', 1), Transition(1, 'n', 5), Transition(5, 't', 9),
                       Transition(0, 'c', 2), Transition(2, 'h', 6), Transition(6, 'a', 10), Transition(10, 'r', 13),
                       Transition(0, 'b', 3), Transition(3, 'o', 7), Transition(7, 'o', 11), Transition(11, 'l', 14),
                       Transition(14, 'e', 16), Transition(16, 'a', 18), Transition(18, 'n', 20),
                       Transition(0, 's', 4), Transition(4, 't', 8), Transition(8, 'r', 12),
                       Transition(12, 'i', 15), Transition(15, 'n', 17), Transition(17, 'g', 19)], [9, 13, 20, 19])
INT = DFA('INT', 0, [Transition(0, '0', 1), Transition(0, '-', 2), Transition(0, positive, 3), Transition(2, positive, 3),
                     Transition(3, digits, 4), Transition(4, digits, 4)], [4])
CHAR = DFA('CHAR', 0, [Transition(0, "'", 1), Transition(1, digits, 2), Transition(1, letter, 3),
                       Transition(1, ' ', 4), Transition(2, "'", 5), Transition(3, "'", 5), Transition(4, "'", 5)], [5])
BOOL = DFA('BOOL', 0, [Transition(0, 't', 1), Transition(1, 'r', 3), Transition(3, 'u', 5), Transition(5, 'e', 7),
                       Transition(0, 'f', 2), Transition(2, 'a', 4), Transition(4, 'l', 6),
                       Transition(6, 's', 8), Transition(8, 'e', 9)], [7, 9])
STRING = DFA('STRING', 0, [Transition(0, '"', 1), Transition(1, digits, 2), Transition(1, letter, 3), Transition(1, ' ', 4),
                           Transition(2, digits, 5), Transition(2, letter, 6), Transition(2, ' ', 7),
                           Transition(3, digits, 5), Transition(3, letter, 6), Transition(3, ' ', 7),
                           Transition(4, digits, 5), Transition(4, letter, 6), Transition(4, ' ', 7),
                           Transition(5, digits, 5), Transition(5, letter, 6), Transition(5, ' ', 7),
                           Transition(6, digits, 5), Transition(6, letter, 6), Transition(6, ' ', 7),
                           Transition(7, digits, 5), Transition(7, letter, 6), Transition(7, ' ', 7),
                           Transition(5, '"', 8), Transition(6, '"', 8), Transition(7, '"', 8)], [8])
ID = DFA('ID', 0, [Transition(0, letter, 1), Transition(0, '_', 2),
                   Transition(1, digits, 3), Transition(1, letter, 4), Transition(1, '_', 5),
                   Transition(2, digits, 3), Transition(2, letter, 4), Transition(2, '_', 5),
                   Transition(3, digits, 3), Transition(3, letter, 4), Transition(3, '_', 5),
                   Transition(4, digits, 3), Transition(4, letter, 4), Transition(4, '_', 5),
                   Transition(5, digits, 3), Transition(5, letter, 4), Transition(5, '_', 5)], [1, 2, 3, 4, 5])
KEY = DFA('KEY', 0, [Transition(0, 'i', 1), Transition(1, 'f', 6), Transition(0, 'e', 2), Transition(2, 'l', 7),
                     Transition(7, 's', 11), Transition(11, 'e', 15), Transition(0, 'w', 3), Transition(3, 'h', 8),
                     Transition(8, 'i', 12), Transition(12, 'l', 16), Transition(16, 'e', 19), Transition(0, 'c', 4),
                     Transition(4, 'l', 9), Transition(9, 'a', 13), Transition(13, 's', 17), Transition(17, 's', 20),
                     Transition(0, 'r', 5), Transition(5, 'e', 10), Transition(10, 't', 14), Transition(14, 'u', 18),
                     Transition(18, 'r', 21), Transition(21, 'n', 22)], [6, 15, 19, 20, 22])
ARITH = DFA('ARITH', 0, [Transition(0, '+', 1), Transition(0, '-', 2), Transition(0, '*', 3), Transition(0, '/', 4)], [1, 2, 3, 4])
ASSIGN = DFA('ASSIGN', 0, [Transition(0, '=', 1)], [1])
COMP = DFA('COMP', 0, [Transition(0, '<', 1), Transition(0, '>', 2), Transition(0, '!', 3), Transition(0, '=', 4),
                       Transition(1, '=', 5), Transition(2, '=', 5), Transition(3, '=', 6), Transition(4, '=', 6)], [1, 2, 5, 6])
SEMI = DFA('SEMI', 0, [Transition(0, ';', 1)], [1])
BRACKET = DFA('BRACKET', 0, [Transition(0, '{', 1), Transition(0, '}', 2)], [1, 2])
PAREN = DFA('PAREN', 0, [Transition(0, '(', 1), Transition(0, ')', 2)], [1, 2])
BRACE = DFA('BRACE', 0, [Transition(0, '[', 1), Transition(0, ']', 2)], [1, 2])
COMMA = DFA('COMMA', 0, [Transition(0, ',', 1)], [1])
WHITESPACE = DFA('WHITESPACE', 0, [Transition(0, '\t', 1), Transition(0, '\n', 2), Transition(0, ' ', 3)], [1, 2, 3])



