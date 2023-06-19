from dist.YulVisitor import YulVisitor
from yul_operators import operators, update_operations, assembly_operations

if __name__ is not None and "." in __name__:
    from dist.YulParser import YulParser
else:
    from dist.YulParser import YulParser


class YulToVyperTranspiler(YulVisitor):

    def __init__(self):
        self.indentation_level = 0
        self.indentation = '    '
        self.output = []
        self.wholeSentence = ""

    def add_line(self, line: str):
        self.output.append(self.indentation * self.indentation_level + line)

    def visitSourceUnit(self, ctx: YulParser.SourceUnitContext):
        self.wholeSentence = ctx.getText()
        return self.visitChildren(ctx)

    def visitObject(self, ctx: YulParser.ObjectContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YulParser#code.
    def visitCode(self, ctx: YulParser.CodeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YulParser#data.
    def visitData(self, ctx: YulParser.DataContext):
        return self.visitChildren(ctx)

    def visitStatement(self, ctx: YulParser.StatementContext):
        return self.visitChildren(ctx)

    def visitBlock(self, ctx: YulParser.BlockContext):
        self.indentation_level += 1
        self.visitChildren(ctx)
        self.indentation_level -= 1

    # Visit a parse tree produced by YulParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx: YulParser.VariableDeclarationContext):
        return self.visitChildren(ctx)

    def visitAssignment(self, ctx: YulParser.AssignmentContext):
        equal = "="
        expression_text = ctx.expression().getText()
        identifier_text = ctx.identifierList().getText()
        expression_parts = expression_text.split("(")
        first_part = expression_parts[0]
        if expression_text[:3] in update_operations.keys():
            operation = expression_text.replace("(", ",").replace(")", "").split(",")
            self.add_line(f"{ctx.identifierList().getText()} {equal} "
                          f"{operation[1]}{update_operations[operation[0]]}{operation[2]}")

        else:
            is_unimplemented_function = (
                    len(expression_parts) > 1 and
                    first_part not in assembly_operations and
                    "function" + first_part not in self.wholeSentence
            )

            if is_unimplemented_function:
                self.add_line(f"#{identifier_text} = {expression_text} function {expression_text} not implemented")
                self.add_line(f"{identifier_text} = \"manuallyAdValue\"")
            else:
                self.add_line(f"{identifier_text} = {expression_text}")

        return self.visitChildren(ctx)

    # Visit a parse tree produced by YulParser#expression.
    def visitExpression(self, ctx: YulParser.ExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YulParser#ifStatement.
    def visitIfStatement(self, ctx: YulParser.IfStatementContext):
        self.add_line(f"if {ctx.expression().getText()}")
        return self.visitBlock(ctx.block())

    # Visit a parse tree produced by YulParser#forStatement.
    def visitForStatement(self, ctx: YulParser.ForStatementContext):
        loop_val = ctx.init.getText().split(":=")[1].replace("}", "")
        loop_bounds = ctx.cond.getText().replace("lt(", "").replace(")", "").split(",")
        condition = ctx.cond.getText().split("(")[0]
        update = ctx.post.getText().split(":=")[1].replace(")}", "").replace("(", ",").split(",")
        loop_range = f"range({loop_val}, {loop_bounds[1]})"
        try:
            update_value = int(update[2])
        except:
            update_value = int(update[1])
        if update[0] == 'add':
            loop_range = f"range({loop_val}, {loop_bounds[1]}, {update_value})"
        elif update[0] == 'sup':
            loop_range = f"range({loop_val}, {loop_bounds[1]}, -{update_value})"
        else:
            self.add_line(f"#That for wont works, it should look like this:")
            self.add_line(f'#for (int {loop_bounds[0]} = {loop_val}; {loop_bounds[0]} {operators[condition]}'
                          f' {loop_bounds[1]}; '
                          f'i = {update[1]} {update_operations[update[0]]} {update[2]})')
        self.add_line(f"for {loop_bounds[0]} in {loop_range}:")
        return self.visit(ctx.body)

    def visitSwitchCase(self, ctx: YulParser.SwitchCaseContext, if_or_elif="if"):
        self.add_line(f"{if_or_elif} {ctx.parentCtx.expression().getText()} == {ctx.literal().getText()}")
        return self.visit(ctx.block())

    # Visit a parse tree produced by YulParser#switchStatement.
    def visitSwitchStatement(self, ctx: YulParser.SwitchStatementContext):
        for i, x in enumerate(ctx.switchCase()):
            if i == 0:
                self.visitSwitchCase(x, "if")
            else:
                self.visitSwitchCase(x, "elif")

        if ctx.Default() is not None:
            self.add_line(f"else")
            return self.visit(ctx.block())

        pass

    # Visit a parse tree produced by YulParser#functionDefinition.
    def visitFunctionDefinition(self, ctx: YulParser.FunctionDefinitionContext):
        func_name = ctx.Identifier()
        self.add_line(f"# function params type can not be correctly inferred, please check manually")

        try:
            returns = ctx.returnParameters[0].getText()
        except:
            returns = ""

        try:
            params = ctx.arguments[0].getText()
        except:
            params = ""

        # delete to skip type of params which can be problematic
        params = params.replace(":u256", "")
        type_arg = "uint256"
        if returns != "":
            returns = returns.replace(":u256", "")
            returns = returns.split(",")
            if len(returns) > 1:
                returns = "(" + ", ".join(returns) + ")"
            else:
                returns = returns[0]

            if params != "":
                params = f"{type_arg}: " + params.replace(",", f", {type_arg}: ")
                self.add_line(f"def {func_name}({params}) -> {returns} #chceck type of returns")
            else:
                self.add_line(f"def {func_name}() -> {returns} #chceck type of returns")
        else:
            params = f"{type_arg}: " + params.replace(",", f", {type_arg}: ")
            self.add_line(f"def {func_name}({params})")
        self.visit(ctx.block())

    def visitFunctionCall(self, ctx: YulParser.FunctionCallContext):
        if ctx.getText()[:3] in update_operations.keys():
            pass
        else:
            expressions = []
            for expression in ctx.expression():
                expressions.append(expression.getText())

            expression = ",".join(expressions)
            if ("function" + ctx.Identifier().getText() not in self.wholeSentence) and ctx.Identifier().getText() != "return":
                self.add_line(f"#{ctx.Identifier().getText()}({expression}) !!function {ctx.Identifier()} not declared!!")
                return self.visitChildren(ctx)
            self.add_line(f"{ctx.Identifier().getText()}({expression})")
            return self.visitChildren(ctx)

    def visitBoolean(self, ctx: YulParser.BooleanContext):
        return self.visitChildren(ctx)

    def visitLiteral(self, ctx: YulParser.LiteralContext):
        return self.visitChildren(ctx)

    def visitTypedIdentifierList(self, ctx: YulParser.TypedIdentifierListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YulParser#identifierList.
    def visitIdentifierList(self, ctx: YulParser.IdentifierListContext):
        return self.visitChildren(ctx)

    def visitTypeName(self, ctx: YulParser.TypeNameContext):
        return self.visitChildren(ctx)

    def get_vyper_code(self) -> str:
        return "\n".join(self.output)
