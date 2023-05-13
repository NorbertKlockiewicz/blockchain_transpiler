lexer grammar VyperLexer;

tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from dist.VyperParser import VyperParser
}
@lexer::members {
ignore = False
bracketCount = 0

def openBracket(self):
    self.bracketCount += 1
    VyperLexer.ignore=True

def closeBracket(self):
    self.bracketCount -= 1
    if self.bracketCount == 0:
        VyperLexer.ignore=False

class MyCoolDenter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: VyperLexer = lexer

    def pull_token(self):
        return super(VyperLexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.MyCoolDenter(self, self.NEWLINE, VyperParser.INDENT, VyperParser.DEDENT, False)
    return self.denter.next_token()
}
// Import statements (Supports all styles of Python imports)
AS: 'as';
FROM: 'from';
IMPORT: 'import';

DOT: '.';
COMMA: ',';
COLON: ':';
ASSIGN: '=';
AT: '@';

// Parenthisis
LPAREN: '(' {self.openBracket()};
RPAREN: ')' {self.closeBracket()};
LSQUARE: '[' {self.openBracket()};
RSQUARE: ']' {self.closeBracket()};
LCURLY: '{' {self.openBracket()};
RCURLY: '}' {self.closeBracket()};

CONSTANT: 'constant';
IMMUTABLE: 'immutable';
PUBLIC: 'public';
INDEXED: 'indexed';


// Types
DYNARRAY: 'DynArray';

// Functions
FUNCDECL: 'def';
RETURNTYPE: '->';

// Events can be composed of 0 or more members
EVENTDECL: 'event';

// Enums
ENUMDECL: 'enum';

// NOTE: Map takes a basic type and maps to another type (can be non-basic, including maps)
MAP: 'HashMap';

// Structs can be composed of 1+ basic types or other customtypes
STRUCTDECL: 'struct';


// Interfaces are composed of a series of method definitions, plus their mutability
INTERFACEDECL: 'interface';


// Statements
// If and For blocks create a new block, and thus are complete when de-indented
// Conversely, the rest of the statements require a newline to be considered complete
// (as they do not create a new block)
SKIPASSIGN: '_';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
POW: '**';
SHL: '<<';
SHR: '>>';
PASS: 'pass';
Break: 'break';
CONTINUE: 'continue';
LOG: 'log';
RETURN: 'return';
RAISE: 'raise';
ASSERT: 'assert';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';

UNREACHABLE: 'UNREACHABLE';

FOR: 'for';
IN: 'in';

// Operators
// This section needs to match Python's operator precedence:
// See https://docs.python.org/3/reference/expressions.html#operator-precedence
// NOTE: The recursive cycle here helps enforce operator precedence
//       Precedence goes up the lower down you go
AND: 'and';
OR: 'or';
NOT: 'not';
NEG: '~';

BITAND: '&';
BITOR: '|';
BITXOR: '^';

// Comparisions
EQ: '==';
NE: '!=';
LE: '<=';
GE: '>=';
LT: '<';
GT: '>';

EMPTY: 'empty';
ABIDECODE: 'abidecode';

BOOL: 'True' | 'False';

// Tokens
// Adapted from Lark repo. https://github.com/lark-parser/lark/blob/master/examples/python3.lark
// Adapted from: https://docs.python.org/3/reference/grammar.html
// Adapted by: Erez Shinan
NAME: [a-zA-Z_][a-zA-Z0-9_]*;


TYPE: [a-zA-Z_][a-zA-Z0-9_]*;
STRING: ('b'? '"' (ESC|.)*? '"' | 'b'? '\'' (ESC|.)*? '\'') ;
DOCSTRING: ('"""' (ESC|.)*? '"""' | '\'\'\'' (ESC|.)*? '\'\'\'') ;

fragment ESC: '\\\\' | '\\"' | '\\\'' ;

DECNUMBER: [0-9]+;
HEXNUMBER: '0x' [0-9a-f]*;
OCTNUMBER: '0o' [0-7]*;
BINNUMBER: '0b' [0-1]*;
FLOATNUMBER: [+-]?([0-9]*[.])?[0-9]+;

SPACES: ' '+ -> skip;

NEWLINE
 : ('\r'? '\n' ' '*) {
    if VyperLexer.ignore:
        self.skip()
};

COMMENT
 : '#' ~[\r\n\f]* -> skip;
