import argparse
from SLR import *


def syntax_analyzer(data):
    data = data.split()                         # split output of lexical analyzer by blank and reset to analyze easier
    del data[-1]
    data.append('$')
    data.append('$')
    index = 1                                   # initialize index of starting token
    state_stack = [0]                           # stack that stores states and last element is current state
    left_substring = []                         # store left substring that already shifted before
    while True:
        if data[index] == 'OP':                 # distinguish +, - and *, / operators
            if data[index + 1] == '+' or data[index + 1] == '-':
                data[index] = 'ADDSUB'
            else:
                data[index] = 'MULTDIV'
        for action in slr_table.action[state_stack[-1]]:
            if data[index] == action[1]:                # find action corresponding to terminal value
                if action[2][0] == 's':                 # shift and goto decision
                    state_stack.append(int(action[2][1:]))
                    left_substring.append(data[index])
                    index += 2
                elif action[2][0] == 'r':               # reduce decision
                    for non_terminal in reversed(slr_grammar.grammar[int(action[2][1:])][1].split()):
                        if non_terminal == left_substring[-1]:
                            del left_substring[-1]
                            state_stack.pop()
                        else:
                            print(f"There's no goto at state {state_stack[-1]} for {left_substring}")
                            return
                    left_substring.append(slr_grammar.grammar[int(action[2][1:])][0])
                    for goto in slr_table.goto[state_stack[-1]]:        # find goto corresponding to non-terminal value
                        if left_substring[-1] == goto[1]:
                            state_stack.append(goto[2])
                else:
                    print("Accept")
                    return
                break
        else:
            print("reject")
            print(f"There's no action at state {state_stack[-1]} for {data[index]}")
            return


parser = argparse.ArgumentParser()
parser.add_argument("input_file_name", help="file name of your input code")
args = parser.parse_args()
fr = open(args.input_file_name, 'r')
lexical_output = fr.read()
syntax_analyzer(lexical_output)
