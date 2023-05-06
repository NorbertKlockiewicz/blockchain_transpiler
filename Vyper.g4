// Vyper grammar for Lark

// A module is a sequence of definitions and methods (and comments).
// NOTE: Start symbol for the grammar
// NOTE: Module can start with docstring

grammar Vyper;

module: ( DOCSTRING
        | LINE_COMMENT
        | IMPORT
        | struct_def
        | interface_def
        | constant_def
        | variable_def
        | enum_def
        | event_def
        | function_def
        | immutable_def )*EOF;


// Import statements (Supports all styles of Python imports)
AS: 'as';
FROM: 'from';
IMPORT: 'import';
DOT: '.';
WILDCARD: '*';
import_name: NAME;
// NOTE: Don't use DOT here, just a separator
import_path: (import_name '.')* import_name;
import_alias: AS NAME;
import_list: import_name [import_alias] ("," _import_name [import_alias] )* [","]
import_from: FROM (DOT* import_path | DOT+);
IMPORT: IMPORT DOT* import_path [import_alias]
      | import_from IMPORT ( WILDCARD | import_name [import_alias] )
      | import_from IMPORT '(' import_list ')';

// Constant definitions
// NOTE: Temporary until decorators used
constant: 'constant' '(' type ')';
constant_private: NAME ':' constant;
constant_with_getter: NAME ':' 'public' '(' constant ')';
constant_def: (constant_private | constant_with_getter) '=' expr;

// immutable definitions
// NOTE: Temporary until decorators used
immutable: 'immutable' '(' type ')';
immutable_def: NAME ':' immutable;

variable: NAME ':' type;
// NOTE: Temporary until decorators used
variable_with_getter: NAME ':' 'public' '(' (type | immutable) ')';
variable_def: variable | variable_with_getter;

// A decorator 'wraps' a method, modifying it's context.
// NOTE: One or more can be applied (some combos might conflict)
decorator: '@' NAME ('(' arguments? ')')? NEWLINE;

decorators: decorator+;

// Functions/Methods take a list of zero or more typed parameters,
// and can return up to one parameter.
// NOTE: Parameters can have a default value,
//       which must be a constant or environment variable.
parameter: NAME ':' type ['=' _expr];
parameters: parameter (',' parameter?)*;

FUNC_DECL: 'def';
RETURN_TYPE: '->';
RETURNS: RETURN_TYPE type;
function_sig: FUNC_DECL NAME '(' (parameters)? ')' (RETURNS)?;
function_def: (decorators)? function_sig ':' body;


// Events can be composed of 0 or more members
EVENT_DECL: 'event';
event_member: NAME ':' type;
indexed_event_arg: NAME ':' 'indexed' '(' type ')';
event_body: NEWLINE INDENT ((event_member | indexed_event_arg) NEWLINE)+ DEDENT;
// Events which use no args use a pass statement instead
event_def: EVENT_DECL NAME ':' ( event_body | PASS );

// Enums
ENUM_DECL: 'enum';
enum_member: NAME;
enum_body: NEWLINE INDENT (enum_member NEWLINE)+ DEDENT;
enum_def: ENUM_DECL NAME ':' enum_body;

// Types
array_def: (NAME | array_def | dyn_array_def) '[' expr ']';
dyn_array_def: 'DynArray' '[' (NAME | array_def | dyn_array_def) ',' expr ']';
tuple_def: '(' ( NAME | array_def | dyn_array_def | tuple_def ) ( ',' ( NAME | array_def | dyn_array_def | tuple_def ) )* [','] ')';
// NOTE: Map takes a basic type and maps to another type (can be non-basic, including maps)
MAP: 'HashMap';
map_def: MAP '[' ( NAME | array_def ) ',' type ']';
type: ( NAME | array_def | tuple_def | map_def | dyn_array_def );

// Structs can be composed of 1+ basic types or other custom_types
STRUCT_DECL: 'struct';
struct_member: NAME ':' type;
struct_def: STRUCT_DECL NAME ':' NEWLINE INDENT (struct_member NEWLINE)+ DEDENT;

