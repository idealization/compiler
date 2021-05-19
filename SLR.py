class SLRGrammar:
    def __init__(self, grammar):
        self.grammar = grammar


class SLRTable:                               # represent SLR-parsing table
    def __init__(self, action, goto):
        self.action = action
        self.goto = goto


slr_grammar = SLRGrammar([['CODE', 'VDECL CODE'],
                          ['CODE', 'FDECL CODE'],
                          ['CODE', 'CDECL CODE'],
                          ['CODE', ''],
                          ['VDECL', 'VTYPE ID SEMI'],
                          ['VDECL', 'VTYPE GOTO_ASSIGN SEMI'],
                          ['GOTO_ASSIGN', 'ID ASSIGN RHS'],
                          ['RHS', 'EXPR'],
                          ['RHS', 'STRING'],
                          ['RHS', 'CHAR'],
                          ['RHS', 'BOOL'],
                          ['EXPR', 'TERM ADDSUB EXPR'],
                          ['EXPR', 'TERM'],
                          ['TERM', 'FACTOR MULTDIV TERM'],
                          ['TERM', 'FACTOR'],
                          ['FACTOR', 'LPAREN EXPR RPAREN'],
                          ['FACTOR', 'ID'],
                          ['FACTOR', 'INTEGER'],
                          ['FDECL', 'VTYPE ID LPAREN ARG RPAREN LBRACE BLOCK GOTO_RETURN RBRACE'],
                          ['ARG', 'VTYPE ID MOREARGS'],
                          ['ARG', ''],
                          ['MOREARGS', 'COMMA VTYPE ID MOREARGS'],
                          ['MOREARGS', ''],
                          ['BLOCK', 'STMT BLOCK'],
                          ['BLOCK', ''],
                          ['STMT', 'VDECL'],
                          ['STMT', 'GOTO_ASSIGN SEMI'],
                          ['STMT', 'IF LPAREN COND RPAREN LBRACE BLOCK RBRACE GOTO_ELSE'],
                          ['STMT', 'WHILE LPAREN COND RPAREN LBRACE BLOCK RBRACE'],
                          ['COND', "COND' COMP COND"],
                          ['COND', "COND'"],
                          ["COND'", 'BOOL'],
                          ['GOTO_ELSE', 'ELSE LBRACE BLOCK RBRACE'],
                          ['GOTO_ELSE', ''],
                          ['GOTO_RETURN', 'RETURN RHS SEMI'],
                          ['CDECL', 'CLASS ID LBRACE ODECL RBRACE'],
                          ['ODECL', 'VDECL ODECL'],
                          ['ODECL', 'FDECL ODECL'],
                          ['ODECL', '']])


