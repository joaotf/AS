
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programleftLPARENRPARENleftLOGOU_LOGICOleftMAIORMENORMAIOREQUALSMENOREQUALSEQUALITYDIFERENTEleftPLUSMINUSleftTIMESDIVIDEASPAS ATRIBUTION COMMENT DIFERENTE DIVIDE DO ELSE EQUALITY FALSE FLOAT FOR IDENTIFIER IF INTEGER LBRACE LCOLCHETE LOG LPAREN MAIOR MAIOREQUALS MENOR MENOREQUALS MINUS MINUSMINUS OU_LOGICO PLUS PLUSPLUS PRINT RBRACE RCOLCHETE READ RPAREN SEMI STRING STRINGS TIMES TIMESX TRUE WHILEprogram : declaration_listdeclaration_list : declaration_list  declaration\n   \t\t\t\t\t   | declaration\n   declaration : var_declaration\n\t\t\t\t   | print_stmt\n\t\t\t\t   | read_stmt\n\t\t\t\t   | selection_stmt\n\t\t\t       | iteration_stmt\n\t\t\t\t   | expression\n\tprint_stmt   : PRINT LPAREN STRING RPAREN SEMI declaration\n\t\t\t\t\t| PRINT LPAREN STRING RPAREN SEMI \n\t\t\t\t    | PRINT LPAREN IDENTIFIER RPAREN SEMI declaration\n\t\t\t\t\t| PRINT LPAREN IDENTIFIER RPAREN SEMI \n\t\t\t\t    | PRINT LPAREN NUMBER RPAREN SEMI declaration\n\t\t\t\t\t| PRINT LPAREN NUMBER RPAREN SEMI \n\t\t\t\t    | PRINT LPAREN boolean RPAREN SEMI declaration\n\t\t\t\t\t| PRINT LPAREN boolean RPAREN SEMI \n                    | PRINT LPAREN expression RPAREN SEMI declaration\n\t\t\t\t\t| PRINT LPAREN expression RPAREN SEMI \n                    | PRINT LPAREN RPAREN SEMI declaration\n\t\t\t\t\t| PRINT LPAREN RPAREN SEMI \n\tvar_declaration : IDENTIFIER var_declaration\n                       | IDENTIFIER \n                       | IDENTIFIER ATRIBUTION NUMBER var_declaration\n                       | IDENTIFIER ATRIBUTION NUMBER SEMI\n                       | IDENTIFIER ATRIBUTION boolean var_declaration\n                       | IDENTIFIER ATRIBUTION boolean SEMI\n                       | IDENTIFIER ATRIBUTION IDENTIFIER var_declaration\n                       | IDENTIFIER ATRIBUTION IDENTIFIER SEMI\n                       | IDENTIFIER ATRIBUTION simple_expression SEMI\n\tstatement : expression_stmt\n\t\t\t\t | selection_stmt\n\t\t\t\t | iteration_stmt\n\t\t\t\t | print_stmt\n\t\t\t\t | read_stmt\n\texpression_stmt : expressionselection_stmt : IF LPAREN expression RPAREN LBRACE expression RBRACE ELSE LBRACE expression RBRACE statement\n\t\t\t\t\t  | IF LPAREN expression RPAREN LBRACE expression RBRACE statement \n\t\t\t\t\t  | IF LPAREN expression RPAREN LBRACE declaration RBRACE\n\t\t\t\t\t  | IF LPAREN expression RPAREN LBRACE declaration RBRACE ELSE LBRACE declaration RBRACE\n\t\t\t\t\t  \n\titeration_stmt : FOR LPAREN var_declaration expression SEMI additive_expression RPAREN LBRACE expression RBRACE statement \n\t\t\t\t\t  | FOR LPAREN var_declaration expression SEMI additive_expression RPAREN LBRACE print_stmt RBRACE\n\titeration_stmt : WHILE LPAREN expression RPAREN LBRACE expression RBRACE statement\n\t\t\t\t\t  | WHILE LPAREN expression RPAREN LBRACE statement RBRACE\n\titeration_stmt : DO LBRACE statement SEMI RBRACE WHILE LPAREN expression RPAREN SEMI\n\t\t\t\t\t  | DO LBRACE print_stmt RBRACE WHILE LPAREN expression RPAREN SEMI\n\t\t\t\t\t  | DO LBRACE read_stmt RBRACE WHILE LPAREN expression RPAREN SEMI\n\t\t\t\t\t  | DO LBRACE selection_stmt RBRACE WHILE LPAREN expression RPAREN SEMI statement\n\t\t\t\t\t  | DO LBRACE selection_stmt RBRACE WHILE LPAREN expression RPAREN SEMI \n\t\n\t\tread_stmt : READ LPAREN STRING RPAREN SEMI declaration\n\t\t\t\t  | READ LPAREN STRING RPAREN SEMI \n\t\t\t      | IDENTIFIER ATRIBUTION READ LPAREN STRING RPAREN SEMI\n\t\t\t\t  | IDENTIFIER ATRIBUTION READ LPAREN RPAREN SEMI\n\texpression : IDENTIFIER EQUALITY expression\n\t\t\t\t  | simple_expression\n\t\t\t\t  | IDENTIFIER EQUALITY IDENTIFIER\n\t\t\t      | expression LOG expression\n\t\t\t\t  | expression OU_LOGICO expression\n\tsimple_expression : additive_expression relop additive_expression\n\t\t\t\t\t\t | additive_expression\n\trelop : MENOR\n\t\t\t | MENOREQUALS\n\t\t\t | MAIOR\n\t\t\t | MAIOREQUALS\n\t\t\t | DIFERENTE\n             | EQUALITY\n\tadditive_expression : additive_expression addop term\n    \t\t\t\t\t   | term \n    \t\t\t\t\t   | term MINUSMINUS\n    \t\t\t\t       | term PLUSPLUS\n\taddop : PLUS\n\t\t\t | MINUS\n\tterm : term mulop factor\n\t\t\t| factor\n\tmulop : TIMES\n\t\t\t | DIVIDE\n\tfactor : LPAREN expression RPAREN\n\t\t\t  | IDENTIFIER\n\t\t\t  | NUMBER\n\t\t\t  | boolean\n\t\t\t  | IDENTIFIER LPAREN args RPAREN\n\tboolean : TRUE\n\t\t\t   | FALSE\n\tNUMBER : INTEGER\n\t\t\t  | FLOAT\n\targs : args_list\n\t\t\t| empty\n\targs_list : expressionexpression : expression PLUS term\n                  | expression MINUS term\n                  | expression TIMES term\n                  | expression DIVIDE term\n                  | expression TIMESX term\n                  | expression LOG term\n                  | expression OU_LOGICO term\n    empty :'
    