// Interfaces are composed of a series of method definitions, plus their mutability
INTERFACE_DECL: 'interface';
mutability: NAME;
interface_function: function_sig ':' mutability;
interface_def: INTERFACE_DECL NAME ':' NEWLINE INDENT ( interface_function NEWLINE)+ _DEDENT;
IMPLEMENTS_DECL: 'implements';
implements_def: IMPLEMENTS_DECL ':' NAME;


// Statements
// If and For blocks create a new block, and thus are complete when de-indented
// Conversely, the rest of the statements require a newline to be considered complete
// (as they do not create a new block)
stmt: ( if_stmt | for_stmt ) COMMENT?
     | (declaration
       | assign
       | aug_assign
       | return_stmt
       | pass_stmt
       | break_stmt
       | continue_stmt
       | log_stmt
       | raise_stmt
       | assert_stmt
       | expr ) COMMENT?;

declaration: variable ['=' _expr];
skip_assign: '_';
multiple_assign: (variable_access | skip_assign) (',' (variable_access | skip_assign))+;
assign: (variable_access | multiple_assign | '(' multiple_assign ')' ) '=' expr;
// NOTE: Keep these in sync with bin_op below
aug_operator: '+'  -> add
             | '-'  -> sub
             | '*'  -> mul
             | '/'  -> div
             | '%'  -> mod
             | '**' -> pow
             | '<<' -> shl
             | '>>' -> shr
             | _BITAND -> bitand
             | _BITOR -> bitor
             | _BITXOR -> bitxor
             | _AND -> and
             | _OR  -> or;
// NOTE: Post-process into a normal assign
aug_assign: variable_access aug_operator '=' expr;

PASS: 'pass';
BREAK: 'break';
CONTINUE: 'continue';
LOG: 'log';
RETURN: 'return';
RAISE: 'raise';
ASSERT: 'assert';

pass_stmt: PASS;
break_stmt: BREAK;
continue_stmt: CONTINUE;

log_stmt: LOG NAME '(' [arguments] ')';
return_stmt: RETURN [expr (',' _expr)*];
UNREACHABLE: 'UNREACHABLE';
raise_stmt: RAISE -> raise
          | RAISE expr -> raise_with_reason
          | RAISE UNREACHABLE -> raise_unreachable;
assert_stmt: ASSERT expr -> assert
           | ASSERT expr ',' expr -> assert_with_reason
           | ASSERT expr ',' UNREACHABLE -> assert_unreachable;

body: NEWLINE INDENT ([COMMENT] _NEWLINE | stmt)+ _DEDENT;
cond_exec: expr ':' body;
default_exec: body;
if_stmt: 'if' cond_exec ('elif' cond_exec)* ['else' ':' default_exec];
// TODO: make this into a variable definition e.g. `for i: uint256 in range(0, 5): ...`
loop_variable: NAME [':' NAME];
loop_iterator: expr;
for_stmt: 'for' loop_variable 'in' loop_iterator ':' body;


// Expressions
expr: operation
     | dict;

get_item: variable_access '[' expr ']';
get_attr: variable_access '.' NAME;
call: variable_access '(' [arguments] ')'
?variable_access: NAME -> get_var
                | get_item
                | get_attr
                | call
                | '(' variable_access ')';

arg: expr;
kwarg: NAME '=' expr;
argument: (arg | kwarg);
arguments: argument (',' argument)* [','];

tuple: '(' ',' ')' | '(' expr ( (',' expr)+ [','] | ',' ) ')';
list: '[' ']' | '[' expr (',' expr)* [','] ']';
dict: '{' '}' | '{' (NAME ':' expr) (',' (NAME ':' expr))* [','] '}';


// Operators
// This section needs to match Python's operator precedence:
// See https://docs.python.org/3/reference/expressions.html#operator-precedence
// NOTE: The recursive cycle here helps enforce operator precedence
//       Precedence goes up the lower down you go
operation: bool_or;

