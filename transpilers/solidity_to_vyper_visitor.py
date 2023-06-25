from dist.SolidityParserVisitor import SolidityParserVisitor
from dist.SolidityParser import SolidityParser
from antlr4 import *
import io
from dist.SolidityLexer import SolidityLexer

class SolidityToVyperVisitor(SolidityParserVisitor):
    def __init__(self):
        self.indentation_level = 0
        self.indentation = '    '
        self.output = []
        self.state_variables = []

    def add_line(self, line: str):
        print('add', line)
        self.output.append(self.indentation * (self.indentation_level - 1) + line)

    def visitSourceUnit(self, ctx: SolidityParser.SourceUnitContext):
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#pragmaDirective.
    def visitPragmaDirective(self, ctx: SolidityParser.PragmaDirectiveContext):
        self.add_line("# pragma directive not supported in yul")
        self.add_line(f"#{ctx.getText()}")
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#importDirective.
    def visitImportDirective(self, ctx: SolidityParser.ImportDirectiveContext):
        print('importDirective: ', ctx.getText())
        self.add_line(f"TODO: imports not supported in Vyper{ctx.getText()}")
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#importAliases.
    def visitImportAliases(self, ctx: SolidityParser.ImportAliasesContext):
        print('importAliases: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#path.
    def visitPath(self, ctx: SolidityParser.PathContext):
        print('path: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#symbolAliases.
    def visitSymbolAliases(self, ctx: SolidityParser.SymbolAliasesContext):
        print('symbolAliases: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#contractDefinition.
    def visitContractDefinition(self, ctx: SolidityParser.ContractDefinitionContext):
        print('contractDefinition: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#interfaceDefinition.
    def visitInterfaceDefinition(self, ctx: SolidityParser.InterfaceDefinitionContext):
        print('interfaceDefinition: ', ctx.getText())
        self.add_line(f"interface {ctx.identifier().getText()}:")
        self.indentation_level += 1
        return self.visitBlock(ctx)
        self.indentation_level -= 1
    # Visit a parse tree produced by SolidityParser#libraryDefinition.
    def visitLibraryDefinition(self, ctx: SolidityParser.LibraryDefinitionContext):
        print('libraryDefinition: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#inheritanceSpecifierList.
    def visitInheritanceSpecifierList(self, ctx: SolidityParser.InheritanceSpecifierListContext):
        print('inheritanceSpecifierList: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#inheritanceSpecifier.
    def visitInheritanceSpecifier(self, ctx: SolidityParser.InheritanceSpecifierContext):
        print('inheritanceSpecifier: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#contractBodyElement.
    def visitContractBodyElement(self, ctx: SolidityParser.ContractBodyElementContext):
        print('contractBodyElement: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#namedArgument.
    def visitNamedArgument(self, ctx: SolidityParser.NamedArgumentContext):
        print('namedArgument: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#callArgumentList.
    def visitCallArgumentList(self, ctx: SolidityParser.CallArgumentListContext):
        print('callArgumentList: ', ctx.getText())

        return ctx.getText()
    # Visit a parse tree produced by SolidityParser#identifierPath.
    def visitIdentifierPath(self, ctx: SolidityParser.IdentifierPathContext):
        print('identifierPath: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#modifierInvocation.
    def visitModifierInvocation(self, ctx: SolidityParser.ModifierInvocationContext):
        print('modifierInvocation: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#visibility.
    def visitVisibility(self, ctx: SolidityParser.VisibilityContext):
        print('visibility: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#parameterList.
    def visitParameterList(self, ctx: SolidityParser.ParameterListContext):
        print('parameterList: ', ctx.getText())
        parameters = []
        for parameter in ctx.parameters:
            if parameter.typeName() and parameter.identifier():
                parameters.append(f"{self.visit(parameter.typeName())} {parameter.identifier().getText()}")
            elif parameter.typeName():
                parameters.append(f"{self.visit(parameter.typeName())}")
            else:
                parameters.append(f"{parameter.identifier().getText()}")

        if len(parameters) > 1:
            return f"({', '.join(parameters)})"
        return ", ".join(parameters)
    # Visit a parse tree produced by SolidityParser#parameterDeclaration.
    def visitParameterDeclaration(self, ctx: SolidityParser.ParameterDeclarationContext):
        print('parameterDeclaration: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#constructorDefinition.
    def visitConstructorDefinition(self, ctx: SolidityParser.ConstructorDefinitionContext):
        print('constructorDefinition: ', ctx.getText())
        arguments = ""
        if ctx.parameterList():
            for i in range(len(ctx.parameterList().parameterDeclaration())):
                if i == len(ctx.parameterList().parameterDeclaration()) - 1:
                    arguments += f"{self.visit(ctx.parameterList().parameterDeclaration(i).typeName())} {ctx.parameterList().parameterDeclaration(i).identifier().getText()}"
                else:
                    arguments += f"{self.visit(ctx.parameterList().parameterDeclaration(i).typeName())} {ctx.parameterList().parameterDeclaration(i).identifier().getText()} "

        self.add_line("@external")
        if ctx.Payable():
            self.add_line("@payable")
        self.add_line(f"def __init__({arguments}):")
        return self.visitBlock(ctx)
    # Visit a parse tree produced by SolidityParser#stateMutability.
    def visitStateMutability(self, ctx: SolidityParser.StateMutabilityContext):
        print('stateMutability: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#overrideSpecifier.
    def visitOverrideSpecifier(self, ctx: SolidityParser.OverrideSpecifierContext):
        print('overrideSpecifier: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#contractFunctionDefinition.
    def visitContractFunctionDefinition(self, ctx: SolidityParser.ContractFunctionDefinitionContext):
        print('contractFunctionDefinition: ', ctx.getText())
        print(ctx.stateMutability())
        arguments = []
        if ctx.visibility(0).getText() == 'public' or ctx.visibility(0).getText() == 'external':
            self.add_line("@external")
        elif ctx.visibility(0).getText() == 'private' or ctx.visibility(0).getText() == 'internal':
            self.add_line("@internal")


        if len(ctx.stateMutability()) > 0:
            if ctx.stateMutability(0).getText() == 'pure':
                self.add_line("@pure")
            elif ctx.stateMutability(0).getText() == 'view':
                self.add_line("@view")
            elif ctx.stateMutability(0).getText() == 'payable':
                self.add_line("@payable")
        if ctx.Returns():
            if len(ctx.parameterList()) < 2:
                self.add_line(f"def {ctx.identifier().getText()}() -> {self.visit(ctx.parameterList()[-1])}:")
            else:
                for i in range(len(ctx.parameterList()[0].parameterDeclaration())):
                    arguments.append(f"{self.visit(ctx.parameterList()[0].parameterDeclaration()[i].typeName())} {ctx.parameterList()[0].parameterDeclaration()[i].identifier().getText()}")

                self.add_line(f"def {ctx.identifier().getText()}({','.join(arguments)}) -> {self.visit(ctx.parameterList()[-1])}:")
        else:
            if len(ctx.parameterList()) > 0:
                for i in range(len(ctx.parameterList()[0].parameterDeclaration())):
                    arguments.append(f"{self.visit(ctx.parameterList()[0].parameterDeclaration()[i].typeName())} {ctx.parameterList()[0].parameterDeclaration()[i].identifier().getText()}")

            self.add_line(f"def {ctx.identifier().getText()}({','.join(arguments)}):")

        return self.visitBlock(ctx)
    # Visit a parse tree produced by SolidityParser#freeFunctionDefinition.
    def visitFreeFunctionDefinition(self, ctx: SolidityParser.FreeFunctionDefinitionContext):
        print('freeFunctionDefinition: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#modifierDefinition.
    def visitModifierDefinition(self, ctx: SolidityParser.ModifierDefinitionContext):
        print('modifierDefinition: ', ctx.getText())
        return self.add_line(f"'''TODO: modifiers not supported in vyper(implement it manually):\n {ctx.getText()}'''")
    # Visit a parse tree produced by SolidityParser#fallbackFunctionDefinition.
    def visitFallbackFunctionDefinition(self, ctx: SolidityParser.FallbackFunctionDefinitionContext):
        print('fallbackFunctionDefinition: ', ctx.getText())

        arguments = ""
        if ctx.parameterList():
            for i in range(len(ctx.parameterList().parameterDeclaration())):
                if i == len(ctx.parameterList().parameterDeclaration()) - 1:
                    arguments += f"{self.visit(ctx.parameterList().parameterDeclaration(i).typeName())} {ctx.parameterList().parameterDeclaration(i).identifier().getText()}"
                else:
                    arguments += f"{self.visit(ctx.parameterList().parameterDeclaration(i).typeName())} {ctx.parameterList().parameterDeclaration(i).identifier().getText()} "

        self.add_line("#Fallback function")
        self.add_line("@public")
        self.add_line(f"def __default__({arguments}):")
        return self.visitBlock(ctx)
    # Visit a parse tree produced by SolidityParser#receiveFunctionDefinition.
    def visitReceiveFunctionDefinition(self, ctx: SolidityParser.ReceiveFunctionDefinitionContext):
        print('receiveFunctionDefinition: ', ctx.getText())
        self.add_line("#Receive function")
        self.add_line("@public")
        self.add_line("@payable")
        self.add_line(f"def __default__():")
        return self.visitBlock(ctx)
    # Visit a parse tree produced by SolidityParser#structDefinition.
    def visitStructDefinition(self, ctx: SolidityParser.StructDefinitionContext):
        print('structDefinition: ', ctx.getText())
        self.add_line(f"struct {ctx.identifier().getText()}:")
        for member in ctx.structMember():
            self.add_line(f"{self.visit(member)}")    # Visit a parse tree produced by SolidityParser#structMember.
    def visitStructMember(self, ctx: SolidityParser.StructMemberContext):
        return f"\t {self.visit(ctx.identifier())}: {self.visit(ctx.typeName())}"
    # Visit a parse tree produced by SolidityParser#enumDefinition.
    def visitEnumDefinition(self, ctx: SolidityParser.EnumDefinitionContext):
        print('enumDefinition: ', ctx.getText())
        self.add_line(f"enum {ctx.identifier(0).getText()}:")
        self.indentation_level += 1
        for i in range(len(ctx.identifier())):
            if i != 0:
                self.add_line(f"\t {ctx.identifier(i).getText()}")

        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#userDefinedValueTypeDefinition.
    def visitUserDefinedValueTypeDefinition(self, ctx: SolidityParser.UserDefinedValueTypeDefinitionContext):
        print('userDefinedValueTypeDefinition: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#stateVariableDeclaration.
    def visitStateVariableDeclaration(self, ctx: SolidityParser.StateVariableDeclarationContext):
        print('stateVariableDeclaration: ', ctx.getText())

        type = "public"
        if len(ctx.Private()) > 0:
            type = "private"
        elif len(ctx.Constant()) > 0:
            type = "constant"
        elif len(ctx.Immutable()) > 0:
            type = "immutable"

        if ctx.expression() is not None:
            print(ctx.expression().getText())
            self.add_line(ctx.identifier().getText()+ f": {type}" + f"({self.visit(ctx.typeName())})" + "=" + ctx.expression().getText())
        else:
            self.add_line(ctx.identifier().getText()+ f": {type}" + f"({self.visit(ctx.typeName())})")

        self.state_variables.append(ctx.identifier().getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#constantVariableDeclaration.
    def visitConstantVariableDeclaration(self, ctx: SolidityParser.ConstantVariableDeclarationContext):
        print('constantVariableDeclaration: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#eventParameter.
    def visitEventParameter(self, ctx: SolidityParser.EventParameterContext):
        print('eventParameter: ', ctx.getText())
        return f"{self.visit(ctx.identifier())}: {self.visit(ctx.typeName())}"
    # Visit a parse tree produced by SolidityParser#eventDefinition.
    def visitEventDefinition(self, ctx: SolidityParser.EventDefinitionContext):
        print('eventDefinition: ', ctx.getText())
        self.add_line(f"event {ctx.identifier().getText()}: ")
        for parameter in ctx.eventParameter():
            self.add_line(f"\t {self.visit(parameter)}")
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#errorParameter.
    def visitErrorParameter(self, ctx: SolidityParser.ErrorParameterContext):
        print('errorParameter: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#errorDefinition.
    def visitErrorDefinition(self, ctx: SolidityParser.ErrorDefinitionContext):
        print('errorDefinition: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#userDefinableOperator.
    def visitUserDefinableOperator(self, ctx: SolidityParser.UserDefinableOperatorContext):
        print('userDefinableOperator: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#usingDirective.
    def visitUsingDirective(self, ctx: SolidityParser.UsingDirectiveContext):
        print('usingDirective: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#typeName.
    def visitTypeName(self, ctx: SolidityParser.TypeNameContext):
        print('typeName: ', ctx.getText())
        if ctx.mappingType():
            return self.visit(ctx.mappingType())
        elif '[' in ctx.getText():
            return f"DynArray[{ctx.typeName().getText()}, 10]"
        else:
            return ctx.getText()

        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#elementaryTypeName.
    def visitElementaryTypeName(self, ctx: SolidityParser.ElementaryTypeNameContext):
        print('elementaryTypeName: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#functionTypeName.
    def visitFunctionTypeName(self, ctx: SolidityParser.FunctionTypeNameContext):
        print('functionTypeName: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx: SolidityParser.VariableDeclarationContext):
        print('variableDeclaration: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#dataLocation.
    def visitDataLocation(self, ctx: SolidityParser.DataLocationContext):
        print('dataLocation: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#UnaryPrefixOperation.
    def visitUnaryPrefixOperation(self, ctx: SolidityParser.UnaryPrefixOperationContext):
        print('UnaryPrefixOperation: ', ctx.getText())
        if ctx.Delete():
            self.add_line(f"del {ctx.expression().getText()}")
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#PrimaryExpression.
    def visitPrimaryExpression(self, ctx: SolidityParser.PrimaryExpressionContext):
        print('PrimaryExpression: ', ctx.getText())
        return ctx.getText()
    # Visit a parse tree produced by SolidityParser#OrderComparison.
    def visitOrderComparison(self, ctx: SolidityParser.OrderComparisonContext):
        print('OrderComparison: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#Conditional.
    def visitConditional(self, ctx: SolidityParser.ConditionalContext):
        print('Conditional: ', ctx.getText())
        if type(ctx.parentCtx) == SolidityParser.ReturnStatementContext:
            self.add_line(f"return {ctx.expression(1).getText()} if {ctx.expression(0).getText()} else {ctx.expression(2).getText()}")
        else:
            self.add_line(f"{ctx.expression(1).getText()} if {ctx.expression(0).getText()} else {ctx.expression(2).getText()}")
    # Visit a parse tree produced by SolidityParser#PayableConversion.
    def visitPayableConversion(self, ctx: SolidityParser.PayableConversionContext):
        print('PayableConversion: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#Assignment.
    def visitAssignment(self, ctx: SolidityParser.AssignmentContext):
        print('Assignment: ', ctx.getText())
        print(ctx.expression(1).getText())
        if ctx.expression(0).getText() in self.state_variables:
            self.add_line(f"self.{self.visit(ctx.expression(0))} {ctx.assignOp().getText()} {self.visit(ctx.expression(1))}")
        else:
            self.add_line(f"{self.visit(ctx.expression(0))} {ctx.assignOp().getText()} {self.visit(ctx.expression(1))}")

        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#UnarySuffixOperation.
    def visitUnarySuffixOperation(self, ctx: SolidityParser.UnarySuffixOperationContext):
        print('UnarySuffixOperation: ', ctx.getText())

        if type(ctx.parentCtx) != SolidityParser.ForStatementContext:
            if ctx.Inc():
                self.add_line(f"{ctx.expression().getText()} += 1")
            elif ctx.Dec():
                self.add_line(f"{ctx.expression().getText()} -= 1")
            return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#ShiftOperation.
    def visitShiftOperation(self, ctx: SolidityParser.ShiftOperationContext):
        print('ShiftOperation: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#BitAndOperation.
    def visitBitAndOperation(self, ctx: SolidityParser.BitAndOperationContext):
        print('BitAndOperation: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#FunctionCall.
    def visitFunctionCall(self, ctx: SolidityParser.FunctionCallContext):
        print('FunctionCall: ', ctx.getText())
        if type(ctx.parentCtx) != SolidityParser.StateVariableDeclarationContext:
            if ctx.expression().getText() == 'assert' or ctx.expression().getText() == 'require' or ctx.expression().getText() == 'revert':
                self.add_line(f"assert {ctx.callArgumentList().getText().replace('(', '').replace(')', '')}")
            else:
                self.add_line(f"{ctx.expression().getText()}{self.visit(ctx.callArgumentList())}")

        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#IndexRangeAccess.
    def visitIndexRangeAccess(self, ctx: SolidityParser.IndexRangeAccessContext):
        print('IndexRangeAccess: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#IndexAccess.
    def visitIndexAccess(self, ctx: SolidityParser.IndexAccessContext):
        print('IndexAccess: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#AddSubOperation.
    def visitAddSubOperation(self, ctx: SolidityParser.AddSubOperationContext):
        print('AddSubOperation: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#BitOrOperation.
    def visitBitOrOperation(self, ctx: SolidityParser.BitOrOperationContext):
        print('BitOrOperation: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#ExpOperation.
    def visitExpOperation(self, ctx: SolidityParser.ExpOperationContext):
        print('ExpOperation: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#AndOperation.
    def visitAndOperation(self, ctx: SolidityParser.AndOperationContext):
        print('AndOperation: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#InlineArray.
    def visitInlineArray(self, ctx: SolidityParser.InlineArrayContext):
        print('InlineArray: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#OrOperation.
    def visitOrOperation(self, ctx: SolidityParser.OrOperationContext):
        print('OrOperation: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#MemberAccess.
    def visitMemberAccess(self, ctx: SolidityParser.MemberAccessContext):
        print('MemberAccess: ', ctx.getText())
        if ctx.expression().getText in self.state_variables:
            print(f"self.{ctx.expression().getText()}.{ctx.identifier().getText()}")
            return f"self.{ctx.expression().getText()}.{ctx.identifier().getText()}"
        else:
            print(f"self.{ctx.expression().getText()}.{ctx.identifier().getText()}")
            return f"{ctx.expression().getText()}.{ctx.identifier().getText()}"
    # Visit a parse tree produced by SolidityParser#MulDivModOperation.
    def visitMulDivModOperation(self, ctx: SolidityParser.MulDivModOperationContext):
        print('MulDivModOperation: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#FunctionCallOptions.
    def visitFunctionCallOptions(self, ctx: SolidityParser.FunctionCallOptionsContext):
        print('FunctionCallOptions: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#NewExpr.
    def visitNewExpr(self, ctx: SolidityParser.NewExprContext):
        print('NewExpr: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#BitXorOperation.
    def visitBitXorOperation(self, ctx: SolidityParser.BitXorOperationContext):
        print('BitXorOperation: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#Tuple.
    def visitTuple(self, ctx: SolidityParser.TupleContext):
        print('Tuple: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#EqualityComparison.
    def visitEqualityComparison(self, ctx: SolidityParser.EqualityComparisonContext):
        print('EqualityComparison: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#MetaType.
    def visitMetaType(self, ctx: SolidityParser.MetaTypeContext):
        print('MetaType: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#assignOp.
    def visitAssignOp(self, ctx: SolidityParser.AssignOpContext):
        print('assignOp: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#tupleExpression.
    def visitTupleExpression(self, ctx: SolidityParser.TupleExpressionContext):
        print('tupleExpression: ', ctx.getText())
        expression = []
        for exp in ctx.expression():
            expression.append(exp.getText())
        return ",".join(expression)
    # Visit a parse tree produced by SolidityParser#inlineArrayExpression.
    def visitInlineArrayExpression(self, ctx: SolidityParser.InlineArrayExpressionContext):
        print('inlineArrayExpression: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#identifier.
    def visitIdentifier(self, ctx: SolidityParser.IdentifierContext):
        print('identifier: ', ctx.getText())
        return ctx.getText()
    # Visit a parse tree produced by SolidityParser#literal.
    def visitLiteral(self, ctx: SolidityParser.LiteralContext):
        print('literal: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#literalWithSubDenomination.
    def visitLiteralWithSubDenomination(self, ctx: SolidityParser.LiteralWithSubDenominationContext):
        print('literalWithSubDenomination: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#boolLiteral.
    def visitBoolLiteral(self, ctx: SolidityParser.BoolLiteralContext):
        print('boolLiteral: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#stringLiteral.
    def visitStringLiteral(self, ctx: SolidityParser.StringLiteralContext):
        print('stringLiteral: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#hexStringLiteral.
    def visitHexStringLiteral(self, ctx: SolidityParser.HexStringLiteralContext):
        print('hexStringLiteral: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#unicodeStringLiteral.
    def visitUnicodeStringLiteral(self, ctx: SolidityParser.UnicodeStringLiteralContext):
        print('unicodeStringLiteral: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#numberLiteral.
    def visitNumberLiteral(self, ctx: SolidityParser.NumberLiteralContext):
        print('numberLiteral: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#block.
    def visitBlock(self, ctx: SolidityParser.BlockContext):
        self.indentation_level += 1
        self.visitChildren(ctx)
        self.indentation_level -= 1
    # Visit a parse tree produced by SolidityParser#uncheckedBlock.
    def visitUncheckedBlock(self, ctx: SolidityParser.UncheckedBlockContext):
        print('uncheckedBlock: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#statement.
    def visitStatement(self, ctx: SolidityParser.StatementContext):
        print('statement: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#simpleStatement.
    def visitSimpleStatement(self, ctx: SolidityParser.SimpleStatementContext):
        print('simpleStatement: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#ifStatement.
    def visitIfStatement(self, ctx: SolidityParser.IfStatementContext):
        print('ifStatement: ', ctx.getText())

        if type(ctx.parentCtx.parentCtx) == SolidityParser.IfStatementContext:
            self.add_line("elif " + ctx.expression().getText() + ":")
            self.visit(ctx.statement(0))
        else:
            self.add_line("if " + ctx.expression().getText() + ":")
            self.visit(ctx.statement(0))

        if ctx.Else() is not None and ctx.statement(1).ifStatement() is None:
            self.add_line("else:")

        if len(ctx.statement()) > 1:
            self.visit(ctx.statement(1))

    # Visit a parse tree produced by SolidityParser#forStatement.
    def visitForStatement(self, ctx: SolidityParser.ForStatementContext):
        stop = ctx.expressionStatement().expression().expression(1).getText()
        step = 1
        if type(ctx.expression()) == SolidityParser.UnarySuffixOperationContext:
            if  "++" in ctx.expression().getText():
                step = 1
            elif "--" in ctx.expression().getText():
                step = -1
        elif type(ctx.expression()) == SolidityParser.UnaryPrefixOperationContext:
            if  "++" in ctx.expression().getText():
                step = 1
            elif "--" in ctx.expression().getText():
                step = -1

        self.add_line(f"for {ctx.simpleStatement().variableDeclarationStatement().variableDeclaration().identifier().getText()} in range({ctx.simpleStatement().variableDeclarationStatement().expression().getText()}, {stop}, {step}):")
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#whileStatement.
    def visitWhileStatement(self, ctx: SolidityParser.WhileStatementContext):
        print('whileStatement: ', ctx.getText())
        print(ctx.expression().getText())
        self.add_line(f"#Originally while({ctx.expression().getText()}) loop which is not supported in Vyper, manually convert to for loop")
        self.add_line("for x in range(100):")
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#doWhileStatement.
    def visitDoWhileStatement(self, ctx: SolidityParser.DoWhileStatementContext):
        print('doWhileStatement: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#continueStatement.
    def visitContinueStatement(self, ctx: SolidityParser.ContinueStatementContext):
        print('continueStatement: ', ctx.getText())
        self.add_line("continue")
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#breakStatement.
    def visitBreakStatement(self, ctx: SolidityParser.BreakStatementContext):
        print('breakStatement: ', ctx.getText())
        self.add_line("break")
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#tryStatement.
    def visitTryStatement(self, ctx: SolidityParser.TryStatementContext):
        print('tryStatement: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#catchClause.
    def visitCatchClause(self, ctx: SolidityParser.CatchClauseContext):
        print('catchClause: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#returnStatement.
    def visitReturnStatement(self, ctx: SolidityParser.ReturnStatementContext):
        print('returnStatement: ', ctx.getText())
        if type(ctx.expression()) != SolidityParser.ConditionalContext:
            self.add_line(f"return {ctx.expression().getText()}")
        else:
            self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#emitStatement.
    def visitEmitStatement(self, ctx: SolidityParser.EmitStatementContext):
        print('emitStatement: ', ctx.getText())
        self.add_line(f"log {ctx.expression().getText()}{self.visit(ctx.callArgumentList())}")
    # Visit a parse tree produced by SolidityParser#revertStatement.
    def visitRevertStatement(self, ctx: SolidityParser.RevertStatementContext):
        print('revertStatement: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#assemblyStatement.
    def visitAssemblyStatement(self, ctx: SolidityParser.AssemblyStatementContext):
        print('assemblyStatement: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#assemblyFlags.
    def visitAssemblyFlags(self, ctx: SolidityParser.AssemblyFlagsContext):
        print('assemblyFlags: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#variableDeclarationList.
    def visitVariableDeclarationList(self, ctx: SolidityParser.VariableDeclarationListContext):
        print('variableDeclarationList: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#variableDeclarationTuple.
    def visitVariableDeclarationTuple(self, ctx: SolidityParser.VariableDeclarationTupleContext):
        print('variableDeclarationTuple: ', ctx.getText())
        variables = []
        for v in ctx.variableDeclaration():
            variables.append(f"{self.visit(v.typeName())} {self.visit(v.identifier())}")
        return ",".join(variables)
    # Visit a parse tree produced by SolidityParser#variableDeclarationStatement.
    def visitVariableDeclarationStatement(self, ctx: SolidityParser.VariableDeclarationStatementContext):
        print('variableDeclarationStatement: ', ctx.getText())
        if ctx.variableDeclaration():
            if type(ctx.parentCtx.parentCtx) != SolidityParser.ForStatementContext:
               if type(ctx.expression()) == SolidityParser.ConditionalContext:
                   self.add_line(ctx.variableDeclaration().identifier().getText() + ": " +self.visit(ctx.variableDeclaration().typeName()) +" = ")
               else:
                   if ctx.expression() is not None:
                       self.add_line(ctx.variableDeclaration().identifier().getText() + ": " +self.visit(ctx.variableDeclaration().typeName()) +" = " + ctx.expression().getText())
                   else:
                       self.add_line(ctx.variableDeclaration().identifier().getText() + ": " + self.visit(ctx.variableDeclaration().typeName()))
        else:
            self.add_line(f"{self.visit(ctx.variableDeclarationTuple())} = {ctx.expression().getText()}")

    # Visit a parse tree produced by SolidityParser#expressionStatement.
    def visitExpressionStatement(self, ctx: SolidityParser.ExpressionStatementContext):
        print('expressionStatement: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#mappingType.
    def visitMappingType(self, ctx: SolidityParser.MappingTypeContext):
        print('mappingType: ', ctx.getText())
        return f"HashMap[{ctx.mappingKeyType().getText()}, {self.visit(ctx.typeName())}]"
    # Visit a parse tree produced by SolidityParser#mappingKeyType.
    def visitMappingKeyType(self, ctx: SolidityParser.MappingKeyTypeContext):
        print('mappingKeyType: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#yulStatement.
    def visitYulStatement(self, ctx: SolidityParser.YulStatementContext):
        print('yulStatement: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#yulBlock.
    def visitYulBlock(self, ctx: SolidityParser.YulBlockContext):
        print('yulBlock: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#yulVariableDeclaration.
    def visitYulVariableDeclaration(self, ctx: SolidityParser.YulVariableDeclarationContext):
        print('yulVariableDeclaration: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#yulAssignment.
    def visitYulAssignment(self, ctx: SolidityParser.YulAssignmentContext):
        print('yulAssignment: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#yulIfStatement.
    def visitYulIfStatement(self, ctx: SolidityParser.YulIfStatementContext):
        print('yulIfStatement: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#yulForStatement.
    def visitYulForStatement(self, ctx: SolidityParser.YulForStatementContext):
        print('yulForStatement: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#yulSwitchCase.
    def visitYulSwitchCase(self, ctx: SolidityParser.YulSwitchCaseContext):
        print('yulSwitchCase: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#yulSwitchStatement.
    def visitYulSwitchStatement(self, ctx: SolidityParser.YulSwitchStatementContext):
        print('yulSwitchStatement: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#yulFunctionDefinition.
    def visitYulFunctionDefinition(self, ctx: SolidityParser.YulFunctionDefinitionContext):
        print('yulFunctionDefinition: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#yulPath.
    def visitYulPath(self, ctx: SolidityParser.YulPathContext):
        print('yulPath: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#yulFunctionCall.
    def visitYulFunctionCall(self, ctx: SolidityParser.YulFunctionCallContext):
        print('yulFunctionCall: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#yulbool.
    def visitYulbool(self, ctx: SolidityParser.YulboolContext):
        print('yulbool: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#yulLiteral.
    def visitYulLiteral(self, ctx: SolidityParser.YulLiteralContext):
        print('yulLiteral: ', ctx.getText())
        return self.visitChildren(ctx)
    # Visit a parse tree produced by SolidityParser#yulExpression.
    def visitYulExpression(self, ctx: SolidityParser.YulExpressionContext):
        print('yulExpression: ', ctx.getText())
        return self.visitChildren(ctx)
    def get_vyper_code(self) -> str:
        return "\n".join(self.output)