_lr_action_items = {'IDENTIFIER':([0,2,3,4,5,6,7,8,9,10,11,12,13,15,19,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,84,85,92,95,96,97,100,104,105,106,107,108,109,110,111,112,113,114,116,118,134,135,136,137,138,139,140,141,142,143,149,150,151,152,153,154,155,158,163,164,165,167,168,169,170,171,172,174,175,176,181,183,184,189,190,194,195,196,199,200,201,202,203,204,205,206,],[10,10,-3,-4,-5,-6,-7,-8,-9,36,-79,-80,-55,43,-60,-68,-74,-84,-85,-82,-83,-2,43,43,69,69,69,69,69,36,-22,75,43,84,88,-78,43,36,69,69,-61,-62,-63,-64,-65,-66,-71,-72,43,106,-69,-70,69,-75,-76,-57,-68,-58,-68,-89,-78,-90,-91,-92,-93,75,36,36,36,-56,-54,-77,43,-59,-67,-36,-31,-33,-78,-73,-28,-29,-24,-25,-26,-27,-30,-81,10,10,-20,10,10,10,10,10,158,69,162,-53,-10,-12,-14,-16,-18,-50,36,-32,-34,-35,43,43,43,-52,106,-39,106,-44,43,-38,43,-43,43,10,-46,-47,106,106,-42,-45,-48,106,-40,-41,-37,]),'PRINT':([0,2,3,4,5,6,7,8,9,10,11,12,13,19,22,23,24,25,26,27,28,36,37,43,58,59,60,64,65,66,67,68,69,70,71,72,73,84,85,92,96,97,100,104,105,106,107,108,109,110,111,112,113,114,116,118,134,135,136,137,138,139,140,141,143,149,150,151,152,153,154,155,163,164,165,170,171,172,174,175,181,183,184,190,194,195,196,199,200,201,202,203,204,205,206,],[14,14,-3,-4,-5,-6,-7,-8,-9,-23,-79,-80,-55,-60,-68,-74,-84,-85,-82,-83,-2,-23,-22,-78,14,-69,-70,-57,-68,-58,-68,-89,-78,-90,-91,-92,-93,-56,-54,-77,-59,-67,-36,-31,-33,-78,-73,-28,-29,-24,-25,-26,-27,-30,-81,14,14,-20,14,14,14,14,14,14,14,-53,-10,-12,-14,-16,-18,-50,-32,-34,-35,-52,14,-39,14,-44,-38,14,-43,14,-46,-47,14,14,-42,-45,-48,14,-40,-41,-37,]),'READ':([0,2,3,4,5,6,7,8,9,10,11,12,13,19,22,23,24,25,26,27,28,36,37,38,43,58,59,60,64,65,66,67,68,69,70,71,72,73,84,85,92,96,97,100,104,105,106,107,108,109,110,111,112,113,114,116,118,131,134,135,136,137,138,139,140,141,143,149,150,151,152,153,154,155,163,164,165,170,171,172,174,175,181,184,190,194,195,196,199,200,201,202,203,204,205,206,],[16,16,-3,-4,-5,-6,-7,-8,-9,-23,-79,-80,-55,-60,-68,-74,-84,-85,-82,-83,-2,-23,-22,79,-78,16,-69,-70,-57,-68,-58,-68,-89,-78,-90,-91,-92,-93,-56,-54,-77,-59,-67,-36,-31,-33,-78,-73,-28,-29,-24,-25,-26,-27,-30,-81,16,79,16,-20,16,16,16,16,16,16,16,-53,-10,-12,-14,-16,-18,-50,-32,-34,-35,-52,16,-39,16,-44,-38,-43,16,-46,-47,16,16,-42,-45,-48,16,-40,-41,-37,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,12,13,19,22,23,24,25,26,27,28,36,37,43,58,59,60,64,65,66,67,68,69,70,71,72,73,84,85,92,96,97,100,104,105,106,107,108,109,110,111,112,113,114,116,118,134,135,136,137,138,139,140,141,143,149,150,151,152,153,154,155,163,164,165,170,171,172,174,175,181,184,190,194,195,196,199,200,201,202,203,204,205,206,],[17,17,-3,-4,-5,-6,-7,-8,-9,-23,-79,-80,-55,-60,-68,-74,-84,-85,-82,-83,-2,-23,-22,-78,17,-69,-70,-57,-68,-58,-68,-89,-78,-90,-91,-92,-93,-56,-54,-77,-59,-67,-36,-31,-33,-78,-73,-28,-29,-24,-25,-26,-27,-30,-81,17,17,-20,17,17,17,17,17,17,17,-53,-10,-12,-14,-16,-18,-50,-32,-34,-35,-52,17,-39,17,-44,-38,-43,17,-46,-47,17,17,-42,-45,-48,17,-40,-41,-37,]),'FOR':([0,2,3,4,5,6,7,8,9,10,11,12,13,19,22,23,24,25,26,27,28,36,37,43,58,59,60,64,65,66,67,68,69,70,71,72,73,84,85,92,96,97,100,104,105,106,107,108,109,110,111,112,113,114,116,118,134,135,136,137,138,139,140,141,143,149,150,151,152,153,154,155,163,164,165,170,171,172,174,175,181,184,190,194,195,196,199,200,201,202,203,204,205,206,],[18,18,-3,-4,-5,-6,-7,-8,-9,-23,-79,-80,-55,-60,-68,-74,-84,-85,-82,-83,-2,-23,-22,-78,18,-69,-70,-57,-68,-58,-68,-89,-78,-90,-91,-92,-93,-56,-54,-77,-59,-67,-36,-31,-33,-78,-73,-28,-29,-24,-25,-26,-27,-30,-81,18,18,-20,18,18,18,18,18,18,18,-53,-10,-12,-14,-16,-18,-50,-32,-34,-35,-52,18,-39,18,-44,-38,-43,18,-46,-47,18,18,-42,-45,-48,18,-40,-41,-37,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,19,22,23,24,25,26,27,28,36,37,43,58,59,60,64,65,66,67,68,69,70,71,72,73,84,85,92,96,97,100,104,105,106,107,108,109,110,111,112,113,114,116,118,128,129,130,134,135,136,137,138,139,140,141,143,144,149,150,151,152,153,154,155,163,164,165,170,171,172,174,175,181,184,190,194,195,196,199,200,201,202,203,204,205,206,],[20,20,-3,-4,-5,-6,-7,-8,-9,-23,-79,-80,-55,-60,-68,-74,-84,-85,-82,-83,-2,-23,-22,-78,20,-69,-70,-57,-68,-58,-68,-89,-78,-90,-91,-92,-93,-56,-54,-77,-59,-67,-36,-31,-33,-78,-73,-28,-29,-24,-25,-26,-27,-30,-81,20,145,146,147,20,-20,20,20,20,20,20,20,20,166,-53,-10,-12,-14,-16,-18,-50,-32,-34,-35,-52,20,-39,20,-44,-38,-43,20,-46,-47,20,20,-42,-45,-48,20,-40,-41,-37,]),'DO':([0,2,3,4,5,6,7,8,9,10,11,12,13,19,22,23,24,25,26,27,28,36,37,43,58,59,60,64,65,66,67,68,69,70,71,72,73,84,85,92,96,97,100,104,105,106,107,108,109,110,111,112,113,114,116,118,134,135,136,137,138,139,140,141,143,149,150,151,152,153,154,155,163,164,165,170,171,172,174,175,181,184,190,194,195,196,199,200,201,202,203,204,205,206,],[21,21,-3,-4,-5,-6,-7,-8,-9,-23,-79,-80,-55,-60,-68,-74,-84,-85,-82,-83,-2,-23,-22,-78,21,-69,-70,-57,-68,-58,-68,-89,-78,-90,-91,-92,-93,-56,-54,-77,-59,-67,-36,-31,-33,-78,-73,-28,-29,-24,-25,-26,-27,-30,-81,21,21,-20,21,21,21,21,21,21,21,-53,-10,-12,-14,-16,-18,-50,-32,-34,-35,-52,21,-39,21,-44,-38,-43,21,-46,-47,21,21,-42,-45,-48,21,-40,-41,-37,]),'LPAREN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,84,85,88,92,95,96,97,100,104,105,106,107,108,109,110,111,112,113,114,116,118,134,135,136,137,138,139,140,141,142,143,145,146,147,149,150,151,152,153,154,155,158,162,163,164,165,166,167,168,169,170,171,172,174,175,176,181,183,184,189,190,194,195,196,199,200,201,202,203,204,205,206,],[15,15,-3,-4,-5,-6,-7,-8,-9,39,-79,-80,-55,41,15,44,45,46,-60,57,-68,-74,-84,-85,-82,-83,-2,15,15,15,15,15,15,15,-23,-22,15,15,15,15,39,15,15,15,-61,-62,-63,-64,-65,-66,-71,-72,15,15,-69,-70,15,-75,-76,-57,-68,-58,-68,-89,39,-90,-91,-92,-93,15,39,115,39,-54,39,-77,15,-59,-67,-36,-31,-33,39,-73,-28,-29,-24,-25,-26,-27,-30,-81,15,15,-20,15,15,15,15,15,15,15,15,167,168,169,-53,-10,-12,-14,-16,-18,-50,39,39,-32,-34,-35,176,15,15,15,-52,15,-39,15,-44,15,-38,15,-43,15,15,-46,-47,15,15,-42,-45,-48,15,-40,-41,-37,]),'INTEGER':([0,2,3,4,5,6,7,8,9,10,11,12,13,15,19,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,84,85,92,95,96,97,100,104,105,106,107,108,109,110,111,112,113,114,116,118,134,135,136,137,138,139,140,141,142,143,149,150,151,152,153,154,155,163,164,165,167,168,169,170,171,172,174,175,176,181,183,184,189,190,194,195,196,199,200,201,202,203,204,205,206,],[24,24,-3,-4,-5,-6,-7,-8,-9,-23,-79,-80,-55,24,-60,-68,-74,-84,-85,-82,-83,-2,24,24,24,24,24,24,24,-23,-22,24,24,24,24,-78,24,24,24,-61,-62,-63,-64,-65,-66,-71,-72,24,24,-69,-70,24,-75,-76,-57,-68,-58,-68,-89,-78,-90,-91,-92,-93,24,-56,-54,-77,24,-59,-67,-36,-31,-33,-78,-73,-28,-29,-24,-25,-26,-27,-30,-81,24,24,-20,24,24,24,24,24,24,24,24,-53,-10,-12,-14,-16,-18,-50,-32,-34,-35,24,24,24,-52,24,-39,24,-44,24,-38,24,-43,24,24,-46,-47,24,24,-42,-45,-48,24,-40,-41,-37,]),'FLOAT':([0,2,3,4,5,6,7,8,9,10,11,12,13,15,19,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,84,85,92,95,96,97,100,104,105,106,107,108,109,110,111,112,113,114,116,118,134,135,136,137,138,139,140,141,142,143,149,150,151,152,153,154,155,163,164,165,167,168,169,170,171,172,174,175,176,181,183,184,189,190,194,195,196,199,200,201,202,203,204,205,206,],[25,25,-3,-4,-5,-6,-7,-8,-9,-23,-79,-80,-55,25,-60,-68,-74,-84,-85,-82,-83,-2,25,25,25,25,25,25,25,-23,-22,25,25,25,25,-78,25,25,25,-61,-62,-63,-64,-65,-66,-71,-72,25,25,-69,-70,25,-75,-76,-57,-68,-58,-68,-89,-78,-90,-91,-92,-93,25,-56,-54,-77,25,-59,-67,-36,-31,-33,-78,-73,-28,-29,-24,-25,-26,-27,-30,-81,25,25,-20,25,25,25,25,25,25,25,25,-53,-10,-12,-14,-16,-18,-50,-32,-34,-35,25,25,25,-52,25,-39,25,-44,25,-38,25,-43,25,25,-46,-47,25,25,-42,-45,-48,25,-40,-41,-37,]),'TRUE':([0,2,3,4,5,6,7,8,9,10,11,12,13,15,19,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,84,85,92,95,96,97,100,104,105,106,107,108,109,110,111,112,113,114,116,118,134,135,136,137,138,139,140,141,142,143,149,150,151,152,153,154,155,163,164,165,167,168,169,170,171,172,174,175,176,181,183,184,189,190,194,195,196,199,200,201,202,203,204,205,206,],[26,26,-3,-4,-5,-6,-7,-8,-9,-23,-79,-80,-55,26,-60,-68,-74,-84,-85,-82,-83,-2,26,26,26,26,26,26,26,-23,-22,26,26,26,26,-78,26,26,26,-61,-62,-63,-64,-65,-66,-71,-72,26,26,-69,-70,26,-75,-76,-57,-68,-58,-68,-89,-78,-90,-91,-92,-93,26,-56,-54,-77,26,-59,-67,-36,-31,-33,-78,-73,-28,-29,-24,-25,-26,-27,-30,-81,26,26,-20,26,26,26,26,26,26,26,26,-53,-10,-12,-14,-16,-18,-50,-32,-34,-35,26,26,26,-52,26,-39,26,-44,26,-38,26,-43,26,26,-46,-47,26,26,-42,-45,-48,26,-40,-41,-37,]),'FALSE':([0,2,3,4,5,6,7,8,9,10,11,12,13,15,19,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,84,85,92,95,96,97,100,104,105,106,107,108,109,110,111,112,113,114,116,118,134,135,136,137,138,139,140,141,142,143,149,150,151,152,153,154,155,163,164,165,167,168,169,170,171,172,174,175,176,181,183,184,189,190,194,195,196,199,200,201,202,203,204,205,206,],[27,27,-3,-4,-5,-6,-7,-8,-9,-23,-79,-80,-55,27,-60,-68,-74,-84,-85,-82,-83,-2,27,27,27,27,27,27,27,-23,-22,27,27,27,27,-78,27,27,27,-61,-62,-63,-64,-65,-66,-71,-72,27,27,-69,-70,27,-75,-76,-57,-68,-58,-68,-89,-78,-90,-91,-92,-93,27,-56,-54,-77,27,-59,-67,-36,-31,-33,-78,-73,-28,-29,-24,-25,-26,-27,-30,-81,27,27,-20,27,27,27,27,27,27,27,27,-53,-10,-12,-14,-16,-18,-50,-32,-34,-35,27,27,27,-52,27,-39,27,-44,27,-38,27,-43,27,27,-46,-47,27,27,-42,-45,-48,27,-40,-41,-37,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,19,22,23,24,25,26,27,28,36,37,43,59,60,64,65,66,67,68,69,70,71,72,73,84,85,92,96,97,100,104,105,106,107,108,109,110,111,112,113,114,116,118,134,135,136,137,138,139,140,149,150,151,152,153,154,155,163,164,165,170,172,175,181,184,194,195,196,200,201,202,204,205,206,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-23,-79,-80,-55,-60,-68,-74,-84,-85,-82,-83,-2,-23,-22,-78,-69,-70,-57,-68,-58,-68,-89,-78,-90,-91,-92,-93,-56,-54,-77,-59,-67,-36,-31,-33,-78,-73,-28,-29,-24,-25,-26,-27,-30,-81,-21,-11,-20,-13,-15,-17,-19,-51,-53,-10,-12,-14,-16,-18,-50,-32,-34,-35,-52,-39,-44,-38,-43,-46,-47,-49,-42,-45,-48,-40,-41,-37,]),'RBRACE':([4,5,6,7,8,9,10,11,12,13,19,22,23,24,25,26,27,36,37,43,59,60,64,65,66,67,68,69,70,71,72,73,84,85,92,96,97,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,116,118,127,134,135,136,137,138,139,140,149,150,151,152,153,154,155,156,157,158,160,161,162,163,164,165,170,172,175,181,184,191,192,194,195,196,197,198,200,201,202,204,205,206,],[-4,-5,-6,-7,-8,-9,-23,-79,-80,-55,-60,-68,-74,-84,-85,-82,-83,-23,-22,-78,-69,-70,-57,-68,-58,-68,-89,-78,-90,-91,-92,-93,-56,-54,-77,-59,-67,-36,128,129,130,-31,-33,-78,-73,-28,-29,-24,-25,-26,-27,-30,-81,-21,144,-11,-20,-13,-15,-17,-19,-51,-53,-10,-12,-14,-16,-18,-50,171,172,-23,174,175,-78,-32,-34,-35,-52,-39,-44,-38,-43,199,200,-46,-47,-49,203,204,-42,-45,-48,-40,-41,-37,]),'SEMI':([4,5,6,7,8,9,10,11,12,13,19,22,23,24,25,26,27,36,37,43,59,60,64,65,66,67,68,69,70,71,72,73,75,76,77,78,84,85,87,92,96,97,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,116,117,118,119,120,121,122,123,125,133,134,135,136,137,138,139,140,148,149,150,151,152,153,154,155,163,164,165,170,172,175,181,184,186,187,188,193,194,195,196,200,201,202,204,205,206,],[-4,-5,-6,-7,-8,-9,-23,-79,-80,-55,-60,-68,-74,-84,-85,-82,-83,-23,-22,-78,-69,-70,-57,-68,-58,-68,-89,-78,-90,-91,-92,-93,109,111,113,114,-56,-54,118,-77,-59,-67,127,-36,-34,-35,-32,-31,-33,-78,-73,-28,-29,-24,-25,-26,-27,-30,-81,134,-21,136,137,138,139,140,142,149,-11,-20,-13,-15,-17,-19,-51,170,-53,-10,-12,-14,-16,-18,-50,-32,-34,-35,-52,-39,-44,-38,-43,194,195,196,201,-46,-47,-49,-42,-45,-48,-40,-41,-37,]),'LOG':([9,10,11,12,13,19,22,23,24,25,26,27,42,43,59,60,64,65,66,67,68,69,70,71,72,73,83,84,85,88,89,90,91,92,94,96,97,98,100,106,107,116,125,156,158,160,162,177,178,179,185,191,197,],[29,-78,-79,-80,-55,-60,-68,-74,-84,-85,-82,-83,29,-78,-69,-70,-57,-68,-58,-68,-89,-78,-90,-91,-92,-93,29,-56,-54,-78,-79,-80,29,-77,29,-59,-67,29,29,-78,-73,-81,29,29,-78,29,-78,29,29,29,29,29,29,]),'OU_LOGICO':([9,10,11,12,13,19,22,23,24,25,26,27,42,43,59,60,64,65,66,67,68,69,70,71,72,73,83,84,85,88,89,90,91,92,94,96,97,98,100,106,107,116,125,156,158,160,162,177,178,179,185,191,197,],[30,-78,-79,-80,-55,-60,-68,-74,-84,-85,-82,-83,30,-78,-69,-70,-57,-68,-58,-68,-89,-78,-90,-91,-92,-93,30,-56,-54,-78,-79,-80,30,-77,30,-59,-67,30,30,-78,-73,-81,30,30,-78,30,-78,30,30,30,30,30,30,]),'PLUS':([9,10,11,12,13,19,22,23,24,25,26,27,42,43,59,60,64,65,66,67,68,69,70,71,72,73,75,76,77,83,84,85,88,89,90,91,92,94,96,97,98,100,106,107,116,125,156,158,159,160,162,177,178,179,185,191,197,],[31,-78,-79,-80,-55,55,-68,-74,-84,-85,-82,-83,31,-78,-69,-70,31,-68,31,-68,-89,-78,-90,-91,-92,-93,-78,-79,-80,31,-56,31,-78,-79,-80,31,-77,31,55,-67,31,31,-78,-73,-81,31,31,-78,55,31,-78,31,31,31,31,31,31,]),'MINUS':([9,10,11,12,13,19,22,23,24,25,26,27,42,43,59,60,64,65,66,67,68,69,70,71,72,73,75,76,77,83,84,85,88,89,90,91,92,94,96,97,98,100,106,107,116,125,156,158,159,160,162,177,178,179,185,191,197,],[32,-78,-79,-80,-55,56,-68,-74,-84,-85,-82,-83,32,-78,-69,-70,32,-68,32,-68,-89,-78,-90,-91,-92,-93,-78,-79,-80,32,-56,32,-78,-79,-80,32,-77,32,56,-67,32,32,-78,-73,-81,32,32,-78,56,32,-78,32,32,32,32,32,32,]),'TIMES':([9,10,11,12,13,19,22,23,24,25,26,27,42,43,59,60,64,65,66,67,68,69,70,71,72,73,75,76,77,83,84,85,88,89,90,91,92,94,96,97,98,100,106,107,116,125,156,158,160,162,177,178,179,185,191,197,],[33,-78,-79,-80,-55,-60,62,-74,-84,-85,-82,-83,33,-78,-69,-70,33,62,33,62,62,-78,62,-91,-92,62,-78,-79,-80,33,-56,33,-78,-79,-80,33,-77,33,-59,62,33,33,-78,-73,-81,33,33,-78,33,-78,33,33,33,33,33,33,]),'DIVIDE':([9,10,11,12,13,19,22,23,24,25,26,27,42,43,59,60,64,65,66,67,68,69,70,71,72,73,75,76,77,83,84,85,88,89,90,91,92,94,96,97,98,100,106,107,116,125,156,158,160,162,177,178,179,185,191,197,],[34,-78,-79,-80,-55,-60,63,-74,-84,-85,-82,-83,34,-78,-69,-70,34,63,34,63,63,-78,63,-91,-92,63,-78,-79,-80,34,-56,34,-78,-79,-80,34,-77,34,-59,63,34,34,-78,-73,-81,34,34,-78,34,-78,34,34,34,34,34,34,]),'TIMESX':([9,10,11,12,13,19,22,23,24,25,26,27,42,43,59,60,64,65,66,67,68,69,70,71,72,73,83,84,85,88,89,90,91,92,94,96,97,98,100,106,107,116,125,156,158,160,162,177,178,179,185,191,197,],[35,-78,-79,-80,-55,-60,-68,-74,-84,-85,-82,-83,35,-78,-69,-70,-57,-68,-58,-68,-89,-78,-90,-91,-92,-93,35,-56,-54,-78,-79,-80,35,-77,35,-59,-67,35,35,-78,-73,-81,35,35,-78,35,-78,35,35,35,35,35,35,]),'ATRIBUTION':([10,36,106,158,162,],[38,74,131,38,131,]),'EQUALITY':([10,11,12,19,22,23,24,25,26,27,43,59,60,65,67,69,75,76,77,84,88,89,90,92,97,106,107,116,158,162,],[40,-79,-80,54,-68,-74,-84,-85,-82,-83,40,-69,-70,-68,-68,-78,-78,-79,-80,40,40,-79,-80,-77,-67,40,-73,-81,40,40,]),'MINUSMINUS':([10,11,12,22,23,24,25,26,27,43,65,67,69,75,76,77,84,88,89,90,92,106,107,116,158,162,],[-78,-79,-80,59,-74,-84,-85,-82,-83,-78,59,59,-78,-78,-79,-80,-78,-78,-79,-80,-77,-78,-73,-81,-78,-78,]),'PLUSPLUS':([10,11,12,22,23,24,25,26,27,43,65,67,69,75,76,77,84,88,89,90,92,106,107,116,158,162,],[-78,-79,-80,60,-74,-84,-85,-82,-83,-78,60,60,-78,-78,-79,-80,-78,-78,-79,-80,-77,-78,-73,-81,-78,-78,]),'MENOR':([10,11,12,19,22,23,24,25,26,27,43,59,60,65,67,69,75,76,77,84,88,89,90,92,97,106,107,116,158,162,],[-78,-79,-80,49,-68,-74,-84,-85,-82,-83,-78,-69,-70,-68,-68,-78,-78,-79,-80,-78,-78,-79,-80,-77,-67,-78,-73,-81,-78,-78,]),'MENOREQUALS':([10,11,12,19,22,23,24,25,26,27,43,59,60,65,67,69,75,76,77,84,88,89,90,92,97,106,107,116,158,162,],[-78,-79,-80,50,-68,-74,-84,-85,-82,-83,-78,-69,-70,-68,-68,-78,-78,-79,-80,-78,-78,-79,-80,-77,-67,-78,-73,-81,-78,-78,]),'MAIOR':([10,11,12,19,22,23,24,25,26,27,43,59,60,65,67,69,75,76,77,84,88,89,90,92,97,106,107,116,158,162,],[-78,-79,-80,51,-68,-74,-84,-85,-82,-83,-78,-69,-70,-68,-68,-78,-78,-79,-80,-78,-78,-79,-80,-77,-67,-78,-73,-81,-78,-78,]),'MAIOREQUALS':([10,11,12,19,22,23,24,25,26,27,43,59,60,65,67,69,75,76,77,84,88,89,90,92,97,106,107,116,158,162,],[-78,-79,-80,52,-68,-74,-84,-85,-82,-83,-78,-69,-70,-68,-68,-78,-78,-79,-80,-78,-78,-79,-80,-77,-67,-78,-73,-81,-78,-78,]),'DIFERENTE':([10,11,12,19,22,23,24,25,26,27,43,59,60,65,67,69,75,76,77,84,88,89,90,92,97,106,107,116,158,162,],[-78,-79,-80,53,-68,-74,-84,-85,-82,-83,-78,-69,-70,-68,-68,-78,-78,-79,-80,-78,-78,-79,-80,-77,-67,-78,-73,-81,-78,-78,]),'RPAREN':([11,12,13,19,22,23,24,25,26,27,39,41,42,43,59,60,64,65,66,67,68,69,70,71,72,73,80,81,82,83,84,85,86,88,89,90,91,92,93,94,96,97,98,107,115,116,132,159,177,178,179,185,],[-79,-80,-55,-60,-68,-74,-84,-85,-82,-83,-96,87,92,-78,-69,-70,-57,-68,-58,-68,-89,-78,-90,-91,-92,-93,116,-86,-87,-88,-56,-54,117,119,120,121,122,-77,123,124,-59,-67,126,-73,133,-81,148,173,186,187,188,193,]),'LBRACE':([21,124,126,173,180,182,],[58,141,143,183,189,190,]),'STRING':([41,44,115,],[86,93,132,]),'ELSE':([171,172,],[180,182,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declaration_list':([0,],[2,]),'declaration':([0,2,118,134,136,137,138,139,140,141,190,],[3,28,135,150,151,152,153,154,155,157,198,]),'var_declaration':([0,2,10,36,46,75,76,77,118,134,136,137,138,139,140,141,158,190,],[4,4,37,37,95,108,110,112,4,4,4,4,4,4,4,4,37,4,]),'print_stmt':([0,2,58,118,134,136,137,138,139,140,141,143,171,174,183,190,196,199,203,],[5,5,101,5,5,5,5,5,5,5,5,164,164,164,192,5,164,164,164,]),'read_stmt':([0,2,58,118,134,136,137,138,139,140,141,143,171,174,190,196,199,203,],[6,6,102,6,6,6,6,6,6,6,6,165,165,165,6,165,165,165,]),'selection_stmt':([0,2,58,118,134,136,137,138,139,140,141,143,171,174,190,196,199,203,],[7,7,103,7,7,7,7,7,7,7,7,163,163,163,7,163,163,163,]),'iteration_stmt':([0,2,58,118,134,136,137,138,139,140,141,143,171,174,190,196,199,203,],[8,8,105,8,8,8,8,8,8,8,8,105,105,105,8,105,105,105,]),'expression':([0,2,15,29,30,39,40,41,45,57,58,95,118,134,136,137,138,139,140,141,143,167,168,169,171,174,176,183,189,190,196,199,203,],[9,9,42,64,66,83,85,91,94,98,100,125,9,9,9,9,9,9,9,156,160,177,178,179,100,100,185,191,197,9,100,100,100,]),'NUMBER':([0,2,15,29,30,31,32,33,34,35,38,39,40,41,45,47,48,57,58,61,74,95,118,134,136,137,138,139,140,141,142,143,167,168,169,171,174,176,183,189,190,196,199,203,],[11,11,11,11,11,11,11,11,11,11,76,11,11,89,11,11,11,11,11,11,76,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'boolean':([0,2,15,29,30,31,32,33,34,35,38,39,40,41,45,47,48,57,58,61,74,95,118,134,136,137,138,139,140,141,142,143,167,168,169,171,174,176,183,189,190,196,199,203,],[12,12,12,12,12,12,12,12,12,12,77,12,12,90,12,12,12,12,12,12,77,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'simple_expression':([0,2,15,29,30,38,39,40,41,45,57,58,74,95,118,134,136,137,138,139,140,141,143,167,168,169,171,174,176,183,189,190,196,199,203,],[13,13,13,13,13,78,13,13,13,13,13,13,78,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'additive_expression':([0,2,15,29,30,38,39,40,41,45,47,57,58,74,95,118,134,136,137,138,139,140,141,142,143,167,168,169,171,174,176,183,189,190,196,199,203,],[19,19,19,19,19,19,19,19,19,19,96,19,19,19,19,19,19,19,19,19,19,19,19,159,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'term':([0,2,15,29,30,31,32,33,34,35,38,39,40,41,45,47,48,57,58,74,95,118,134,136,137,138,139,140,141,142,143,167,168,169,171,174,176,183,189,190,196,199,203,],[22,22,22,65,67,68,70,71,72,73,22,22,22,22,22,22,97,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'factor':([0,2,15,29,30,31,32,33,34,35,38,39,40,41,45,47,48,57,58,61,74,95,118,134,136,137,138,139,140,141,142,143,167,168,169,171,174,176,183,189,190,196,199,203,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,107,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'relop':([19,],[47,]),'addop':([19,96,159,],[48,48,48,]),'mulop':([22,65,67,68,70,71,72,73,97,],[61,61,61,61,61,61,61,61,61,]),'args':([39,],[80,]),'args_list':([39,],[81,]),'empty':([39,],[82,]),'statement':([58,143,171,174,196,199,203,],[99,161,181,184,202,205,206,]),'expression_stmt':([58,143,171,174,196,199,203,],[104,104,104,104,104,104,104,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declaration_list','program',1,'p_program','NIRA_Parser.py',16),
  ('declaration_list -> declaration_list declaration','declaration_list',2,'p_declaration_list','NIRA_Parser.py',20),
  ('declaration_list -> declaration','declaration_list',1,'p_declaration_list','NIRA_Parser.py',21),
  ('declaration -> var_declaration','declaration',1,'p_declaration','NIRA_Parser.py',26),
  ('declaration -> print_stmt','declaration',1,'p_declaration','NIRA_Parser.py',27),
  ('declaration -> read_stmt','declaration',1,'p_declaration','NIRA_Parser.py',28),
  ('declaration -> selection_stmt','declaration',1,'p_declaration','NIRA_Parser.py',29),
  ('declaration -> iteration_stmt','declaration',1,'p_declaration','NIRA_Parser.py',30),
  ('declaration -> expression','declaration',1,'p_declaration','NIRA_Parser.py',31),
  ('print_stmt -> PRINT LPAREN STRING RPAREN SEMI declaration','print_stmt',6,'p_print_stmt','NIRA_Parser.py',36),
  ('print_stmt -> PRINT LPAREN STRING RPAREN SEMI','print_stmt',5,'p_print_stmt','NIRA_Parser.py',37),
  ('print_stmt -> PRINT LPAREN IDENTIFIER RPAREN SEMI declaration','print_stmt',6,'p_print_stmt','NIRA_Parser.py',38),
  ('print_stmt -> PRINT LPAREN IDENTIFIER RPAREN SEMI','print_stmt',5,'p_print_stmt','NIRA_Parser.py',39),
  ('print_stmt -> PRINT LPAREN NUMBER RPAREN SEMI declaration','print_stmt',6,'p_print_stmt','NIRA_Parser.py',40),
  ('print_stmt -> PRINT LPAREN NUMBER RPAREN SEMI','print_stmt',5,'p_print_stmt','NIRA_Parser.py',41),
  ('print_stmt -> PRINT LPAREN boolean RPAREN SEMI declaration','print_stmt',6,'p_print_stmt','NIRA_Parser.py',42),
  ('print_stmt -> PRINT LPAREN boolean RPAREN SEMI','print_stmt',5,'p_print_stmt','NIRA_Parser.py',43),
  ('print_stmt -> PRINT LPAREN expression RPAREN SEMI declaration','print_stmt',6,'p_print_stmt','NIRA_Parser.py',44),
  ('print_stmt -> PRINT LPAREN expression RPAREN SEMI','print_stmt',5,'p_print_stmt','NIRA_Parser.py',45),
  ('print_stmt -> PRINT LPAREN RPAREN SEMI declaration','print_stmt',5,'p_print_stmt','NIRA_Parser.py',46),
  ('print_stmt -> PRINT LPAREN RPAREN SEMI','print_stmt',4,'p_print_stmt','NIRA_Parser.py',47),
  ('var_declaration -> IDENTIFIER var_declaration','var_declaration',2,'p_var_declaration','NIRA_Parser.py',52),
  ('var_declaration -> IDENTIFIER','var_declaration',1,'p_var_declaration','NIRA_Parser.py',53),
  ('var_declaration -> IDENTIFIER ATRIBUTION NUMBER var_declaration','var_declaration',4,'p_var_declaration','NIRA_Parser.py',54),
  ('var_declaration -> IDENTIFIER ATRIBUTION NUMBER SEMI','var_declaration',4,'p_var_declaration','NIRA_Parser.py',55),
  ('var_declaration -> IDENTIFIER ATRIBUTION boolean var_declaration','var_declaration',4,'p_var_declaration','NIRA_Parser.py',56),
  ('var_declaration -> IDENTIFIER ATRIBUTION boolean SEMI','var_declaration',4,'p_var_declaration','NIRA_Parser.py',57),
  ('var_declaration -> IDENTIFIER ATRIBUTION IDENTIFIER var_declaration','var_declaration',4,'p_var_declaration','NIRA_Parser.py',58),
  ('var_declaration -> IDENTIFIER ATRIBUTION IDENTIFIER SEMI','var_declaration',4,'p_var_declaration','NIRA_Parser.py',59),
  ('var_declaration -> IDENTIFIER ATRIBUTION simple_expression SEMI','var_declaration',4,'p_var_declaration','NIRA_Parser.py',60),
  ('statement -> expression_stmt','statement',1,'p_statement','NIRA_Parser.py',65),
  ('statement -> selection_stmt','statement',1,'p_statement','NIRA_Parser.py',66),
  ('statement -> iteration_stmt','statement',1,'p_statement','NIRA_Parser.py',67),
  ('statement -> print_stmt','statement',1,'p_statement','NIRA_Parser.py',68),
  ('statement -> read_stmt','statement',1,'p_statement','NIRA_Parser.py',69),
  ('expression_stmt -> expression','expression_stmt',1,'p_expression_stmt','NIRA_Parser.py',74),
  ('selection_stmt -> IF LPAREN expression RPAREN LBRACE expression RBRACE ELSE LBRACE expression RBRACE statement','selection_stmt',12,'p_selection_stmt_1','NIRA_Parser.py',78),
  ('selection_stmt -> IF LPAREN expression RPAREN LBRACE expression RBRACE statement','selection_stmt',8,'p_selection_stmt_1','NIRA_Parser.py',79),
  ('selection_stmt -> IF LPAREN expression RPAREN LBRACE declaration RBRACE','selection_stmt',7,'p_selection_stmt_1','NIRA_Parser.py',80),
  ('selection_stmt -> IF LPAREN expression RPAREN LBRACE declaration RBRACE ELSE LBRACE declaration RBRACE','selection_stmt',11,'p_selection_stmt_1','NIRA_Parser.py',81),
  ('iteration_stmt -> FOR LPAREN var_declaration expression SEMI additive_expression RPAREN LBRACE expression RBRACE statement','iteration_stmt',11,'p_iteration_stmt_1','NIRA_Parser.py',87),
  ('iteration_stmt -> FOR LPAREN var_declaration expression SEMI additive_expression RPAREN LBRACE print_stmt RBRACE','iteration_stmt',10,'p_iteration_stmt_1','NIRA_Parser.py',88),
  ('iteration_stmt -> WHILE LPAREN expression RPAREN LBRACE expression RBRACE statement','iteration_stmt',8,'p_iteration_stmt_2','NIRA_Parser.py',92),
  ('iteration_stmt -> WHILE LPAREN expression RPAREN LBRACE statement RBRACE','iteration_stmt',7,'p_iteration_stmt_2','NIRA_Parser.py',93),
  ('iteration_stmt -> DO LBRACE statement SEMI RBRACE WHILE LPAREN expression RPAREN SEMI','iteration_stmt',10,'p_iteration_stmt_3','NIRA_Parser.py',98),
  ('iteration_stmt -> DO LBRACE print_stmt RBRACE WHILE LPAREN expression RPAREN SEMI','iteration_stmt',9,'p_iteration_stmt_3','NIRA_Parser.py',99),
  ('iteration_stmt -> DO LBRACE read_stmt RBRACE WHILE LPAREN expression RPAREN SEMI','iteration_stmt',9,'p_iteration_stmt_3','NIRA_Parser.py',100),
  ('iteration_stmt -> DO LBRACE selection_stmt RBRACE WHILE LPAREN expression RPAREN SEMI statement','iteration_stmt',10,'p_iteration_stmt_3','NIRA_Parser.py',101),
  ('iteration_stmt -> DO LBRACE selection_stmt RBRACE WHILE LPAREN expression RPAREN SEMI','iteration_stmt',9,'p_iteration_stmt_3','NIRA_Parser.py',102),
  ('read_stmt -> READ LPAREN STRING RPAREN SEMI declaration','read_stmt',6,'p_read_stmt','NIRA_Parser.py',108),
  ('read_stmt -> READ LPAREN STRING RPAREN SEMI','read_stmt',5,'p_read_stmt','NIRA_Parser.py',109),
  ('read_stmt -> IDENTIFIER ATRIBUTION READ LPAREN STRING RPAREN SEMI','read_stmt',7,'p_read_stmt','NIRA_Parser.py',110),
  ('read_stmt -> IDENTIFIER ATRIBUTION READ LPAREN RPAREN SEMI','read_stmt',6,'p_read_stmt','NIRA_Parser.py',111),
  ('expression -> IDENTIFIER EQUALITY expression','expression',3,'p_expression','NIRA_Parser.py',116),
  ('expression -> simple_expression','expression',1,'p_expression','NIRA_Parser.py',117),
  ('expression -> IDENTIFIER EQUALITY IDENTIFIER','expression',3,'p_expression','NIRA_Parser.py',118),
  ('expression -> expression LOG expression','expression',3,'p_expression','NIRA_Parser.py',119),
  ('expression -> expression OU_LOGICO expression','expression',3,'p_expression','NIRA_Parser.py',120),
  ('simple_expression -> additive_expression relop additive_expression','simple_expression',3,'p_simple_expression','NIRA_Parser.py',126),
  ('simple_expression -> additive_expression','simple_expression',1,'p_simple_expression','NIRA_Parser.py',127),
  ('relop -> MENOR','relop',1,'p_relop','NIRA_Parser.py',132),
  ('relop -> MENOREQUALS','relop',1,'p_relop','NIRA_Parser.py',133),
  ('relop -> MAIOR','relop',1,'p_relop','NIRA_Parser.py',134),
  ('relop -> MAIOREQUALS','relop',1,'p_relop','NIRA_Parser.py',135),
  ('relop -> DIFERENTE','relop',1,'p_relop','NIRA_Parser.py',136),
  ('relop -> EQUALITY','relop',1,'p_relop','NIRA_Parser.py',137),
  ('additive_expression -> additive_expression addop term','additive_expression',3,'p_additive_expression','NIRA_Parser.py',142),
  ('additive_expression -> term','additive_expression',1,'p_additive_expression','NIRA_Parser.py',143),
  ('additive_expression -> term MINUSMINUS','additive_expression',2,'p_additive_expression','NIRA_Parser.py',144),
  ('additive_expression -> term PLUSPLUS','additive_expression',2,'p_additive_expression','NIRA_Parser.py',145),
  ('addop -> PLUS','addop',1,'p_addop','NIRA_Parser.py',150),
  ('addop -> MINUS','addop',1,'p_addop','NIRA_Parser.py',151),
  ('term -> term mulop factor','term',3,'p_term','NIRA_Parser.py',156),
  ('term -> factor','term',1,'p_term','NIRA_Parser.py',157),
  ('mulop -> TIMES','mulop',1,'p_mulop','NIRA_Parser.py',162),
  ('mulop -> DIVIDE','mulop',1,'p_mulop','NIRA_Parser.py',163),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','NIRA_Parser.py',168),
  ('factor -> IDENTIFIER','factor',1,'p_factor','NIRA_Parser.py',169),
  ('factor -> NUMBER','factor',1,'p_factor','NIRA_Parser.py',170),
  ('factor -> boolean','factor',1,'p_factor','NIRA_Parser.py',171),
  ('factor -> IDENTIFIER LPAREN args RPAREN','factor',4,'p_factor','NIRA_Parser.py',172),
  ('boolean -> TRUE','boolean',1,'p_boolean','NIRA_Parser.py',177),
  ('boolean -> FALSE','boolean',1,'p_boolean','NIRA_Parser.py',178),
  ('NUMBER -> INTEGER','NUMBER',1,'p_number','NIRA_Parser.py',184),
  ('NUMBER -> FLOAT','NUMBER',1,'p_number','NIRA_Parser.py',185),
  ('args -> args_list','args',1,'p_args','NIRA_Parser.py',191),
  ('args -> empty','args',1,'p_args','NIRA_Parser.py',192),
  ('args_list -> expression','args_list',1,'p_args_list','NIRA_Parser.py',197),
  ('expression -> expression PLUS term','expression',3,'p_expressions_all','NIRA_Parser.py',201),
  ('expression -> expression MINUS term','expression',3,'p_expressions_all','NIRA_Parser.py',202),
  ('expression -> expression TIMES term','expression',3,'p_expressions_all','NIRA_Parser.py',203),
  ('expression -> expression DIVIDE term','expression',3,'p_expressions_all','NIRA_Parser.py',204),
  ('expression -> expression TIMESX term','expression',3,'p_expressions_all','NIRA_Parser.py',205),
  ('expression -> expression LOG term','expression',3,'p_expressions_all','NIRA_Parser.py',206),
  ('expression -> expression OU_LOGICO term','expression',3,'p_expressions_all','NIRA_Parser.py',207),
  ('empty -> <empty>','empty',0,'p_empty','NIRA_Parser.py',229),
]