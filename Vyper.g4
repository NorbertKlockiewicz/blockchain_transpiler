// Vyper grammar for Lark

// A module is a sequence of definitions and methods (and comments).
// NOTE: Start symbol for the grammar
// NOTE: Module can start with docstring
grammar Vyper;

tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from dist.VyperParser import VyperParser
}
@lexer::members {
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

module: (STRING
        | COMMENT
        | import_
        | structdef
        | interfacedef
        | constantdef
        | variabledef
        | enumdef
        | eventdef
        | functiondef
        | immutabledef
        | NEWLINE)* EOF;

// Import statements (Supports all styles of Python imports)
AS: 'as';
FROM: 'from';
IMPORT: 'import';
DOT: '.';
COMMA: ',';
WILDCARD: '*';
LParen: '(';
RParen: ')';
COLON: ':';
CONSTANT: 'constant';
EQUALITY: '=';
IMMUTABLE: 'immutable';
PUBLIC: 'public';
AT: '@';
INDEXED: 'indexed';
RSquare: '[';
LSquare: ']';
DynArray: 'DynArray';

importname: NAME;
// NOTE: Don't use DOT here, just a separator
importpath: (importname DOT)* importname;
importalias: AS NAME;
importlist: importname importalias? (COMMA importname importalias? )* COMMA?;
importfrom: FROM (DOT* importpath | DOT+);
import_: IMPORT DOT* importpath importalias?
      | importfrom IMPORT ( WILDCARD | importname importalias? )
      | importfrom IMPORT LParen importlist RParen;


// Constant definitions
// NOTE: Temporary until decorators used
constantdef: NAME COLON CONSTANT LParen type_ RParen EQUALITY expr NEWLINE?;

// immutable definitions
// NOTE: Temporary until decorators used
immutabledef: NAME COLON IMMUTABLE LParen type_ RParen NEWLINE?;

variable: NAME COLON type_;
// NOTE: Temporary until decorators used
variablewithgetter: NAME COLON PUBLIC LParen type_ RParen;
variabledef: (variable | variablewithgetter) NEWLINE?;

// A decorator 'wraps' a method, modifying it's context.
// NOTE: One or more can be applied (some combos might conflict)
decorator: AT NAME ( LParen arguments? RParen )? NEWLINE;
decorators: decorator+;

// Functions/Methods take a list of zero or more typed parameters,
// and can return up to one parameter.
// NOTE: Parameters can have a default value,
//       which must be a constant or environment variable.
parameter:  NAME SPACES? COLON SPACES? type_ SPACES? (EQUALITY expr)?;
parameters: INDENT? parameter (COMMA NEWLINE? parameter?)* DEDENT?;

FUNCDECL: 'def';
RETURNTYPE: '->';
returns_: RETURNTYPE type_;
functionsig: FUNCDECL NAME LParen parameters? RParen returns_?;
functiondef: decorators? functionsig COLON body;

// Events can be composed of 0 or more members
EVENTDECL: 'event';
eventmember: NAME COLON type_;
indexedeventarg: NAME COLON INDEXED LParen type_ RParen;
eventbody: INDENT ((variable | indexedeventarg) NEWLINE?)+ DEDENT;
// Events which use no args use a pass statement instead
eventdef: EVENTDECL NAME COLON ( eventbody | PASS );

// Enums
ENUMDECL: 'enum';
enummember: NAME;
enumbody: NEWLINE INDENT (enummember NEWLINE?)+ DEDENT;
enumdef: ENUMDECL NAME COLON enumbody;

// Types
arraydef: simple_arraydef | dynarraydef;
simple_arraydef: NAME index*;
dynarraydef: DynArray dynindex+;
index: RSquare (DECNUMBER | NAME) LSquare;
dynindex: RSquare (NAME | simple_arraydef | dynarraydef) COMMA (DECNUMBER | NAME) LSquare;

tupledef: LParen ( NAME | arraydef | dynarraydef | tupledef ) ( COMMA ( NAME | arraydef | dynarraydef | tupledef ) )* COMMA? RParen;
// NOTE: Map takes a basic type and maps to another type (can be non-basic, including maps)
MAP: 'HashMap';
mapdef: MAP RSquare ( NAME | arraydef ) COMMA type_ LSquare;
type_: ( NAME | arraydef | tupledef | mapdef | dynarraydef );

// Structs can be composed of 1+ basic types or other customtypes
STRUCTDECL: 'struct';
structmember: NAME COLON type_;
structdef: STRUCTDECL NAME COLON INDENT (structmember NEWLINE?)+ DEDENT;

// Interfaces are composed of a series of method definitions, plus their mutability
INTERFACEDECL: 'interface';
mutability: NAME;
interfacefunction: functionsig COLON mutability;
interfacedef: INTERFACEDECL NAME COLON INDENT ( interfacefunction NEWLINE? )+ DEDENT;


// Statements
// If and For blocks create a new block, and thus are complete when de-indented
// Conversely, the rest of the statements require a newline to be considered complete
// (as they do not create a new block)
stmt: ( ifstmt | forstmt ) COMMENT?
     | (declaration
       | assign
       | augassign
       | returnstmt
       | passstmt
       | breakstmt
       | continuestmt
       | logstmt
       | raisestmt
       | assertstmt
       | expr ) COMMENT?;

declaration: variable (EQUALITY expr)?;
SkipAssign: '_';
multipleassign: (variableaccess | SkipAssign) (COMMA (variableaccess | SkipAssign))+;
assign: (variableaccess | multipleassign | LParen multipleassign RParen ) EQUALITY expr;
// NOTE: Keep these in sync with binop below
augoperator: ADD
             | SUB
             | MUL
             | DIV
             | MOD
             | POW
             | SHL
             | SHR
             | BITAND
             | BITOR
             | BITXOR
             | AND
             | OR;

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
POW: '**';
SHL: '<<';
SHR: '>>';

// NOTE: Post-process into a normal assign
augassign: variableaccess augoperator EQUALITY expr;

PASS: 'pass';
Break: 'break';
CONTINUE: 'continue';
LOG: 'log';
RETURN: 'return';
RAISE: 'raise';
ASSERT: 'assert';
If: 'if';
Else: 'else';
Elif: 'elif';


passstmt: PASS;
breakstmt: Break;
continuestmt: CONTINUE;

logstmt: LOG NAME LParen arguments? RParen;
returnstmt: RETURN (expr (COMMA expr)*)?;
UNREACHABLE: 'UNREACHABLE';

raisestmt: RAISE
          | RAISE expr
          | RAISE UNREACHABLE;
assertstmt: ASSERT expr
           | ASSERT expr COMMA expr
           | ASSERT expr COMMA UNREACHABLE;

body: INDENT (COMMENT | stmt NEWLINE?)+ DEDENT;
condexec: expr COLON body;
defaultexec: body;
ifstmt: If condexec (Elif condexec)* (Else COLON defaultexec)?;
// TODO: make this into a variable definition e.g. `for i: uint256 in range(0, 5): ...`
loopvariable: NAME (COLON NAME)?;
loopiterator: expr;
forstmt: For loopvariable In loopiterator COLON body;

For: 'for';
In: 'in';

// Expressions
expr: operation
     | dict;

variableaccess: (NAME | LParen variableaccess RParen) (getattr | getitem | call)*;
getattr: DOT NAME;
getitem: RSquare expr LSquare;
call: LParen (arguments?) RParen;

arg: expr;
kwarg: NAME EQUALITY expr;
argument: (arg | kwarg);
arguments: argument (COMMA argument)* (COMMA)?;

tuple: LParen COMMA RParen | LParen expr ( (COMMA expr)+ (COMMA)? | COMMA ) RParen;
list: RSquare LSquare | RSquare expr (COMMA expr)* (COMMA)? LSquare;
dict: LCurly RCurly | LCurly (NAME COLON expr) (COMMA (NAME COLON expr))* (COMMA)? RCurly;

LCurly: '{';
RCurly: '}';


// Operators
// This section needs to match Python's operator precedence:
// See https://docs.python.org/3/reference/expressions.html#operator-precedence
// NOTE: The recursive cycle here helps enforce operator precedence
//       Precedence goes up the lower down you go
operation: boolor;

AND: 'and';
OR: 'or';
NOT: 'not';
NEG: '~';

// Boolean Operations
boolor: booland
        | boolor OR  booland;

booland: boolnot
         | booland AND boolnot;

boolnot: comparator
         | NOT boolnot;

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

comparator: bitwiseor
           | comparator LT bitwiseor
           | comparator GT bitwiseor
           | comparator EQ bitwiseor
           | comparator NE bitwiseor
           | comparator LE bitwiseor
           | comparator GE bitwiseor
           | comparator In bitwiseor
           | comparator NOT In bitwiseor;

// Binary Operations
// NOTE: Keep these in sync with augassign above
bitwiseor : bitwisexor
            | bitwiseor BITOR  bitwisexor;
bitwisexor: bitwiseand
            | bitwisexor BITXOR  bitwiseand;
bitwiseand: shift
            | bitwiseand BITAND  shift;
shift: summation
      | shift SHL  summation
      | shift SHR  summation;
summation: product
          | summation ADD  product
          | summation SUB  product;
product: unary
        | product MUL  unary
        | product DIV  unary
        | product MOD  unary;
unary: power
       | ADD  power
       | SUB  power
       | NEG  power ;
power: atom
      | power POW  atom;

Empty: 'empty';
AbiDecode: 'abidecode';

// special rule to handle types as 'arguments' (for `empty` builtin)
empty: Empty LParen type_ RParen;

// special rule to handle types as 'arguments' (for `abidecode` builtin)
abidecode: AbiDecode LParen arg COMMA type_ ( COMMA kwarg )* RParen;

specialbuiltins: empty | abidecode;

// NOTE: Must end recursive cycle like this (with `atom` calling `operation`)
atom: variableaccess
     | literal
     | specialbuiltins
     | tuple
     | list
     | LParen operation RParen;

// Tokens
// Adapted from Lark repo. https://github.com/lark-parser/lark/blob/master/examples/python3.lark
// Adapted from: https://docs.python.org/3/reference/grammar.html
// Adapted by: Erez Shinan
NAME: [a-zA-Z0-9_]+;


TYPE: [a-zA-Z_][a-zA-Z0-9_]*;
STRING: ( [rR] | [uU] | [fF] | ( [fF] [rR] ) | ( [rR] [fF] ) )? ( SHORT_STRING | LONG_STRING );

/// shortstring     ::=  "'" shortstringitem* "'" | '"' shortstringitem* '"'
/// shortstringitem ::=  shortstringchar | stringescapeseq
/// shortstringchar ::=  <any source character except "\" or newline or the quote>
fragment SHORT_STRING
 : '\'' ( STRING_ESCAPE_SEQ | ~[\\\r\n\f'] )* '\''
 | '"' ( STRING_ESCAPE_SEQ | ~[\\\r\n\f"] )* '"'
 ;
/// longstring      ::=  "'''" longstringitem* "'''" | '"""' longstringitem* '"""'
fragment LONG_STRING
 : '\'\'\'' LONG_STRING_ITEM*? '\'\'\''
 | '"""' LONG_STRING_ITEM*? '"""'
 ;

/// longstringitem  ::=  longstringchar | stringescapeseq
fragment LONG_STRING_ITEM
 : LONG_STRING_CHAR
 | STRING_ESCAPE_SEQ
 ;

/// longstringchar  ::=  <any source character except "\">
fragment LONG_STRING_CHAR
 : ~'\\'
 ;

/// stringescapeseq ::=  "\" <any source character>
fragment STRING_ESCAPE_SEQ
 : '\\' .
 | '\\' NEWLINE
 ;


DECNUMBER: [0-9]+;
HEXNUMBER: '0x' [0-9a-f]*;
OCTNUMBER: '0o' [0-7]*;
BINNUMBER: '0b' [0-1]*;
FLOATNUMBER: [+-]?([0-9]*[.])?[0-9]+;

number: DECNUMBER
       | HEXNUMBER
       | BINNUMBER
       | OCTNUMBER
       | FLOATNUMBER;

BOOL: 'True' | 'False';

// TODO: Remove Docstring from here, and ADD to first part of body
literal: ( number | STRING | BOOL );

SPACES: [\t \f]+ -> skip;

NEWLINE
 : ('\r'? '\n' ' '*);

COMMENT
 : '#' ~[\r\n\f]* -> skip;