# Generated from VyperParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .VyperParser import VyperParser
else:
    from VyperParser import VyperParser

# This class defines a complete generic visitor for a parse tree produced by VyperParser.

class VyperParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by VyperParser#module.
    def visitModule(self, ctx:VyperParser.ModuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#importname.
    def visitImportname(self, ctx:VyperParser.ImportnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#import_.
    def visitImport_(self, ctx:VyperParser.Import_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#importpath.
    def visitImportpath(self, ctx:VyperParser.ImportpathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#importalias.
    def visitImportalias(self, ctx:VyperParser.ImportaliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#importlist.
    def visitImportlist(self, ctx:VyperParser.ImportlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#importfrom.
    def visitImportfrom(self, ctx:VyperParser.ImportfromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#implements.
    def visitImplements(self, ctx:VyperParser.ImplementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#constantdef.
    def visitConstantdef(self, ctx:VyperParser.ConstantdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#immutabledef.
    def visitImmutabledef(self, ctx:VyperParser.ImmutabledefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#variable.
    def visitVariable(self, ctx:VyperParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#variablewithgetter.
    def visitVariablewithgetter(self, ctx:VyperParser.VariablewithgetterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#variabledef.
    def visitVariabledef(self, ctx:VyperParser.VariabledefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#decorator.
    def visitDecorator(self, ctx:VyperParser.DecoratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#decorators.
    def visitDecorators(self, ctx:VyperParser.DecoratorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#parameter.
    def visitParameter(self, ctx:VyperParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#parameters.
    def visitParameters(self, ctx:VyperParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#returns_.
    def visitReturns_(self, ctx:VyperParser.Returns_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#functionsig.
    def visitFunctionsig(self, ctx:VyperParser.FunctionsigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#functiondef.
    def visitFunctiondef(self, ctx:VyperParser.FunctiondefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#body.
    def visitBody(self, ctx:VyperParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#eventmember.
    def visitEventmember(self, ctx:VyperParser.EventmemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#indexedeventarg.
    def visitIndexedeventarg(self, ctx:VyperParser.IndexedeventargContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#eventbody.
    def visitEventbody(self, ctx:VyperParser.EventbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#eventdef.
    def visitEventdef(self, ctx:VyperParser.EventdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#enummember.
    def visitEnummember(self, ctx:VyperParser.EnummemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#enumbody.
    def visitEnumbody(self, ctx:VyperParser.EnumbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#enumdef.
    def visitEnumdef(self, ctx:VyperParser.EnumdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#arraydef.
    def visitArraydef(self, ctx:VyperParser.ArraydefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#arraydeftail.
    def visitArraydeftail(self, ctx:VyperParser.ArraydeftailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#dynarraydef.
    def visitDynarraydef(self, ctx:VyperParser.DynarraydefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#dynarraydefinner.
    def visitDynarraydefinner(self, ctx:VyperParser.DynarraydefinnerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#tupledef.
    def visitTupledef(self, ctx:VyperParser.TupledefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#tupledefinner.
    def visitTupledefinner(self, ctx:VyperParser.TupledefinnerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#mapdef.
    def visitMapdef(self, ctx:VyperParser.MapdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#type_.
    def visitType_(self, ctx:VyperParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#structmember.
    def visitStructmember(self, ctx:VyperParser.StructmemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#structdef.
    def visitStructdef(self, ctx:VyperParser.StructdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#mutability.
    def visitMutability(self, ctx:VyperParser.MutabilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#interfacefunction.
    def visitInterfacefunction(self, ctx:VyperParser.InterfacefunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#interfacedef.
    def visitInterfacedef(self, ctx:VyperParser.InterfacedefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#stmt.
    def visitStmt(self, ctx:VyperParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#comment.
    def visitComment(self, ctx:VyperParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#docstring.
    def visitDocstring(self, ctx:VyperParser.DocstringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#declaration.
    def visitDeclaration(self, ctx:VyperParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#multipleassign.
    def visitMultipleassign(self, ctx:VyperParser.MultipleassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#assign.
    def visitAssign(self, ctx:VyperParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#augoperator.
    def visitAugoperator(self, ctx:VyperParser.AugoperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#augassign.
    def visitAugassign(self, ctx:VyperParser.AugassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#passstmt.
    def visitPassstmt(self, ctx:VyperParser.PassstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#breakstmt.
    def visitBreakstmt(self, ctx:VyperParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#continuestmt.
    def visitContinuestmt(self, ctx:VyperParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#logstmt.
    def visitLogstmt(self, ctx:VyperParser.LogstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#returnstmt.
    def visitReturnstmt(self, ctx:VyperParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#raisestmt.
    def visitRaisestmt(self, ctx:VyperParser.RaisestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#assertstmt.
    def visitAssertstmt(self, ctx:VyperParser.AssertstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#condexec.
    def visitCondexec(self, ctx:VyperParser.CondexecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#defaultexec.
    def visitDefaultexec(self, ctx:VyperParser.DefaultexecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#ifstmt.
    def visitIfstmt(self, ctx:VyperParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#loopvariable.
    def visitLoopvariable(self, ctx:VyperParser.LoopvariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#loopiterator.
    def visitLoopiterator(self, ctx:VyperParser.LoopiteratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#forstmt.
    def visitForstmt(self, ctx:VyperParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#expr.
    def visitExpr(self, ctx:VyperParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#variableaccess.
    def visitVariableaccess(self, ctx:VyperParser.VariableaccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#getattr.
    def visitGetattr(self, ctx:VyperParser.GetattrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#getitem.
    def visitGetitem(self, ctx:VyperParser.GetitemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#call.
    def visitCall(self, ctx:VyperParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#arg.
    def visitArg(self, ctx:VyperParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#kwarg.
    def visitKwarg(self, ctx:VyperParser.KwargContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#argument.
    def visitArgument(self, ctx:VyperParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#arguments.
    def visitArguments(self, ctx:VyperParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#tuple.
    def visitTuple(self, ctx:VyperParser.TupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#list.
    def visitList(self, ctx:VyperParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#dict.
    def visitDict(self, ctx:VyperParser.DictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#operation.
    def visitOperation(self, ctx:VyperParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#boolor.
    def visitBoolor(self, ctx:VyperParser.BoolorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#booland.
    def visitBooland(self, ctx:VyperParser.BoolandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#boolnot.
    def visitBoolnot(self, ctx:VyperParser.BoolnotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#comparator.
    def visitComparator(self, ctx:VyperParser.ComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#bitwiseor.
    def visitBitwiseor(self, ctx:VyperParser.BitwiseorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#bitwisexor.
    def visitBitwisexor(self, ctx:VyperParser.BitwisexorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#bitwiseand.
    def visitBitwiseand(self, ctx:VyperParser.BitwiseandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#shift.
    def visitShift(self, ctx:VyperParser.ShiftContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#summation.
    def visitSummation(self, ctx:VyperParser.SummationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#product.
    def visitProduct(self, ctx:VyperParser.ProductContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#unary.
    def visitUnary(self, ctx:VyperParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#power.
    def visitPower(self, ctx:VyperParser.PowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#empty.
    def visitEmpty(self, ctx:VyperParser.EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#abidecode.
    def visitAbidecode(self, ctx:VyperParser.AbidecodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#specialbuiltins.
    def visitSpecialbuiltins(self, ctx:VyperParser.SpecialbuiltinsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#atom.
    def visitAtom(self, ctx:VyperParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#number.
    def visitNumber(self, ctx:VyperParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#literal.
    def visitLiteral(self, ctx:VyperParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#string.
    def visitString(self, ctx:VyperParser.StringContext):
        return self.visitChildren(ctx)



del VyperParser