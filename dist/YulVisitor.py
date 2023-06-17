# Generated from Yul.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YulParser import YulParser
else:
    from YulParser import YulParser

# This class defines a complete generic visitor for a parse tree produced by YulParser.

class YulVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by YulParser#sourceUnit.
    def visitSourceUnit(self, ctx:YulParser.SourceUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YulParser#object.
    def visitObject(self, ctx:YulParser.ObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YulParser#code.
    def visitCode(self, ctx:YulParser.CodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YulParser#data.
    def visitData(self, ctx:YulParser.DataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YulParser#statement.
    def visitStatement(self, ctx:YulParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YulParser#block.
    def visitBlock(self, ctx:YulParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YulParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:YulParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YulParser#assignment.
    def visitAssignment(self, ctx:YulParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YulParser#expression.
    def visitExpression(self, ctx:YulParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YulParser#ifStatement.
    def visitIfStatement(self, ctx:YulParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YulParser#forStatement.
    def visitForStatement(self, ctx:YulParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YulParser#switchCase.
    def visitSwitchCase(self, ctx:YulParser.SwitchCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YulParser#switchStatement.
    def visitSwitchStatement(self, ctx:YulParser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YulParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:YulParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YulParser#functionCall.
    def visitFunctionCall(self, ctx:YulParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YulParser#boolean.
    def visitBoolean(self, ctx:YulParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YulParser#literal.
    def visitLiteral(self, ctx:YulParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YulParser#typedIdentifierList.
    def visitTypedIdentifierList(self, ctx:YulParser.TypedIdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YulParser#identifierList.
    def visitIdentifierList(self, ctx:YulParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YulParser#typeName.
    def visitTypeName(self, ctx:YulParser.TypeNameContext):
        return self.visitChildren(ctx)



del YulParser