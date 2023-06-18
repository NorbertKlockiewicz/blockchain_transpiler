from antlr4.tree.Tree import SyntaxTree, TerminalNodeImpl

from dist.VyperParser import VyperParser
from dist.VyperParserVisitor import VyperParserVisitor
from dist.SolidityParser import SolidityParser
import io

st = SyntaxTree()


class VyperToSolidityTranspiler(VyperParserVisitor):
    def __init__(self, fp):
        self.indentation_level = 0
        self.indentation = '    '
        self.output = fp

        self.comments = []

        self.output.truncate(0)

    def get_indentation(self):
        return self.indentation * self.indentation_level

    def visitModule(self, ctx: VyperParser.ModuleContext):
        self.output.write('pragma solidity >=0.4.0 <0.9.0;\n\n')
        self.output.write('contract FromVyper {\n')
        self.indentation_level += 1
        self.visitChildren(ctx)
        self.output.write('\n}\n\n')

        self.output.write('//######## INSTRUCTIONS TO TRANSLATE MANUALLY ########\n')
        for comment in self.comments:
            self.output.write(comment)

    def visitImportname(self, ctx: VyperParser.ImportnameContext):
        return super().visitImportname(ctx)

    def visitImport_(self, ctx: VyperParser.Import_Context):
        self.comments.append('// TODO: ' + ctx.getText() + '\n')

    def visitImportpath(self, ctx: VyperParser.ImportpathContext):
        return super().visitImportpath(ctx)

    def visitImportalias(self, ctx: VyperParser.ImportaliasContext):
        return super().visitImportalias(ctx)

    def visitImportlist(self, ctx: VyperParser.ImportlistContext):
        return super().visitImportlist(ctx)

    def visitImportfrom(self, ctx: VyperParser.ImportfromContext):
        return super().visitImportfrom(ctx)

    def visitConstantdef(self, ctx: VyperParser.ConstantdefContext):
        self.output.write(self.get_indentation())
        self.visit(ctx.type_())
        self.output.write(' constant ')
        self.output.write(ctx.NAME().getText())
        self.output.write(' = ')

        super().visit(ctx.expr())

        self.output.write(';')

        if ctx.NEWLINE() is not None:
            self.output.write('\n')

    def visitImmutabledef(self, ctx: VyperParser.ImmutabledefContext):
        line = \
            self.get_indentation() \
            + ctx.type_().NAME().getText() \
            + ' ' + ctx.IMMUTABLE().getText() \
            + ' ' + ctx.NAME().getText() \
            + ';'

        self.output.write(line)

    def visitVariable(self, ctx: VyperParser.VariableContext):
        self.visit(ctx.type_())

        self.output.write(' ' + ctx.NAME().getText())

    def visitVariablewithgetter(self, ctx: VyperParser.VariablewithgetterContext):
        self.visit(ctx.type_())

        self.output.write(' ' + 'public')

        self.output.write(' ' + ctx.NAME().getText())

    def visitVariabledef(self, ctx: VyperParser.VariabledefContext):
        self.output.write(self.get_indentation())

        super().visitVariabledef(ctx)

        self.output.write(';')

        if ctx.NEWLINE() is not None:
            self.output.write('\n\n')


    def visitDecorator(self, ctx: VyperParser.DecoratorContext):
        self.decorators.append(ctx)

    def visitDecorators(self, ctx: VyperParser.DecoratorsContext):
        super().visitDecorators(ctx)

        if self.decorators:
            self.output.write(self.get_indentation() + '// ##### VYPER DECORATORS #####\n')
            for idx, dec in enumerate(self.decorators):
                self.output.write(self.get_indentation() + f'// {dec.getText()}')
                self.decorators[idx] = dec.NAME().getText()

    def visitParameter(self, ctx: VyperParser.ParameterContext):
        self.visit(ctx.type_())

        self.output.write(' ' + ctx.NAME().getText())

        if ctx.ASSIGN() is not None:
            self.output.write(' = ')
            self.visit(ctx.expr())

    def visitParameters(self, ctx: VyperParser.ParametersContext):
        isParameter = lambda x: isinstance(x, VyperParser.ParameterContext)

        children = list(ctx.getChildren(isParameter))

        for idx, child in enumerate(children):
            self.visit(child)

            if idx < len(children) - 1:
                self.output.write(', ')

    def visitReturns_(self, ctx: VyperParser.Returns_Context):
        self.output.write(' returns (')
        self.visit(ctx.type_())
        self.output.write(')')

    def visitFunctionsig(self, ctx: VyperParser.FunctionsigContext):

        if ctx.NAME().getText() == '__init__':
            self.output.write(self.get_indentation() + 'constructor ')
        elif ctx.NAME().getText() == '__default__':
            self.output.write(self.get_indentation() + 'fallback')
        else:
            self.output.write(self.get_indentation() + 'function ')

            self.output.write(ctx.NAME().getText())

        self.output.write('(')

        if ctx.parameters() is not None:
            self.visit(ctx.parameters())

        self.output.write(')')

        if ctx.NAME().getText()[0] == '_':
            self.output.write(' private')
        else:
            self.output.write(' public')

        if isinstance(ctx.parentCtx, VyperParser.InterfacefunctionContext):
            self.output.write(' external')
            self.output.write(' ' + ctx.parentCtx.mutability().getText())

        if isinstance(ctx.parentCtx, VyperParser.FunctiondefContext):
            isDecorator = lambda x: isinstance(x, VyperParser.DecoratorContext)

            decorators = sorted(ctx.parentCtx.decorators().getChildren(isDecorator), key=lambda x: x.getText())

            modifiers = []

            for decorator in decorators:
                if decorator.NAME().getText() in ('external', 'internal'):
                    modifiers.append(decorator.NAME().getText())
                elif decorator.NAME().getText() in ('payable', 'pure', 'view'):
                    modifiers.append(decorator.NAME().getText())

            for modifier in modifiers:
                self.output.write(' ' + modifier)

        if ctx.returns_() is not None:
            self.visit(ctx.returns_())

    def visitFunctiondef(self, ctx: VyperParser.FunctiondefContext):
        self.__setattr__('decorators', [])

        self.visit(ctx.decorators())

        if 'noreentrant' in self.decorators:
            lock_variable = ctx.functionsig().NAME().getText() + 'ReentrancyLock'
            self.output.write(self.get_indentation() + f'bool internal {lock_variable} = False;\n')

        docstring = ctx.body().DOCSTRING()

        if docstring is not None:
            self.output.write(self.get_indentation() + '/**')
            self.output.write(docstring.getText()[3:-3])
            self.output.write('*/\n')

        self.visit(ctx.functionsig())


        self.output.write('\n' + self.get_indentation() + '{')

        self.indentation_level += 1

        if 'noreentrant' in self.decorators:
            self.output.write('\n' + self.get_indentation() + '// Reentrancy lock\n')
            self.output.write(self.get_indentation() + f'require(!{lock_variable}, "No re-entrancy");\n')
            self.output.write(self.get_indentation() + f'{lock_variable} = true;\n')

        self.visit(ctx.body())

        if 'noreentrant' in self.decorators:
            self.output.write('\n' + self.get_indentation() + '// Reentrancy unlock\n')
            self.output.write(self.get_indentation() + f'{lock_variable} = false;\n')

        self.indentation_level -= 1

        self.output.write(self.get_indentation() + '}\n\n')

        self.__delattr__('decorators')

    def visitBody(self, ctx: VyperParser.BodyContext):
        self.output.write('\n')
        isStatement = lambda x: isinstance(x, VyperParser.StmtContext) \
                                and x.getChild(0) is not None \
                                and not isinstance(x.getChild(0), VyperParser.PassstmtContext)

        for child in ctx.getChildren(isStatement):
            self.output.write(self.get_indentation())
            self.visit(child)

    def visitEventmember(self, ctx: VyperParser.EventmemberContext):
        self.visit(ctx.type_())
        self.output.write(' ')
        self.output.write(ctx.NAME().getText())

    def visitIndexedeventarg(self, ctx: VyperParser.IndexedeventargContext):
        self.visit(ctx.type_())
        self.output.write(
            ' ' +
            'indexed' +
            ' ' +
            ctx.NAME().getText()
        )

    def visitEventbody(self, ctx: VyperParser.EventbodyContext):


        isEventMember = lambda x: isinstance(x, VyperParser.EventmemberContext) or isinstance(x, VyperParser.IndexedeventargContext)

        children = list(ctx.getChildren(isEventMember))

        for idx, child in enumerate(children):
            self.visit(child)

            if idx != len(children) - 1:
                self.output.write(', ')

    def visitEventdef(self, ctx: VyperParser.EventdefContext):
        self.output.write(
            self.get_indentation() +
            'event' +
            ' ' +
            ctx.NAME().getText()
        )
        self.output.write('(')
        self.visitChildren(ctx)
        self.output.write(');\n')

    def visitEnummember(self, ctx: VyperParser.EnummemberContext):
        self.output.write(ctx.NAME().getText())

    def visitEnumbody(self, ctx: VyperParser.EnumbodyContext):
        is_enum_member = lambda x: isinstance(x, VyperParser.EnummemberContext)

        enum_members = list(ctx.getChildren(is_enum_member))

        for idx, child in enumerate(enum_members):
            self.visit(child)

            if idx != len(enum_members) - 1:
                self.output.write(', ')


    def visitEnumdef(self, ctx: VyperParser.EnumdefContext):
        self.output.write(self.get_indentation() + f'enum {ctx.NAME()} ')

        self.output.write('{ ')

        self.visit(ctx.enumbody())

        self.output.write(' }\n')

    def visitArraydef(self, ctx: VyperParser.ArraydefContext):
        if ctx.NAME() is not None:
            if ctx.NAME().getText() == 'String':
                self.output.write('string')
            elif ctx.NAME().getText() == 'Bytes':
                self.output.write('bytes')
            else:
                self.output.write(ctx.NAME().getText())
        elif ctx.arraydef() is not None:
            self.visit(ctx.arraydef())
        elif ctx.dynarraydef() is not None:
            self.visit(ctx.dynarraydef())

        self.visit(ctx.arraydeftail())

    def visitArraydeftail(self, ctx: VyperParser.ArraydeftailContext):
        if ctx.NAME() is not None:
            self.output.write('[' + ctx.NAME().getText() + ']')
        elif ctx.DECNUMBER() is not None:
            self.output.write('[' + ctx.DECNUMBER().getText() + ']')

    def visitDynarraydef(self, ctx: VyperParser.DynarraydefContext):

        self.visit(ctx.dynarraydefinner())

        self.output.write('[]')

    def visitDynarraydefinner(self, ctx: VyperParser.DynarraydefinnerContext):
        if ctx.NAME() is not None:
            self.output.write(ctx.NAME().getText())
        elif ctx.arraydef() is not None:
            self.visit(ctx.arraydef())
        elif ctx.dynarraydef() is not None:
            self.visit(ctx.dynarraydef())

    def visitTupledef(self, ctx: VyperParser.TupledefContext):
        self.output.write('(')
        children = list(ctx.getChildren(lambda x: isinstance(x, VyperParser.TupledefinnerContext)))

        for idx, children in enumerate(children):
            self.visit(children)

            if idx != len(children) - 1:
                self.output.write(', ')

        self.output.write(')')

    def visitTupledefinner(self, ctx: VyperParser.TupledefinnerContext):
        if ctx.NAME() is not None:
            self.output.write(ctx.NAME().getText())
        elif ctx.arraydef() is not None:
            self.visit(ctx.arraydef())
        elif ctx.tupledef() is not None:
            self.visit(ctx.tupledef())
        elif ctx.dynarraydef() is not None:
            self.visit(ctx.dynarraydef())

    def visitMapdef(self, ctx: VyperParser.MapdefContext):
        self.output.write('mapping (')

        if ctx.NAME() is not None:
            self.output.write(ctx.NAME().getText())
        elif ctx.arraydef() is not None:
            self.visit(ctx.arraydef())

        self.output.write(' => ')

        self.visit(ctx.type_())

        self.output.write(')')

    def visitType_(self, ctx: VyperParser.Type_Context):
        if ctx.NAME() is not None:
            self.output.write(ctx.NAME().getText())
        elif ctx.arraydef() is not None:
            self.visit(ctx.arraydef())
        elif ctx.tupledef() is not None:
            self.visit(ctx.tupledef())
        elif ctx.mapdef() is not None:
            self.visit(ctx.mapdef())
        elif self.visit(ctx.dynarraydef()) is not None:
            self.visit(ctx.dynarraydef())

    def visitStructmember(self, ctx: VyperParser.StructmemberContext):
        self.output.write(self.get_indentation())
        self.visit(ctx.type_())
        self.output.write(' ')
        self.output.write(ctx.NAME().getText())
        self.output.write(';\n')

    def visitStructdef(self, ctx: VyperParser.StructdefContext):
        self.output.write(self.get_indentation() + 'struct ' + ctx.NAME().getText() + ' {\n')
        self.indentation_level += 1
        self.visitChildren(ctx)
        self.indentation_level -= 1
        self.output.write(self.get_indentation() + '}\n\n')

    def visitMutability(self, ctx: VyperParser.MutabilityContext):
        self.output.write(ctx.getText())

    def visitInterfacefunction(self, ctx: VyperParser.InterfacefunctionContext):
        self.visit(ctx.functionsig())
        self.output.write(';\n')

    def visitInterfacedef(self, ctx: VyperParser.InterfacedefContext):
        self.output.write(self.get_indentation() + 'interface ' + ctx.NAME().getText() + ' {\n')
        self.indentation_level += 1

        self.visitChildren(ctx)

        self.indentation_level -= 1
        self.output.write(self.get_indentation() + '}\n')

    def visitStmt(self, ctx: VyperParser.StmtContext):
        super().visitStmt(ctx)

        if ctx.ifstmt() is None and ctx.forstmt() is None and ctx.comment() is None:
            self.output.write(';')

        if ctx.COMMENT() is not None:
            self.output.write(' //' + ctx.COMMENT().getText()[1:])

        self.output.write('\n')

    def visitComment(self, ctx:VyperParser.CommentContext):
        if isinstance(ctx.parentCtx, VyperParser.ModuleContext):
            self.output.write(self.get_indentation())

        self.output.write('//' + ctx.COMMENT().getText()[1:] + '\n')

    def visitDocstring(self, ctx:VyperParser.DocstringContext):
        if isinstance(ctx.parentCtx, VyperParser.ModuleContext):
            self.output.write(self.get_indentation())

        self.output.write('/**')
        self.output.write(ctx.DOCSTRING().getText()[3:-3].replace('\n', '\n' + self.get_indentation()))
        self.output.write('*/\n')

    def visitDeclaration(self, ctx: VyperParser.DeclarationContext):
        self.visit(ctx.variable())

        if ctx.expr() is not None:
            self.output.write(' = ')
            self.visit(ctx.expr())

    def visitMultipleassign(self, ctx: VyperParser.MultipleassignContext):
        first = ctx.getChild(0)

        if isinstance(first, VyperParser.VariableaccessContext):
            self.visit(first)
        else:
            self.output.write('_')

        commas_count = len(ctx.COMMA())

        for i in range(commas_count):
            self.output.write(', ')

            first = ctx.getChild(2 + i*2)

            if isinstance(first, VyperParser.VariableaccessContext):
                self.visit(first)
            else:
                self.output.write('_')

    def visitAssign(self, ctx: VyperParser.AssignContext):
        if ctx.LPAREN() is not None:
            self.output.write("(")

        if ctx.variableaccess() is not None:
            self.visit(ctx.variableaccess())
        else:
            self.visit(ctx.multipleassign())

        if ctx.RPAREN() is not None:
            self.output.write(")")

        self.output.write(' = ')
        self.visit(ctx.expr())

    def visitAugoperator(self, ctx: VyperParser.AugoperatorContext):
        self.output.write(' ' + ctx.getText())

    def visitAugassign(self, ctx: VyperParser.AugassignContext):
        self.visit(ctx.variableaccess())
        self.visit(ctx.augoperator())
        self.output.write('= ')
        self.visit(ctx.expr())

    def visitPassstmt(self, ctx: VyperParser.PassstmtContext):
        self.output.write('{}')

    def visitBreakstmt(self, ctx: VyperParser.BreakstmtContext):
        self.output.write('break')

    def visitContinuestmt(self, ctx: VyperParser.ContinuestmtContext):
        self.output.write('continue')

    def visitLogstmt(self, ctx: VyperParser.LogstmtContext):
        self.output.write('emit ' + ctx.NAME().getText() + '(')
        if ctx.arguments() is not None:
            self.visit(ctx.arguments())
        self.output.write(')')

    def visitReturnstmt(self, ctx: VyperParser.ReturnstmtContext):
        self.output.write('return')

        if ctx.getChildCount() == 1:
            return

        self.output.write(' ')

        expressions = list(ctx.getChildren(lambda x: isinstance(x, VyperParser.ExprContext)))

        for idx, expression in enumerate(expressions):
            self.visit(expression)

            if idx != len(expressions) - 1:
                self.output.write(', ')


    def visitRaisestmt(self, ctx: VyperParser.RaisestmtContext):
        self.output.write("revert ")
        if ctx.expr() is not None:
            self.visit(ctx.expr())
        else:
            self.output.write('""')

    def visitAssertstmt(self, ctx: VyperParser.AssertstmtContext):
        self.output.write('require(')

        if ctx.getChildCount() == 2 or (ctx.getChildCount() == 4 and not isinstance(ctx.getChild(3), VyperParser.ExprContext)):
            self.visit(ctx.getChild(1))
            self.output.write(')')
            return

        if ctx.getChildCount() == 4:
            self.indentation_level += 1
            self.output.write('\n')
            self.output.write(self.get_indentation())
            self.visit(ctx.getChild(1))
            self.output.write(',\n')
            self.output.write(self.get_indentation())
            self.visit(ctx.getChild(3))
            self.output.write('\n')
            self.indentation_level -= 1
            self.output.write(self.get_indentation())
            self.output.write(')')


    def visitCondexec(self, ctx: VyperParser.CondexecContext):
        self.output.write('(')
        self.visit(ctx.expr())
        self.output.write(')')
        self.output.write(' {')
        self.indentation_level += 1
        self.visit(ctx.body())
        self.indentation_level -= 1
        self.output.write(self.get_indentation() + '}')

    def visitDefaultexec(self, ctx: VyperParser.DefaultexecContext):
        return super().visitDefaultexec(ctx)

    def visitIfstmt(self, ctx: VyperParser.IfstmtContext):
        self.output.write('if ')
        self.visit(ctx.getChild(1))

        for idx, another_condition in enumerate(ctx.ELIF(), start=1):
            self.output.write(self.get_indentation() + 'else if ')
            self.visit(ctx.getChild(idx * 2 + 1))

    def visitLoopvariable(self, ctx: VyperParser.LoopvariableContext):
        return super().visitLoopvariable(ctx)

    def visitLoopiterator(self, ctx: VyperParser.LoopiteratorContext):
        return super().visitLoopiterator(ctx)

    def visitForstmt(self, ctx: VyperParser.ForstmtContext):
        self.output.write('\n' + self.get_indentation() + '// TODO: CHECK THE LOOP AND ITS VARIABLES')
        self.output.write('\n' + self.get_indentation())

        expr_type = self.get_expr_type(ctx.loopiterator().expr())

        if isinstance(expr_type, VyperParser.VariableaccessContext):
            if expr_type.NAME().getText() == 'range':
                args = expr_type.call()[0].arguments().argument()
                i_name = ctx.loopvariable().NAME()[0].getText()
                if len(args) == 1:
                    self.output.write(f'for (uint {i_name} = 0; {i_name} < {args[0].getText()}; {i_name}++) {{')
                elif len(args) == 2:
                    self.output.write(f'for (uint {i_name} = {args[0].getText()}; {i_name} < {args[1].getText()}; {i_name}++) {{')
            else:
                self.output.write(f'for (/*{ctx.loopvariable().getText()} in {ctx.loopiterator().getText()} {{')
        else:
            self.output.write(f'for (/*{ctx.loopvariable().getText()} in {ctx.loopiterator().getText()} */) {{')

        self.indentation_level += 1

        self.visit(ctx.body())

        self.indentation_level -= 1

        self.output.write(self.get_indentation() + '}\n')
        self.output.write('\n')


    def visitExpr(self, ctx: VyperParser.ExprContext):
        return super().visitExpr(ctx)

    def visitVariableaccess(self, ctx: VyperParser.VariableaccessContext):
        skip_first_get_attr = False

        if ctx.getText()[:5] == 'send(':
            print(ctx.getText())
            self.visit(ctx.call(0).arguments().argument(0))
            self.output.write('.transfer(')
            self.visit(ctx.call(0).arguments().argument(1))
            self.output.write(')')
            return

        if ctx.NAME() is not None and ctx.NAME().getText() != 'self':
            self.output.write(ctx.NAME().getText())
        elif ctx.variableaccess() is not None:
            self.output.write('(')
            self.visit(ctx.variableaccess())
            self.output.write(')')
        else:
            skip_first_get_attr = True

        notVisited = lambda x: not isinstance(x, VyperParser.VariableaccessContext) and not isinstance(x, TerminalNodeImpl)


        for child in ctx.getChildren(notVisited):
            if skip_first_get_attr and isinstance(child, VyperParser.GetattrContext):
                skip_first_get_attr = False
                self.output.write(child.getText()[1:])
                continue

            self.visit(child)

    def visitGetattr(self, ctx: VyperParser.GetattrContext):
        self.output.write(ctx.getText())

    def visitGetitem(self, ctx: VyperParser.GetitemContext):
        self.output.write('[')
        self.visit(ctx.expr())
        self.output.write(']')

    def visitCall(self, ctx: VyperParser.CallContext):
        self.output.write('(')

        self.visit(ctx.arguments())

        self.output.write(')')

    def visitArg(self, ctx: VyperParser.ArgContext):
        return super().visitArg(ctx)

    def visitKwarg(self, ctx: VyperParser.KwargContext):
        self.output.write(ctx.NAME().getText() + ' = ')
        self.visit(ctx.expr())

    def visitArgument(self, ctx: VyperParser.ArgumentContext):
        return super().visitArgument(ctx)

    def visitArguments(self, ctx: VyperParser.ArgumentsContext):

        isArgument = lambda x: isinstance(x, VyperParser.ArgumentContext)

        arguments = list(ctx.getChildren(isArgument))

        for idx, argument in enumerate(arguments):
            self.visit(argument)

            if idx != len(arguments) - 1:
                self.output.write(', ')

    def visitTuple(self, ctx: VyperParser.TupleContext):
        self.output.write('(')

        for expr in ctx.expr():
            self.visit(expr)
            self.output.write(',')

        self.output.write(')')

    def visitList(self, ctx: VyperParser.ListContext):
        self.output.write('[')

        expressions = ctx.expr()

        for idx, expr in enumerate(expressions):
            self.visit(expr)

            if idx != len(expressions) - 1:
                self.output.write(',')

        self.output.write(']')

    def visitDict(self, ctx: VyperParser.DictContext):
        self.output.write('{\n')
        self.indentation_level += 1

        exprs = ctx.expr()

        for idx, expr in enumerate(exprs):
            self.output.write(self.get_indentation())
            self.output.write(ctx.NAME(idx).getText())
            self.output.write(': ')
            self.visit(exprs[idx])

            if idx != len(exprs) - 1:
                self.output.write(',\n')
            else:
                self.output.write('\n')

        self.indentation_level -= 1
        self.output.write(self.get_indentation() + '}')

    def visitOperation(self, ctx: VyperParser.OperationContext):
        return super().visitOperation(ctx)

    def visitBoolor(self, ctx: VyperParser.BoolorContext):
        if ctx.getChildCount() == 1:
            self.visit(ctx.getChild(0))
            return

        self.visit(ctx.getChild(0))
        self.output.write(' || ')
        self.visit(ctx.getChild(2))

    def visitBooland(self, ctx: VyperParser.BoolandContext):
        if ctx.getChildCount() == 1:
            self.visit(ctx.getChild(0))
            return

        self.visit(ctx.getChild(0))
        self.output.write(' && ')
        self.visit(ctx.getChild(2))

    def visitBoolnot(self, ctx: VyperParser.BoolnotContext):
        if ctx.getChildCount() == 1:
            self.visit(ctx.getChild(0))
            return

        self.output.write('!')
        self.visit(ctx.getChild(1))

    def visitComparator(self, ctx: VyperParser.ComparatorContext):
        if ctx.getChildCount() == 1:
            self.visit(ctx.getChild(0))
            return


        if ctx.IN() is None:
            self.visit(ctx.getChild(0))
            self.output.write(' ')
            self.output.write(ctx.getChild(1).getText())
            self.output.write(' ')
            self.visit(ctx.getChild(2))
        else:
            self.output.write("/* TODO: CHECK 'IN' CONDITION ")
            for child in ctx.children:
                self.output.write(child.getText() + ' ')
            self.output.write("*/")


    def visitBitwiseor(self, ctx: VyperParser.BitwiseorContext):
        if ctx.getChildCount() == 1:
            self.visit(ctx.getChild(0))
            return

        self.visit(ctx.getChild(0))
        self.output.write(' ')
        self.output.write(ctx.getChild(1).getText())
        self.output.write(' ')
        self.visit(ctx.getChild(2))

    def visitBitwisexor(self, ctx: VyperParser.BitwisexorContext):
        if ctx.getChildCount() == 1:
            self.visit(ctx.getChild(0))
            return

        self.visit(ctx.getChild(0))
        self.output.write(' ')
        self.output.write(ctx.getChild(1).getText())
        self.output.write(' ')
        self.visit(ctx.getChild(2))

    def visitBitwiseand(self, ctx: VyperParser.BitwiseandContext):
        if ctx.getChildCount() == 1:
            self.visit(ctx.getChild(0))
            return

        self.visit(ctx.getChild(0))
        self.output.write(' ')
        self.output.write(ctx.getChild(1).getText())
        self.output.write(' ')
        self.visit(ctx.getChild(2))

    def visitShift(self, ctx: VyperParser.ShiftContext):
        if ctx.getChildCount() == 1:
            self.visit(ctx.getChild(0))
            return

        self.visit(ctx.getChild(0))
        self.output.write(' ')
        self.output.write(ctx.getChild(1).getText())
        self.output.write(' ')
        self.visit(ctx.getChild(2))

    def visitSummation(self, ctx: VyperParser.SummationContext):
        if ctx.getChildCount() == 1:
            self.visit(ctx.getChild(0))
            return

        self.visit(ctx.getChild(0))
        self.output.write(' ')
        self.output.write(ctx.getChild(1).getText())
        self.output.write(' ')
        self.visit(ctx.getChild(2))

    def visitProduct(self, ctx: VyperParser.ProductContext):
        if ctx.getChildCount() == 1:
            self.visit(ctx.getChild(0))
            return

        self.visit(ctx.getChild(0))
        self.output.write(' ')
        self.output.write(ctx.getChild(1).getText())
        self.output.write(' ')
        self.visit(ctx.getChild(2))

    def visitUnary(self, ctx: VyperParser.UnaryContext):
        if ctx.getChildCount() == 1:
            self.visit(ctx.getChild(0))
            return

        self.output.write(ctx.getChild(0).getText())
        self.output.write(' ')
        self.visit(ctx.getChild(1))

    def visitPower(self, ctx: VyperParser.PowerContext):
        if ctx.getChildCount() == 1:
            self.visit(ctx.getChild(0))
            return

        self.visit(ctx.getChild(0))
        self.output.write(' ')
        self.output.write(ctx.getChild(1).getText())
        self.output.write(' ')
        self.visit(ctx.getChild(2))


    def visitEmpty(self, ctx: VyperParser.EmptyContext):
        self.visit(ctx.type_())
        self.output.write('(0)')

    def visitAbidecode(self, ctx: VyperParser.AbidecodeContext):
        self.output.write('abi.decode(')
        self.visit(ctx.arg())

        for kwarg in ctx.kwarg():
            self.output.write(',')
            self.visit(kwarg)
        self.output.write(')')

    def visitSpecialbuiltins(self, ctx: VyperParser.SpecialbuiltinsContext):
        return super().visitSpecialbuiltins(ctx)

    def visitAtom(self, ctx: VyperParser.AtomContext):
        if ctx.getChildCount() == 1:
            self.visit(ctx.getChild(0))
            return

        self.output.write('(')
        self.visit(ctx.operation())
        self.output.write(')')

    def visitNumber(self, ctx: VyperParser.NumberContext):
        self.output.write(ctx.getText())

    def visitLiteral(self, ctx: VyperParser.LiteralContext):
        if ctx.number() is not None:
            self.visit(ctx.number())
        elif ctx.STRING() is not None:
            self.output.write(ctx.STRING().getText())
        elif ctx.BOOL() is not None:
            self.output.write(ctx.BOOL().getText().lower())

    def get_expr_type(self, ctx: VyperParser.ExprContext):
        while ctx.getChildCount() == 1:
            ctx = ctx.getChild(0)

        return ctx

# TODO: SELFDESTRUCT https://docs.vyperlang.org/en/stable/built-in-functions.html?highlight=send#selfdestruct