slr_table = SLRTable([[[0, 'VTYPE', 's2']],
                      [[1, 'VTYPE', 's6'], [1, 'CLASS', 's7'], [1, '$', 'r3']],
                      [[2, 'ID', 's8']],
                      [[3, '$', 'acc']],
                      [[4, 'VTYPE', 's6'], [4, 'CLASS', 's7'], [4, '$', 'r3']],
                      [[5, 'VTYPE', 's6'], [5, 'CLASS', 's7'], [5, '$', 'r3']],
                      [[6, 'ID', 's12']],
                      [[7, 'ID', 's13']],
                      [[8, 'SEMI', 's14'], [8, 'OPERATOR', 's15']],
                      [[9, 'SEMI', 's16']],
                      [[10, '$', 'r1']],
                      [[11, '$', 'r2']],
                      [[12, 'SEMI', 's14'], [12, 'OPERATOR', 's15'], [12, 'LPAREN', 's17']],
                      [[13, 'LBRACE', 's18']],
                      [[14, 'VTYPE', 'r4'], [14, 'ID', 'r4'], [14, 'RBRACE', 'r4'], [14, 'IF', 'r4'], [14, 'WHILE', 'r4'], [14, 'RETURN', 'r4'], [14, 'CLASS', 'r4'], [14, '$', 'r4']],
                      [[15, 'ID', 's27'], [15, 'STRING', 's21'], [15, 'CHAR', 's22'], [15, 'BOOL', 's23'], [15, 'LPAREN', 's26'], [15, 'INTEGER', 's28']],
                      [[16, 'VTYPE', 'r5'], [16, 'ID', 'r5'], [16, 'RBRACE', 'r5'], [16, 'IF', 'r5'], [16, 'WHILE', 'r5'], [16, 'RETURN', 'r5'], [16, 'CLASS', 'r5'], [16, '$', 'r5']],
                      [[17, 'VTYPE', 's30'], [17, 'RPAREN', 'r20']],
                      [[18, 'VTYPE', 's6'], [18, 'RBRACE', 'r38']],
                      [[19, 'SEMI', 'r6']],
                      [[20, 'SEMI', 'r7']],
                      [[21, 'SEMI', 'r8']],
                      [[22, 'SEMI', 'r9']],
                      [[23, 'SEMI', 'r10']],
                      [[24, 'SEMI', 'r12'], [24, 'ADDSUB', 's34'], [24, 'RPAREN', 'r12']],
                      [[25, 'SEMI', 'r14'], [25, 'ADDSUB', 'r14'], [25, 'MULTDIV', 's35'], [25, 'RPAREN', 'r14']],
                      [[26, 'ID', 's27'], [26, 'LPAREN', 's26'], [26, 'INTEGER', 's28']],
                      [[27, 'SEMI', 'r16'], [27, 'ADDSUB', 'r16'], [27, 'MULTDIV', 'r16'], [27, 'RPAREN', 'r16']],
                      [[28, 'SEMI', 'r17'], [28, 'ADDSUB', 'r17'], [28, 'MULTDIV', 'r17'], [28, 'RPAREN', 'r17']],
                      [[29, 'RPAREN', 's37']],
                      [[30, 'ID', 's38']],
                      [[31, 'RBRACE', 's39']],
                      [[32, 'VTYPE', 's6'], [32, 'RBRACE', 'r38']],
                      [[33, 'VTYPE', 's6'], [33, 'RBRACE', 'r38']],
                      [[34, 'ID', 's27'], [34, 'LPAREN', 's26'], [34, 'INTEGER', 's28']],
                      [[35, 'ID', 's27'], [35, 'LPAREN', 's26'], [35, 'INTEGER', 's28']],
                      [[36, 'RPAREN', 's44']],
                      [[37, 'LBRACE', 's45']],
                      [[38, 'RPAREN', 'r22'], [38, 'COMMA', 's47']],
                      [[39, 'VTYPE', 'r35'], [39, 'CLASS', 'r35'], [39, '$', 'r35']],
                      [[40,'RBRACE','r36']],
                      [[41, 'RBRACE', 'r37']],
                      [[42, 'SEMI', 'r11'], [42, 'RPAREN', 'r11']],
                      [[43, 'SEMI', 'r13'], [43, 'ADDSUB', 'r13'], [43, 'RPAREN', 'r13']],
                      [[44, 'SEMI', 'r15'], [44, 'ADDSUB', 'r15'], [44, 'MULTDIV', 'r15'], [44, 'RPAREN', 'r15']],
                      [[45, 'VTYPE', 's2'], [45, 'ID', 's54'], [45, 'RBRACE', 'r24'], [45, 'IF', 's52'], [45, 'WHILE', 's53'], [45, 'RETURN', 'r24']],
                      [[46, 'RPAREN', 'r19']],
                      [[47, 'VTYPE', 's55']],
                      [[48, 'RETURN', 's57']],
                      [[49, 'VTYPE', 's2'],[49, 'ID', 's54'],[49, 'RBRACE', 'r24'], [49, 'IF', 's52'], [49, 'WHILE', 's53'], [49, 'RETURN', 'r24']],
                      [[50, 'VTYPE', 'r25'], [50, 'ID', 'r25'], [50, 'RBRACE', 'r25'], [50, 'IF', 'r25'], [50, 'WHILE', 'r25'], [50, 'RETURN', 'r25']]
                      [[51, 'SEMI', 's59']],
                      [[52, 'LPAREN', 's60']],
                      [[53, 'LPAREN', 's61']],
                      [[54, 'ASSIGN', 's15']],
                      [[55, 'ID', 's62']],
                      [[56, 'RBRACE', 's63']],
                      [[57, 'ID', 's27'] , [57, 'LITERAL', 's21'], [57, 'CHARACTER', 's22'], [57, 'BOOLSTR', 's23'], [57, 'LPAREN', 's26'], [57, 'NUM', 's28']],
                      [[58, 'RBRACE', 'r23'], [58, 'RETURN', 'r23']],
                      [[59, 'VTYPE', 'r26'], [59, 'VTYPE', 'r26'], [59, 'RBRACE', 'r26'], [59, 'IF', 'r26'], [59, 'WHILE', 'r26'], [59, 'RETURN', 'r26']],
                      [[60, 'BOOLSTR', 's67']],
                      [[61, 'BOOLSTR', 's67']],
                      [[62, 'RPAREN', 'r22'],[62, 'COMMA', 's47']],
                      [[63, 'VTYPE', 'r18'], [63, 'RBRACE', 'r18'], [63, 'CLASS', 'r18'], [63, '$', 'r18']],
                      [[64, 'SEMI', 's70']],
                      [[65, 'RPAREN', 's71']],
                      [[66, 'RPAREN', 'r30'], [66, 'COMP', 's72']],
                      [[67, 'RPAREN', 'r31'], [67, 'COMP', 'r31']],
                      [[68, 'RPAREN', 's73']],
                      [[69, 'RPAREN', 'r21']],
                      [[70, 'RBRACE', 'r34']],
                      [[71, 'LBRACE', 's74']],
                      [[72, 'BOOLSTR', 's67']],
                      [[73, 'LBRACE', 's76']],
                      [[74, 'VTYPE', 's2'], [74, 'ID', 's54'], [74, 'RBRACE', 'r24'], [74, 'IF', 's52'], [74, 'WHILE', 's53'], [74, 'RETURN', 'r24']],
                      [[75, 'RPAREN', 'r29']],
                      [[76, 'VTYPE', 's2'], [76, 'ID', 's54'], [76, 'RBRACE', 'r24'], [76, 'IF', 's52'], [76, 'WHILE', 's53'], [76, 'RETURN', 'r24']],
                      [[77, 'RBRACE', 's79']],
                      [[78, 'RBRACE', 's80']],
                      [[79, 'VTYPE', 'r33']],
                      [[79, 'ID', 'r33'], [79, 'RBRACE', 'r33'], [79, 'IF', 'r33'], [79, 'WHILE', 'r33'], [79, 'ELSE', 's82'], [79, 'RETURN', 'r33']],
                      [[80, 'VTYPE', 'r28'], [80, 'ID', 'r28'], [80, 'RBRACE', 'r28'], [80, 'IF', 'r28'], [80, 'WHILE', 'r28'], [80, 'RETURN', 'r28']],
                      [[81, 'VTYPE', 'r27'], [81, 'ID', 'r27'], [81, 'RBRACE', 'r27'], [81, 'IF', 'r27'], [81, 'WHILE', 'r27'], [81, 'RETURN', 'r27']],
                      [[82, 'LBRACE', 's83']],
                      [[83, 'VTYPE', 's2'], [83, 'ID', 's54'], [83, 'RBRACE', 'r24'], [83, 'IF', 's52'], [83, 'WHILE', 's53'], [83, 'RETURN', 'r24']],
                      [[84, 'RBRACE', 's85']],
                      [[85, 'RBRACE', 'r32'], [85, 'IF', 'r32'], [85, 'WHILE', 'r32'], [85, 'RETURN', 'r32'], [85, 'VTYPE', 'r32'], [85, 'ID', 'r32']]],
                     [[[0, 'VDECL', 1]],
                      [[1, 'CODE', 3], [1, 'VDECL', 1], [1, 'FDECL', 4], [1, 'CDECL', 5]],
                      [[2, 'GOTO_ASSIGN', 9]],
                      [],
                      [[4, 'CODE', 10], [4, 'VDECL', 1], [4, 'FDECL', 4], [4, 'CDECL', 5]],
                      [[5, 'CODE', 11], [5, 'VDECL', 1], [5, 'FDECL', 4], [5, 'CDECL', 5]],
                      [[6, 'GOTO_ASSIGN', 9]],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [[15, 'RHS', 19], [15, 'EXPR', 20], [15, 'TERM', 24], [15, 'FACTOR', 25]],
                      [],
                      [[17, 'ARG', 29]],
                      [[18, 'VDECL', 32], [18, 'FDECL', 33], [18, 'ODECL', 31]],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [[26, 'EXPR', 36], [26, 'TERM', 24], [26, 'FACTOR', 25]],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [[32, 'VDECL', 32], [32, 'FDECL', 33], [32, 'ODECL', 40]],
                      [[33, 'VDECL', 32], [33, 'FDECL', 33], [33, 'ODECL', 41]],
                      [[34, 'EXPR', 42], [34, 'TERM', 24], [34, 'FACTOR', 25]],
                      [[35, 'TERM', 43], [35, 'FACTOR', 25]],
                      [],
                      [],
                      [[38, 'MOREARGS', '46']],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [[45, 'VDECL', 50], [45, 'ASSIGN', 51], [45, 'BLOCK', 48], [45, 'STMT', 49]],
                      [],
                      [],
                      [[48, 'RETURN', 56]],
                      [[49, 'VDECL', 50], [49, 'ASSIGN', 51], [49, 'BLOCK', 58], [49, 'STMT', 49]],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [[57, 'RHS', 64], [57, 'EXPR', 20], [57, 'TERM', 24], [57, 'FACTOR', 25]],
                      [],
                      [],
                      [[60, 'COND', 65], [60, "COND'", 66]],
                      [[61, 'COND', 68], [61, "COND'", 66]],
                      [[62, 'MOREARGS', 69]],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [[72, 'COND', 75], [72, "COND'", 66]],
                      [],
                      [[74, 'VDECL', 50], [74, 'ASSIGN', 51], [74, 'BLOCK', 77], [74, 'STMT', 49]],
                      [],
                      [[76, 'VDECL', 50], [76, 'ASSIGN', 51], [76,'BLOCK', 78], [76, 'STMT', 49]],
                      [],
                      [],
                      [[79, 'ELSE', 81]],
                      [],
                      [],
                      [],
                      [[83, 'VDECL', 50], [83, 'ASSIGN', 51], [83, 'BLOCK', 84], [83, 'STMT', 49]]])


