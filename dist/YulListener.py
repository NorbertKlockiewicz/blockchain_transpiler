# Generated from Yul.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YulParser import YulParser
else:
    from YulParser import YulParser

# This class defines a complete listener for a parse tree produced by YulParser.
class YulListener(ParseTreeListener):

    # Enter a parse tree produced by YulParser#sourceUnit.
    def enterSourceUnit(self, ctx:YulParser.SourceUnitContext):
        pass

    # Exit a parse tree produced by YulParser#sourceUnit.
    def exitSourceUnit(self, ctx:YulParser.SourceUnitContext):
        pass


    # Enter a parse tree produced by YulParser#object.
    def enterObject(self, ctx:YulParser.ObjectContext):
        pass

    # Exit a parse tree produced by YulParser#object.
    def exitObject(self, ctx:YulParser.ObjectContext):
        pass


    # Enter a parse tree produced by YulParser#code.
    def enterCode(self, ctx:YulParser.CodeContext):
        pass

    # Exit a parse tree produced by YulParser#code.
    def exitCode(self, ctx:YulParser.CodeContext):
        pass


    # Enter a parse tree produced by YulParser#data.
    def enterData(self, ctx:YulParser.DataContext):
        pass

    # Exit a parse tree produced by YulParser#data.
    def exitData(self, ctx:YulParser.DataContext):
        pass


    # Enter a parse tree produced by YulParser#statement.
    def enterStatement(self, ctx:YulParser.StatementContext):
        pass

    # Exit a parse tree produced by YulParser#statement.
    def exitStatement(self, ctx:YulParser.StatementContext):
        pass


    # Enter a parse tree produced by YulParser#block.
    def enterBlock(self, ctx:YulParser.BlockContext):
        pass

    # Exit a parse tree produced by YulParser#block.
    def exitBlock(self, ctx:YulParser.BlockContext):
        pass


    # Enter a parse tree produced by YulParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:YulParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by YulParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:YulParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by YulParser#assignment.
    def enterAssignment(self, ctx:YulParser.AssignmentContext):
        pass

    # Exit a parse tree produced by YulParser#assignment.
    def exitAssignment(self, ctx:YulParser.AssignmentContext):
        pass


    # Enter a parse tree produced by YulParser#expression.
    def enterExpression(self, ctx:YulParser.ExpressionContext):
        pass

    # Exit a parse tree produced by YulParser#expression.
    def exitExpression(self, ctx:YulParser.ExpressionContext):
        pass


    # Enter a parse tree produced by YulParser#ifStatement.
    def enterIfStatement(self, ctx:YulParser.IfStatementContext):
        pass

    # Exit a parse tree produced by YulParser#ifStatement.
    def exitIfStatement(self, ctx:YulParser.IfStatementContext):
        pass


    # Enter a parse tree produced by YulParser#forStatement.
    def enterForStatement(self, ctx:YulParser.ForStatementContext):
        pass

    # Exit a parse tree produced by YulParser#forStatement.
    def exitForStatement(self, ctx:YulParser.ForStatementContext):
        pass


    # Enter a parse tree produced by YulParser#switchCase.
    def enterSwitchCase(self, ctx:YulParser.SwitchCaseContext):
        pass

    # Exit a parse tree produced by YulParser#switchCase.
    def exitSwitchCase(self, ctx:YulParser.SwitchCaseContext):
        pass


    # Enter a parse tree produced by YulParser#switchStatement.
    def enterSwitchStatement(self, ctx:YulParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by YulParser#switchStatement.
    def exitSwitchStatement(self, ctx:YulParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by YulParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:YulParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by YulParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:YulParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by YulParser#functionCall.
    def enterFunctionCall(self, ctx:YulParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by YulParser#functionCall.
    def exitFunctionCall(self, ctx:YulParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by YulParser#boolean.
    def enterBoolean(self, ctx:YulParser.BooleanContext):
        pass

    # Exit a parse tree produced by YulParser#boolean.
    def exitBoolean(self, ctx:YulParser.BooleanContext):
        pass


    # Enter a parse tree produced by YulParser#literal.
    def enterLiteral(self, ctx:YulParser.LiteralContext):
        pass

    # Exit a parse tree produced by YulParser#literal.
    def exitLiteral(self, ctx:YulParser.LiteralContext):
        pass


    # Enter a parse tree produced by YulParser#typedIdentifierList.
    def enterTypedIdentifierList(self, ctx:YulParser.TypedIdentifierListContext):
        pass

    # Exit a parse tree produced by YulParser#typedIdentifierList.
    def exitTypedIdentifierList(self, ctx:YulParser.TypedIdentifierListContext):
        pass


    # Enter a parse tree produced by YulParser#identifierList.
    def enterIdentifierList(self, ctx:YulParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by YulParser#identifierList.
    def exitIdentifierList(self, ctx:YulParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by YulParser#typeName.
    def enterTypeName(self, ctx:YulParser.TypeNameContext):
        pass

    # Exit a parse tree produced by YulParser#typeName.
    def exitTypeName(self, ctx:YulParser.TypeNameContext):
        pass



del YulParser