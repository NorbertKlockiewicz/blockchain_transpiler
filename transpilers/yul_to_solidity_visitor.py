from .dist.YulParser import YulParser
from .dist.YulVisitor import YulVisitor
from .yul_operators import operators, update_operations, assembly_operations

import re


def extract_function_names(string):
    pattern = r'\b\w+\('

    matches = re.findall(pattern, string)

    function_names = [match.rstrip('(') for match in matches]

    return function_names


class YulToSolidityVisitor(YulVisitor):
    def __init__(self):
        self.indentation_level = 0
        self.indentation = '    '
        self.output = []
        self.is_assembly = False
        self.was_assembly = False
        self.is_runtime = False
        self.wholeSentence = ""

    def add_line(self, line: str):
        self.output.append(self.indentation * self.indentation_level + line)

    def visitSourceUnit(self, ctx: YulParser.SourceUnitContext):
        self.add_line("pragma solidity >=0.4.22 <0.9.0;\n\n")
        self.wholeSentence = ctx.getText()
        return self.visitChildren(ctx)

    def visitObject(self, ctx: YulParser.ObjectContext):
        if ctx.StringLiteral().getText() == '"runtime"':
            self.add_line("function " + ctx.StringLiteral().getText().replace("\"", "") + "() public")
            self.is_runtime = True

        else:
            self.add_line("contract " + ctx.StringLiteral().getText().replace("\"", ""))
            self.add_line("{")
            self.indentation_level += 1

            is_object = lambda x: type(x) == YulParser.ObjectContext
            is_not_object = lambda x: not type(x) == YulParser.ObjectContext
            children = list(ctx.getChildren(is_not_object))

            for child in children:
                self.visit(child)

            self.indentation_level -= 1
            self.add_line("}")
            children = list(ctx.getChildren(is_object))

            for child in children:
                self.visit(child)

            return

        return self.visitChildren(ctx)

    def visitCode(self, ctx: YulParser.CodeContext):
        if not ctx.parentCtx.getText().startswith("object\"runtime\""):
            self.add_line(" constructor() public")

        return self.visitChildren(ctx)

    def visitData(self, ctx: YulParser.DataContext):
        return self.visitChildren(ctx)

    def visitStatement(self, ctx: YulParser.StatementContext):
        if type(ctx.children[0]) == YulParser.IfStatementContext:
            operation = extract_function_names(ctx.getText())
        elif type(ctx.children[0]) == YulParser.ForStatementContext:
            operation = ""
            # It's because for statement is changed for solidity
        elif type(ctx.children[0]) == YulParser.FunctionDefinitionContext:
            # It cant be that in function definition is function in assembly
            operation = ""
        elif type(ctx.children[0]) == YulParser.ExpressionContext:
            operation = extract_function_names(ctx.getText())
        elif type(ctx.children[0]) == YulParser.SwitchStatementContext:
            # operation = extract_function_names(ctx.switchStatement().expression().getText())
            operation = ""
        else:
            operation = ctx.getText().split("(")[0].split(":=")
            if len(operation) > 1:
                operation = extract_function_names(ctx.getText().split(":=")[1])
            else:
                operation = operation[0]

        if not any(function_name in list(set(assembly_operations)) for function_name in operation):
            return self.visitChildren(ctx)

        elif type(ctx.children[0]) != YulParser.FunctionDefinitionContext and \
                type(ctx.children[0]) != YulParser.ForStatementContext and not self.was_assembly:
            self.add_line(f"assembly {{")
            self.indentation_level += 1
            self.is_assembly = True
            self.visitChildren(ctx)
            self.is_assembly = False
            self.was_assembly = False
            self.indentation_level -= 1
            self.add_line("}")
            return

        return self.visitChildren(ctx)

    def visitBlock(self, ctx: YulParser.BlockContext):

        if ctx.parentCtx.parentCtx.getText().startswith("object\"runtime\""):
            is_function = lambda x: isinstance(x, YulParser.StatementContext) and x.functionDefinition() is not None
            is_not_function = lambda x: isinstance(x, YulParser.StatementContext) and x.functionDefinition() is None
            children = list(ctx.getChildren(is_not_function))
            self.add_line("{")
            self.indentation_level += 1

            for child in children:
                self.visit(child)

            self.indentation_level -= 1
            self.add_line("}")
            children = list(ctx.getChildren(is_function))

            for child in children:
                self.visit(child)
        elif ctx.parentCtx.parentCtx.getText().startswith("object"):
            is_function = lambda x: isinstance(x, YulParser.StatementContext) and x.functionDefinition() is not None
            is_not_function = lambda x: isinstance(x, YulParser.StatementContext) and x.functionDefinition() is None
            children = list(ctx.getChildren(is_not_function))
            self.add_line("{")
            self.indentation_level += 1

            for child in children:
                self.visit(child)

            self.indentation_level -= 1
            self.add_line("}")
            children = list(ctx.getChildren(is_function))

            for child in children:
                self.visit(child)
        else:
            self.add_line("{")
            self.indentation_level += 1
            self.visitChildren(ctx)
            self.indentation_level -= 1
            self.add_line("}")

    def visitVariableDeclaration(self, ctx: YulParser.VariableDeclarationContext):
        if self.is_assembly:
            equal = ":="
            semicolon = ""
        else:
            equal = "="
            semicolon = ";"
        if self.is_assembly:
            self.add_line(f"{ctx.expression().getText()}")
        elif ctx.expression().getText()[:3] in update_operations.keys():
            operation = ctx.expression().getText().replace("(", ",").replace(")", "").split(",")
            self.add_line(f"int public {ctx.variables[0].getText()} {equal} "
                          f"{operation[1]}{update_operations[operation[0]]}{operation[2]}{semicolon}")
        else:
            if len(ctx.expression().getText().split("(")) > 1:
                if ctx.expression().getText().split("(")[0] not in assembly_operations and \
                        "function" + ctx.expression().getText().split("(")[0] not in self.wholeSentence:
                    self.add_line(f"//uint256 {ctx.variables[0].getText()} {equal} "
                                  f"{ctx.expression().getText()}{semicolon}: "
                                  f"function {ctx.expression().getText()} not implemented")
                    self.add_line(f"uint256 {ctx.variables[0].getText()} {equal} \"ManuallyAddValue\"{semicolon}")
                else:
                    self.add_line(f"uint256 {ctx.variables[0].getText()} {equal} "
                                  f"{ctx.expression().getText()}{semicolon}")
            else:
                self.add_line(f"uint256 {ctx.variables[0].getText()} {equal} {ctx.expression().getText()}{semicolon}")
        return self.visitChildren(ctx)

    def visitAssignment(self, ctx: YulParser.AssignmentContext):
        equal = "="
        semicolon = ";"
        if self.is_assembly:
            self.add_line(f"{ctx.getText()}")

        elif ctx.expression().getText()[:3] in update_operations.keys():
            operation = ctx.expression().getText().replace("(", ",").replace(")", "").split(",")
            self.add_line(f"{ctx.identifierList().getText()} {equal} "
                          f"{operation[1]}{update_operations[operation[0]]}{operation[2]}{semicolon}")

        else:
            if len(ctx.expression().getText().split("(")) > 1:
                if ctx.expression().getText().split("(")[0] not in assembly_operations and \
                        "function" + ctx.expression().getText().split("(")[0] not in self.wholeSentence:
                    self.add_line(f"//{ctx.identifierList().getText()} {equal} {ctx.expression().getText()}{semicolon} "
                                  f"function {ctx.expression().getText()} not implemented")
                    self.add_line(f"{ctx.identifierList().getText()} {equal} \"manuallyAdValue\"{semicolon}")
                else:
                    self.add_line(f"{ctx.identifierList().getText()} {equal} {ctx.expression().getText()}{semicolon}")
            else:
                self.add_line(f"{ctx.identifierList().getText()} {equal} {ctx.expression().getText()}{semicolon}")
        return self.visitChildren(ctx)

    def visitExpression(self, ctx: YulParser.ExpressionContext):
        if type(ctx.parentCtx) == YulParser.AssignmentContext and \
                type(ctx.children[0]) == YulParser.FunctionCallContext \
                or (type(ctx.parentCtx) == YulParser.VariableDeclarationContext and
                    type(ctx.children[0]) == YulParser.FunctionCallContext):
            return
        return self.visitChildren(ctx)

    def visitIfStatement(self, ctx: YulParser.IfStatementContext):
        if self.is_assembly:
            self.was_assembly = True
            self.add_line(f"if {ctx.expression().getText()}")

        else:
            self.add_line(f"if ({ctx.expression().getText()})")
        return self.visitBlock(ctx.block())

    def visitForStatement(self, ctx: YulParser.ForStatementContext):
        loop_val = ctx.init.getText().split(":=")[1].replace("}", "")
        loop_bounds = ctx.cond.getText().replace(")", "").split("(")[1].split(",")
        condition = ctx.cond.getText().split("(")[0]
        update = ctx.post.getText().split(":=")[1].replace(")}", "").replace("(", ",").split(",")

        self.add_line(f'for (int {loop_bounds[0]} = {loop_val}; {loop_bounds[0]} {operators[condition]}'
                      f' {loop_bounds[1]}; '
                      f'i = {update[1]} {update_operations[update[0]]} {update[2]})')
        return self.visit(ctx.body)

    def visitSwitchCase(self, ctx: YulParser.SwitchCaseContext, if_or_elif="if"):
        self.add_line(f"{if_or_elif} ({ctx.parentCtx.expression().getText()} == {ctx.literal().getText()})")
        return self.visit(ctx.block())

    def visitSwitchStatement(self, ctx: YulParser.SwitchStatementContext):
        for i, x in enumerate(ctx.switchCase()):
            if i == 0:
                self.visitSwitchCase(x, "if")
            else:
                self.visitSwitchCase(x, "else if")

        if ctx.Default() is not None:
            self.add_line(f"else")
            return self.visit(ctx.block())

        pass

    def visitFunctionDefinition(self, ctx: YulParser.FunctionDefinitionContext):
        func_name = ctx.Identifier()
        self.add_line(f"// function params type can not be correctly inferred, please check manually")

        try:
            returns = ctx.returnParameters[0].getText()
        except:
            returns = ""

        try:
            params = ctx.arguments[0].getText()
        except:
            params = ""

        params = params.replace(":u256", "")
        type_arg = "uint256"
        if returns != "":
            returns = returns.replace(":u256", "")
            returns = returns.split(",")
            if len(returns) > 1:
                returns = "uint256 " + ",uint256 ".join(returns)
            else:
                returns = "uint256 " + returns[0]

            if params != "":
                params = f"{type_arg} " + params.replace(",", f", {type_arg} ")
                self.add_line(f"function {func_name}({params}) public returns ({returns})")
            else:
                self.add_line(f"function {func_name}() public returns ({returns})")
        else:
            params = f"{type_arg} " + params.replace(",", f", {type_arg} ")
            self.add_line(f"function {func_name}({params}) public")
        self.visit(ctx.block())

    def visitFunctionCall(self, ctx: YulParser.FunctionCallContext):
        if ctx.getText()[:3] in update_operations.keys() or (
                ctx.Identifier().getText() in assembly_operations and self.is_assembly
                and type(ctx.parentCtx.parentCtx) is not YulParser.StatementContext) \
                or ("function" + ctx.Identifier().getText() in self.wholeSentence
                    and type(ctx.parentCtx.parentCtx) is not YulParser.StatementContext):
            pass
        else:
            expressions = []
            for expression in ctx.expression():
                expressions.append(expression.getText())

            expression = ",".join(expressions)
            if ("function" + ctx.Identifier().getText() not in self.wholeSentence) and \
                    ctx.Identifier().getText() not in assembly_operations and ctx.Identifier().getText() != "return":
                self.add_line(f"//{ctx.Identifier().getText()}({expression}) function {ctx.Identifier()} not declared")
                return self.visitChildren(ctx)
            semicolon = ";"
            if self.is_assembly:
                semicolon = ""
            self.add_line(f"{ctx.Identifier().getText()}({expression}){semicolon}")
            return self.visitChildren(ctx)

    def visitBoolean(self, ctx: YulParser.BooleanContext):
        return self.visitChildren(ctx)

    def visitLiteral(self, ctx: YulParser.LiteralContext):
        return self.visitChildren(ctx)

    def visitTypedIdentifierList(self, ctx: YulParser.TypedIdentifierListContext):
        return self.visitChildren(ctx)

    def visitIdentifierList(self, ctx: YulParser.IdentifierListContext):
        return self.visitChildren(ctx)

    def visitTypeName(self, ctx: YulParser.TypeNameContext):
        return self.visitChildren(ctx)

    def visitComment(self, ctx: YulParser.CommentContext):
        self.add_line(f"{ctx.getText()}")
        return self.visitChildren(ctx)

    def get_solidity_code(self) -> str:
        return "\n".join(self.output)