AND: 'and';
OR: 'or';
NOT: 'not';

// Boolean Operations
bool_or: bool_and
        | bool_or _OR  bool_and -> or;

bool_and: bool_not
         | bool_and _AND bool_not -> and;

bool_not: comparator
         | _NOT bool_not -> not;

POW: '**';
SHL: '<<';
SHR: '>>';
BITAND: '&';
BITOR: '|';
BITXOR: '^';

// Comparisions
EQ: '==';
NE: '!=';
LE: '<=';
GE: '>=';
IN: 'in';
comparator: bitwise_or
           | comparator '<' bitwise_or ->  lt
           | comparator '>' bitwise_or ->  gt
           | comparator EQ bitwise_or ->  eq
           | comparator NE bitwise_or ->  ne
           | comparator LE bitwise_or ->  le
           | comparator GE bitwise_or ->  ge
           | comparator IN bitwise_or ->  in
           | comparator NOT IN bitwise_or ->  in;

// Binary Operations
// NOTE: Keep these in sync with aug_assign above
bitwise_or : bitwise_xor
            | bitwise_or BITOR  bitwise_xor -> bitor;
bitwise_xor: bitwise_and
            | bitwise_xor BITXOR  bitwise_and -> bitxor;
bitwise_and: shift
            | bitwise_and BITAND  shift -> bitand;
shift: summation
      | shift SHL  summation -> shl
      | shift SHR  summation -> shr;
summation: product
          | summation '+'  product -> add
          | summation '-'  product -> sub;
product: unary
        | product '*'  unary -> mul
        | product '/'  unary -> div
        | product '%'  unary -> mod;
unary: power
       | '+'  power -> uadd
       | '-'  power -> usub
       | '~'  power -> invert;
power: atom
      | power POW  atom -> pow;

// special rule to handle types as 'arguments' (for `empty` builtin)
empty: 'empty' '(' type ')';

// special rule to handle types as 'arguments' (for `_abi_decode` builtin)
abi_decode: '_abi_decode' '(' arg ',' type ( ',' kwarg )* ')';

special_builtins: empty | abi_decode;

// NOTE: Must end recursive cycle like this (with `atom` calling `operation`)
atom: variable_access
     | literal
     | special_builtins
     | tuple
     | list
     | '(' operation ')';

// Tokens
// Adapted from Lark repo. https://github.com/lark-parser/lark/blob/master/examples/python3.lark
// Adapted from: https://docs.python.org/3/reference/grammar.html
// Adapted by: Erez Shinan
NAME: /[a-zA-Z_]\w*/;
LINE_COMMENT: /#[^\n]*/;
NEWLINE: ( /\r?\n[\t ]*/ | LINE_COMMENT )+;


STRING: /b?('(?!'').*?(?<!\\)(\\\\)*?'|'(?!'').*?(?<!\\)(\\\\)*?')/i;
DOCSTRING: /('''.*?(?<!\\)(\\\\)*?'''|'''.*?(?<!\\)(\\\\)*?''')/is;

DEC_NUMBER: /0|[1-9]\d*/i;
HEX_NUMBER.2: /0x[\da-f]*/i;
OCT_NUMBER.2: /0o[0-7]*/i;
BIN_NUMBER.2 : /0b[0-1]*/i;
FLOAT_NUMBER.2: /((\d+\.\d*|\.\d+)(e[-+]?\d+)?|\d+(e[-+]?\d+))/i;

number: DEC_NUMBER
       | HEX_NUMBER
       | BIN_NUMBER
       | OCT_NUMBER
       | FLOAT_NUMBER;

BOOL: 'True' | 'False';

// TODO: Remove Docstring from here, and add to first part of body
literal: ( number | STRING | DOCSTRING | BOOL );

WS: [\t \f]+ -> skip;  // WS
Line_CONT: ~[/\\[\t \f]*\r?\n/];   // LINE_CONT
ignore COMMENT;
declare INDENT DEDENT;