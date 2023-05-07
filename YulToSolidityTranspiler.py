from dist.YulVisitor import YulVisitor
from antlr4 import *
if __name__ is not None and "." in __name__:
    from dist.YulParser import YulParser
else:
    from dist.YulParser import YulParser
class YulToSolidityTranspiler(YulVisitor):
    def __init__(self):
        self.indentation_level = 0
        self.indentation = '    '
        self.output = []

    def add_line(self, line: str):
        self.output.append(self.indentation * self.indentation_level + line)

    def visitSourceUnit(self, ctx:YulParser.SourceUnitContext):
        return self.visitChildren(ctx)

    def visitObject(self, ctx:YulParser.ObjectContext):
        self.add_line("contract " + ctx.StringLiteral().getText().replace("\"", ""))
        return self.visitChildren(ctx)

    def visitCode(self, ctx:YulParser.CodeContext):
        return self.visitChildren(ctx)

    def visitData(self, ctx:YulParser.DataContext):
        return self.visitChildren(ctx)

    def visitStatement(self, ctx:YulParser.StatementContext):
        return self.visitChildren(ctx)

    def visitBlock(self, ctx:YulParser.BlockContext):
        self.add_line("{")
        self.indentation_level += 1
        self.visitChildren(ctx)
        self.indentation_level -= 1
        self.add_line("}")

    def visitVariableDeclaration(self, ctx:YulParser.VariableDeclarationContext):
        self.add_line(f"string public {ctx.variables[0].getText()} = {ctx.expression().getText()};")
        return self.visitChildren(ctx)

    def visitAssignment(self, ctx:YulParser.AssignmentContext):
        self.add_line(f"string public {ctx.identifierList().getText()} = {ctx.expression().getText()};")
        return self.visitChildren(ctx)

    def visitExpression(self, ctx:YulParser.ExpressionContext):
        return self.visitChildren(ctx)

    def visitIfStatement(self, ctx:YulParser.IfStatementContext):
        self.add_line(f"if (")
        self.visit(ctx.expression())
        self.add_line(f")")
        return self.visitBlock(ctx.block()),

    def visitForStatement(self, ctx:YulParser.ForStatementContext):
        return self.visitChildren(ctx)

    def visitSwitchCase(self, ctx:YulParser.SwitchCaseContext):
        self.add_line(f"if ({ctx.parentCtx.expression().getText()} == {ctx.literal().getText()})")
        return self.visit(ctx.block())

    def visitSwitchStatement(self, ctx:YulParser.SwitchStatementContext):
        print(ctx.switchCase())
        for x in ctx.switchCase():
            self.visit(x)

        if ctx.Default() is not None:
            self.add_line(f"else")
            return self.visit(ctx.block())

        pass

    def visitFunctionDefinition(self, ctx:YulParser.FunctionDefinitionContext):
        func_name = ctx.Identifier()
        try:
            returns = ctx.returnParameters[0].getText()
        except:
            returns = ""

        try:
            params = ctx.arguments[0].getText()
        except:
            params = ""

        if returns != "":
            self.add_line(f"function {func_name}({params}) public returns ({returns})")
        else:
            self.add_line(f"function {func_name}({params}) public")
        self.visit(ctx.block())

    def visitFunctionCall(self, ctx:YulParser.FunctionCallContext):
        if type(ctx.parentCtx.parentCtx) is not YulParser.SwitchStatementContext:
            expressions = []
            for expression in ctx.expression():
                expressions.append(expression.getText())

            expression = ",".join(expressions)
            self.add_line(f"{ctx.Identifier().getText()}({expression})")
            return self.visitChildren(ctx)

        pass

    def visitBoolean(self, ctx:YulParser.BooleanContext):
        return self.visitChildren(ctx)

    def visitLiteral(self, ctx:YulParser.LiteralContext):
        return self.visitChildren(ctx)

    def visitTypedIdentifierList(self, ctx:YulParser.TypedIdentifierListContext):
        return self.visitChildren(ctx)

    def visitIdentifierList(self, ctx:YulParser.IdentifierListContext):
        return self.visitChildren(ctx)

    def visitTypeName(self, ctx:YulParser.TypeNameContext):
        return self.visitChildren(ctx)

    def get_solidity_code(self) -> str:
        return "\n".join(self.output)