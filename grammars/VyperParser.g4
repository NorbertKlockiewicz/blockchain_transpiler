// Vyper grammar for Lark

// A module is a sequence of definitions and methods (and comments).
// NOTE: Start symbol for the grammar
// NOTE: Module can start with docstring
parser grammar VyperParser;

options {
    tokenVocab=VyperLexer;
}

module: (string
        | implements
        | comment
        | docstring
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

importname: NAME;
// NOTE: Don't use DOT here, just a separator
import_:
    IMPORT DOT* importpath importalias?
    | importfrom IMPORT ( MUL | importname importalias? )
    | importfrom IMPORT LPAREN importlist RPAREN;
importpath: (importname DOT)* importname;
importalias: AS NAME;
importlist: importname importalias? (COMMA importname importalias? )* COMMA?;
importfrom: FROM (DOT* importpath | DOT+);

implements: IMPLEMENTS COLON NAME;

// Constant definitions
// NOTE: Temporary until decorators used
constantdef: NAME COLON CONSTANT LPAREN type_ RPAREN ASSIGN expr NEWLINE?;

// immutable definitions
// NOTE: Temporary until decorators used
immutabledef: NAME COLON IMMUTABLE LPAREN type_ RPAREN NEWLINE?;

variable: NAME COLON type_;
// NOTE: Temporary until decorators used
variablewithgetter: NAME COLON PUBLIC LPAREN type_ RPAREN;
variabledef: (variable | variablewithgetter) NEWLINE?;

// A decorator 'wraps' a method, modifying it's context.
// NOTE: One or more can be applied (some combos might conflict)
decorator: AT NAME ( LPAREN arguments? RPAREN )? NEWLINE;
decorators: decorator+;

// Functions/Methods take a list of zero or more typed parameters,
// and can return up to one parameter.
// NOTE: Parameters can have a default value,
//       which must be a constant or environment variable.
parameter:  NAME COLON type_ (ASSIGN expr)?;
parameters: INDENT? parameter (COMMA NEWLINE? parameter?)* DEDENT?;

returns_: RETURNTYPE type_;
functionsig: FUNCDECL NAME LPAREN parameters? RPAREN returns_?;
functiondef: decorators? functionsig COLON body;
body: comment? INDENT ( DOCSTRING NEWLINE?)? ( stmt NEWLINE?)+ DEDENT;

// Events can be composed of 0 or more members
eventmember: NAME COLON type_;
indexedeventarg: NAME COLON INDEXED LPAREN type_ RPAREN;
eventbody: INDENT (docstring NEWLINE?)? ((comment | eventmember | indexedeventarg) NEWLINE?)+ DEDENT;
// Events which use no args use a pass statement instead
eventdef: EVENTDECL NAME COLON ( eventbody | PASS );

// Enums
enummember: NAME;
enumbody: INDENT (docstring NEWLINE?)? (comment | enummember NEWLINE?)+ DEDENT;
enumdef: ENUMDECL NAME COLON enumbody;

// Types
arraydef: NAME arraydeftail | arraydef arraydeftail | dynarraydef arraydeftail;
arraydeftail: LSQUARE (DECNUMBER | NAME) RSQUARE;

dynarraydef: DYNARRAY LSQUARE dynarraydefinner COMMA (DECNUMBER | NAME) RSQUARE;
dynarraydefinner: NAME | arraydef | dynarraydef;

tupledef: LPAREN tupledefinner ( COMMA tupledefinner )* COMMA? RPAREN;
tupledefinner: NAME | arraydef | dynarraydef | tupledef;

// NOTE: Map takes a basic type and maps to another type (can be non-basic, including maps)
mapdef: MAP LSQUARE ( NAME | arraydef ) COMMA type_ RSQUARE;
type_: ( NAME | arraydef | tupledef | mapdef | dynarraydef );

// Structs can be composed of 1+ basic types or other customtypes
structmember: NAME COLON type_ ;
structdef: STRUCTDECL NAME COLON INDENT (docstring NEWLINE?)? ((comment | structmember) NEWLINE?)+ DEDENT;

// INterfaces are composed of a series of method definitions, plus their mutability
mutability: NAME;
interfacefunction: functionsig COLON mutability;
interfacedef: INTERFACEDECL NAME COLON INDENT (docstring NEWLINE?)? ((comment | interfacefunction) NEWLINE? )+ DEDENT;


// Statements
// IF and FOR blocks create a new block, and thus are complete when de-indented
// Conversely, the rest of the statements require a newline to be considered complete
// (as they do not create a new block)
stmt: ( ifstmt | forstmt )
     | ( assign
       | augassign
       | declaration
       | returnstmt
       | passstmt
       | breakstmt
       | continuestmt
       | logstmt
       | raisestmt
       | assertstmt
       | expr ) COMMENT?
       | comment;

comment: COMMENT;
docstring: DOCSTRING;

declaration: variable (ASSIGN expr)?;
multipleassign: (variableaccess | SKIPASSIGN) (COMMA (variableaccess | SKIPASSIGN))+;
assign: (variableaccess | multipleassign | LPAREN multipleassign RPAREN ) ASSIGN expr;
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

// NOTE: Post-process into a normal assign
augassign: variableaccess augoperator ASSIGN expr;

passstmt: PASS;
breakstmt: Break;
continuestmt: CONTINUE;

logstmt: LOG NAME LPAREN arguments? RPAREN;
returnstmt: RETURN (expr (COMMA expr)*)?;

raisestmt: RAISE
          | RAISE expr
          | RAISE UNREACHABLE;
assertstmt: ASSERT expr
           | ASSERT expr COMMA expr
           | ASSERT expr COMMA UNREACHABLE;

condexec: expr COLON body;
defaultexec: body;
ifstmt: IF condexec (ELIF condexec)* (ELSE COLON defaultexec)?;
// TODO: make this into a variable definition e.g. `for i: uint256 in range(0, 5): ...`
loopvariable: NAME (COLON NAME)?;
loopiterator: expr;
forstmt: FOR loopvariable IN loopiterator COLON body;

// Expressions
expr: operation
     | dict;

variableaccess: (NAME | LPAREN variableaccess RPAREN) (getattr | getitem | call)*;
getattr: DOT NAME;
getitem: LSQUARE expr RSQUARE;
call: LPAREN (arguments?) RPAREN;

arg: expr;
kwarg: NAME ASSIGN expr;
argument: (arg | kwarg);
arguments: argument (COMMA argument)* (COMMA)?;

tuple: LPAREN COMMA RPAREN | LPAREN expr ( (COMMA expr)+ (COMMA)? | COMMA ) RPAREN;
list: LSQUARE RSQUARE | LSQUARE expr (COMMA expr)* (COMMA)? RSQUARE;
dict: LCURLY RCURLY | LCURLY (NAME COLON expr) (COMMA (NAME COLON expr))* (COMMA)? RCURLY;

// Operators
// This section needs to match Python's operator precedence:
// See https://docs.python.org/3/reference/expressions.html#operator-precedence
// NOTE: The recursive cycle here helps enforce operator precedence
//       Precedence goes up the lower down you go
operation: comment? boolor;

// Boolean Operations
boolor: booland
        | boolor OR  booland;

booland: boolnot
         | booland AND boolnot;

boolnot: comparator
         | NOT boolnot;

comparator: bitwiseor
           | comparator LT bitwiseor
           | comparator GT bitwiseor
           | comparator EQ bitwiseor
           | comparator NE bitwiseor
           | comparator LE bitwiseor
           | comparator GE bitwiseor
           | comparator IN bitwiseor
           | comparator NOT IN bitwiseor;

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

// special rule to handle types as 'arguments' (for `empty` builtin)
empty: EMPTY LPAREN type_ RPAREN;

// special rule to handle types as 'arguments' (for `abidecode` builtin)
abidecode: ABIDECODE LPAREN arg COMMA type_ ( COMMA kwarg )* RPAREN;

specialbuiltins: empty | abidecode;

// NOTE: Must end recursive cycle like this (with `atom` calling `operation`)
atom: variableaccess
     | literal
     | specialbuiltins
     | tuple
     | list
     | LPAREN operation RPAREN;


number: DECNUMBER
       | HEXNUMBER
       | BINNUMBER
       | OCTNUMBER
       | FLOATNUMBER;

literal: ( number | string | BOOL );

string: STRING;