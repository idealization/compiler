class SLRGrammar:
    def __init__(self, grammar):
        self.grammar = grammar


class SLRTable:                               # represent SLR-parsing table
    def __init__(self, action, goto):
        self.action = action
        self.goto = goto


slr_grammar = SLRGrammar([["CODE'", 'CODE'],
                          ['CODE', 'VDECL CODE'],
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


slr_table = SLRTable([[[0, 'VTYPE', 's5'], [0, 'CLASS', 's6'], [0, '$', 'r4']],
                      [[1, '$', 'acc']],
                      [[2, 'VTYPE', 's5'], [2, 'CLASS', 's6'], [2, '$', 'r4']],
                      [[3, 'VTYPE', 's5'], [3, 'CLASS', 's6'], [3, '$', 'r4']],
                      [[4, 'VTYPE', 's5'], [4, 'CLASS', 's6'], [4, '$', 'r4']],
                      [[5, 'ID', 's10']],
                      [[6, 'ID', 's12']],
                      [[7, '$', 'r1']],
                      [[8, '$', 'r2']],
                      [[9, '$', 'r3']],
                      [[10, 'SEMI', 's13'], [10, 'ASSIGN', 's15'], [10, 'LPAREN', 's14']],
                      [[11, 'SEMI', 's16']],
                      [[12, 'LBRACE', 's17']],
                      [[13, 'VTYPE', 'r5'], [13, 'ID', 'r5'], [13, 'RBRACE', 'r5'], [13, 'IF', 'r5'], [13, 'WHILE', 'r5'], [13, 'RETURN', 'r5'], [13, 'CLASS', 'r5'], [13, '$', 'r5']],
                      [[14, 'VTYPE', 's19'], [14, 'RPAREN', 'r21']],
                      [[15, 'ID', 's28'], [15, 'STRING', 's22'], [15, 'CHAR', 's23'], [15, 'BOOL', 's24'], [15, 'LPAREN', 's27'], [15, 'INTEGER', 's29']],
                      [[16, 'VTYPE', 'r6'], [16, 'ID', 'r6'], [16, 'RBRACE', 'r6'], [16, 'IF', 'r6'], [16, 'WHILE', 'r6'], [16, 'RETURN', 'r6'], [16, 'CLASS', 'r6'], [16, '$', 'r6']],
                      [[17, 'VTYPE', 's5'], [17, 'RPAREN', 'r39']],
                      [[18, 'RPAREN', 's33']],
                      [[19, 'ID', 's34']],
                      [[20, 'SEMI', 'r7']],
                      [[21, 'SEMI', 'r8']],
                      [[22, 'SEMI', 'r9']],
                      [[23, 'SEMI', 'r10']],
                      [[24, 'SEMI', 'r11']],
                      [[25, 'SEMI', 'r13'], [25, 'ADDSUB', 's35'], [25, 'RPAREN', 'r13']],
                      [[26, 'SEMI', 'r15'], [26, 'ADDSUB', 'r15'], [26, 'MULTDIV', 's36'], [26, 'RPAREN', 'r15']],
                      [[27, 'ID', 's28'], [27, 'LPAREN', 's27'], [27, 'INTEGER', 's29']],
                      [[28, 'SEMI', 'r17'], [28, 'ADDSUB', 'r17'], [28, 'MULTDIV', 'r17'], [28, 'RPAREN', 'r17']],
                      [[29, 'SEMI', 'r18'], [29, 'ADDSUB', 'r18'], [29, 'MULTDIV', 'r18'], [29, 'RPAREN', 'r18']],
                      [[30, 'RBRACE', 's38']],
                      [[31, 'VTYPE', 's5'], [31, 'RBRACE', 'r39']],
                      [[32, 'VTYPE', 's5'], [32, 'RBRACE', 'r39']],
                      [[33, 'LBRACE', 's41']],
                      [[34, 'RPAREN', 'r23'], [34, 'COMMA', 's43']],
                      [[35, 'ID', 's28'], [35, 'LPAREN', 's27'], [35, 'INTEGER', 's29']],
                      [[36, 'ID', 's28'], [36, 'LPAREN', 's27'], [36, 'INTEGER', 's29']],
                      [[37, 'RPAREN', 's46']],
                      [[38, 'VTYPE', 'r36'], [38, 'CLASS', 'r36'], [38, '$', 'r36']],
                      [[39, 'RBRACE', 'r37']],
                      [[40, 'RBRACE', 'r38']],
                      [[41, 'VTYPE', 's53'], [41, 'ID', 's54'], [41, 'RBRACE', 'r25'], [41, 'IF', 's51'], [41, 'WHILE', 's52'], [41, 'RETURN', 'r25']],
                      [[42, 'RPAREN', 'r20']],
                      [[43, 'VTYPE', 's55']],
                      [[44, 'SEMI', 'r12'], [44, 'RPAREN', 'r12']],
                      [[45, 'SEMI', 'r14'], [45, 'ADDSUB', 'r14'], [45, 'RPAREN', 'r14']],
                      [[46, 'SEMI', 'r16'], [46, 'ADDSUB', 'r16'], [46, 'MULTDIV', 'r16'], [46, 'RPAREN', 'r16']],
                      [[47, 'RETURN', 's57']],
                      [[48, 'VTYPE', 's53'], [48, 'ID', 's54'], [48, 'RBRACE', 'r25'], [48, 'IF', 's51'], [48, 'WHILE', 's52'], [48, 'RETURN', 'r25']],
                      [[49, 'VTYPE', 'r26'], [49, 'ID', 'r26'], [49, 'RBRACE', 'r26'], [49, 'IF', 'r26'], [49, 'WHILE', 'r26'], [49, 'RETURN', 'r26']],
                      [[50, 'SEMI', 's59']],
                      [[51, 'LPAREN', 's60']],
                      [[52, 'LPAREN', 's61']],
                      [[53, 'ID', 's62']],
                      [[54, 'ASSIGN', 's15']],
                      [[55, 'ID', 's63']],
                      [[56, 'RBRACE', 's64']],
                      [[57, 'ID', 's28'], [57, 'STRING', 's22'], [57, 'CHAR', 's23'], [57, 'BOOL', 's24'],  [57, 'LPAREN', 's27'], [57, 'INTEGER', 's29']],
                      [[58, 'RBRACE', 'r24'], [58, 'RETURN', 'r24']],
                      [[59, 'VTYPE', 'r27'], [59, 'ID', 'r27'], [59, 'RBRACE', 'r27'], [59, 'IF', 'r27'], [59, 'WHILE', 'r27'], [59, 'RETURN', 'r27']],
                      [[60, 'BOOL', 's68']],
                      [[61, 'BOOL', 's68']],
                      [[62, 'SEMI', 's13'], [62, 'ASSIGN', 's15']],
                      [[63, 'RPAREN', 'r23'], [63, 'COMMA', 's43']],
                      [[64, 'VTYPE', 'r19'], [64, 'RBRACE', 'r19'], [64, 'CLASS', 'r19'], [64, '$', 'r19']],
                      [[65, 'SEMI', 's71']],
                      [[66, 'RPAREN', 's72']],
                      [[67, 'RPAREN', 'r31'], [67, 'COMP', 's73']],
                      [[68, 'RPAREN', 'r32'], [68, 'COMP', 'r32']],
                      [[69, 'RPAREN', 's74']],
                      [[70, 'RPAREN', 'r22']],
                      [[71, 'RBRACE', 'r35']],
                      [[72, 'LBRACE', 's75']],
                      [[73, 'BOOL', 's68']],
                      [[74, 'LBRACE', 's77']],
                      [[75, 'VTYPE', 's53'], [75, 'ID', 's54'], [75, 'RBRACE', 'r25'], [75, 'IF', 's51'], [75, 'WHILE', 's52'], [75, 'RETURN', 'r25']],
                      [[76, 'RPAREN', 'r30']],
                      [[77, 'VTYPE', 's53'], [77, 'ID', 's54'], [77, 'RBRACE', 'r25'], [77, 'IF', 's51'], [77, 'WHILE', 's52'], [77, 'RETURN', 'r25']],
                      [[78, 'RBRACE', 's80']],
                      [[79, 'RBRACE', 's81']],
                      [[80, 'VTYPE', 'r34'], [80, 'ID', 'r34'], [80, 'RBRACE', 'r34'], [80, 'IF', 'r34'], [80, 'WHILE', 'r34'], [80, 'ELSE', 's83'], [80, 'RETURN', 'r34']],
                      [[81, 'VTYPE', 'r29'], [81, 'VTYPE', 'r29'], [81, 'RBRACE', 'r29'], [81, 'IF', 'r29'], [81, 'WHILE', 'r29'], [81, 'RETURN', 'r29']],
                      [[82, 'VTYPE', 'r28'], [82, 'ID', 'r28'], [81, 'RBRACE', 'r28'], [82, 'IF', 'r28'], [82, 'WHILE', 'r28'], [82, 'RETURN', 'r28']],
                      [[83, 'LBRACE', 's84']],
                      [[84, 'VTYPE', 's53'], [84, 'ID', 's54'], [84, 'RBRACE', 'r25'], [84, 'IF', 's51'], [84, 'WHILE', 's52'], [84, 'RETURN', 'r25']],
                      [[85, 'RBRACE', 's86']],
                      [[86, 'VTYPE', 'r33'], [86, 'ID', 'r33'], [86, 'RBRACE', 'r33'], [86, 'IF', 'r33'], [86, 'WHILE', 'r33'], [86, 'RETURN', 'r33']]],
                     [[[0, 'CODE', 1], [0, 'VDECL', 2], [0, 'FDECL', 3], [0, 'CDECL', 4]],
                      [],
                      [[2, 'CODE', 7], [2, 'VDECL', 2], [2, 'FDECL', 3], [2, 'CDECL', 4]],
                      [[3, 'CODE', 8], [3, 'VDECL', 2], [3, 'FDECL', 3], [3, 'CDECL', 4]],
                      [[4, 'CODE', 9], [4, 'VDECL', 2], [4, 'FDECL', 3], [4, 'CDECL', 4]],
                      [[5, 'GOTO_ASSIGN', 11]],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [[14, 'ARG', 18]],
                      [[15, 'RHS', 20], [15, 'EXPR', 21], [15, 'TERM', 25], [15, 'FACTOR', 26]],
                      [],
                      [[17, 'VDECL', 31], [17, 'FDECL', 32], [17, 'ODECL', 30]],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [[27, 'EXPR', 37], [27, 'TERM', 25], [27, 'FACTOR', 26]],
                      [],
                      [],
                      [],
                      [[31, 'VDECL', 31], [31, 'FDECL', 32], [31, 'ODECL', 39]],
                      [[32, 'VDECL', 31], [32, 'FDECL', 32], [32, 'ODECL', 40]],
                      [],
                      [[34, 'MOREARGS', 42]],
                      [[35, 'EXPR', 44], [35, 'TERM', 25], [35, 'FACTOR', 26]],
                      [[36, 'TERM', 45], [36, 'FACTOR', 26]],
                      [],
                      [],
                      [],
                      [],
                      [[41, 'VDECL', 49], [41, 'GOTO_ASSIGN', 50], [41, 'BLOCK', 47], [41, 'STMT', 48]],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [[47, 'GOTO_RETURN', 56]],
                      [[48, 'VDECL', 49], [48, 'GOTO_ASSIGN', 50], [48, 'BLOCK', 58], [48, 'STMT', 48]],
                      [],
                      [],
                      [],
                      [],
                      [[53, 'GOTO_ASSIGN', 11]],
                      [],
                      [],
                      [],
                      [[57, 'RHS', 65], [57, 'EXPR', 21], [57, 'TERM', 25], [57, 'FACTOR', 26]],
                      [],
                      [],
                      [[60, 'COND', 66], [60, "COND'", 67]],
                      [[61, 'COND', 69], [61, "COND'", 67]],
                      [],
                      [[63, 'MOREARGS', 70]],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [[73, 'COND', 76], [73, "COND'", 67]],
                      [],
                      [[75, 'VDECL', 49], [75, 'GOTO_ASSIGN', 50], [75, 'BLOCK', 78], [75, 'STMT', 48]],
                      [],
                      [[77, 'VDECL', 49], [77, 'GOTO_ASSIGN', 50], [77, 'BLOCK', 79], [77, 'STMT', 48]],
                      [],
                      [],
                      [[80, 'GOTO_ELSE', 82]],
                      [],
                      [],
                      [],
                      [[84, 'VDECL', 49], [84, 'VDECL', 50], [84, 'BLOCK', 85], [84, 'STMT', 48]],
                      [],
                      []])
