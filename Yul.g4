grammar Yul;

start: object
        | statement;

object: Object StringLiteral LBrace code ( object | data )* RBrace;
code: Code block;
data: Data StringLiteral ( HexStringLiteral | StringLiteral );


statement: block
        | variableDeclaration
        | assignment
        | ifStatement
        | forStatement
        | switchStatement
        | Leave
        | Break
        | Continue
        | functionDefinition
        | expression;

block: LBrace statement* RBrace;

variableDeclaration: (Let variables+=Identifier (Assign expression)?)
                    | (Let variables+=Identifier (Comma variables+=Identifier)* (Assign functionCall)?);

assignment: IdentifierList Assign expression;

expression: functionCall | Identifier | literal;

ifStatement: If cond=expression body=block;

forStatement: For init=block cond=expression post=block body=block;

switchCase: Case literal block;

switchStatement: Switch expression
                (
                    (switchCase+ (Default block)?)
                    | (Default block)
                );

functionDefinition: Function Identifier
                    LParen (arguments+=TypedIdentifierList?) RParen
                    (Arrow returnParameters+=TypedIdentifierList)?
                    body=block;

functionCall: (Identifier | EVMBuiltin) LParen (expression (Comma expression)*)? RParen;

boolean: YulTrue | YulFalse;

literal: (DecimalNumber | StringLiteral | HexNumber | boolean | HexStringLiteral) ( Colon TypeName)?;

TypedIdentifierList: Identifier ( Colon TypeName )? ( Comma Identifier ( Colon TypeName )? )*;
IdentifierList: Identifier ( Comma Identifier )*;

TypeName: Identifier;
Colon: ':';
Object: 'object';
Code: 'code';
Data: 'data';
LBrace: '{';
RBrace: '}';
Let: 'let';
Assign: '=';
Comma: ',';
If: 'if';
For: 'for';
Switch: 'switch';
Case: 'case';
Default: 'default';
Function: 'function';
LParen: '(';
RParen: ')';
Arrow: '->';
Leave: 'leave';
Break: 'break';
Continue: 'continue';
Identifier: [a-zA-Z_][a-zA-Z0-9_]*;
Period: '.';
EVMBuiltin: [a-zA-Z_][a-zA-Z0-9_]*;
YulTrue: 'true';
YulFalse: 'false';
DecimalNumber: [0-9]+;
StringLiteral: '"' ([^"\r\n\\] | '\\' .)* '"';
HexNumber: '0x' [0-9a-fA-F]+;
HexStringLiteral: 'hex"' ~["\r\n]* '"';
WS: [ \t\r\n]+;