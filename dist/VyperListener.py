# Generated from VyperParser.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .VyperParser import VyperParser
else:
    from VyperParser import VyperParser

# This class defines a complete listener for a parse tree produced by VyperParser.
class VyperListener(ParseTreeListener):

    # Enter a parse tree produced by VyperParser#module.
    def enterModule(self, ctx:VyperParser.ModuleContext):
        pass

    # Exit a parse tree produced by VyperParser#module.
    def exitModule(self, ctx:VyperParser.ModuleContext):
        pass


    # Enter a parse tree produced by VyperParser#importname.
    def enterImportname(self, ctx:VyperParser.ImportnameContext):
        pass

    # Exit a parse tree produced by VyperParser#importname.
    def exitImportname(self, ctx:VyperParser.ImportnameContext):
        pass


    # Enter a parse tree produced by VyperParser#importpath.
    def enterImportpath(self, ctx:VyperParser.ImportpathContext):
        pass

    # Exit a parse tree produced by VyperParser#importpath.
    def exitImportpath(self, ctx:VyperParser.ImportpathContext):
        pass


    # Enter a parse tree produced by VyperParser#importalias.
    def enterImportalias(self, ctx:VyperParser.ImportaliasContext):
        pass

    # Exit a parse tree produced by VyperParser#importalias.
    def exitImportalias(self, ctx:VyperParser.ImportaliasContext):
        pass


    # Enter a parse tree produced by VyperParser#importlist.
    def enterImportlist(self, ctx:VyperParser.ImportlistContext):
        pass

    # Exit a parse tree produced by VyperParser#importlist.
    def exitImportlist(self, ctx:VyperParser.ImportlistContext):
        pass


    # Enter a parse tree produced by VyperParser#importfrom.
    def enterImportfrom(self, ctx:VyperParser.ImportfromContext):
        pass

    # Exit a parse tree produced by VyperParser#importfrom.
    def exitImportfrom(self, ctx:VyperParser.ImportfromContext):
        pass


    # Enter a parse tree produced by VyperParser#import_.
    def enterImport_(self, ctx:VyperParser.Import_Context):
        pass

    # Exit a parse tree produced by VyperParser#import_.
    def exitImport_(self, ctx:VyperParser.Import_Context):
        pass


    # Enter a parse tree produced by VyperParser#constantdef.
    def enterConstantdef(self, ctx:VyperParser.ConstantdefContext):
        pass

    # Exit a parse tree produced by VyperParser#constantdef.
    def exitConstantdef(self, ctx:VyperParser.ConstantdefContext):
        pass


    # Enter a parse tree produced by VyperParser#immutabledef.
    def enterImmutabledef(self, ctx:VyperParser.ImmutabledefContext):
        pass

    # Exit a parse tree produced by VyperParser#immutabledef.
    def exitImmutabledef(self, ctx:VyperParser.ImmutabledefContext):
        pass


    # Enter a parse tree produced by VyperParser#variable.
    def enterVariable(self, ctx:VyperParser.VariableContext):
        pass

    # Exit a parse tree produced by VyperParser#variable.
    def exitVariable(self, ctx:VyperParser.VariableContext):
        pass


    # Enter a parse tree produced by VyperParser#variablewithgetter.
    def enterVariablewithgetter(self, ctx:VyperParser.VariablewithgetterContext):
        pass

    # Exit a parse tree produced by VyperParser#variablewithgetter.
    def exitVariablewithgetter(self, ctx:VyperParser.VariablewithgetterContext):
        pass


    # Enter a parse tree produced by VyperParser#variabledef.
    def enterVariabledef(self, ctx:VyperParser.VariabledefContext):
        pass

    # Exit a parse tree produced by VyperParser#variabledef.
    def exitVariabledef(self, ctx:VyperParser.VariabledefContext):
        pass


    # Enter a parse tree produced by VyperParser#decorator.
    def enterDecorator(self, ctx:VyperParser.DecoratorContext):
        pass

    # Exit a parse tree produced by VyperParser#decorator.
    def exitDecorator(self, ctx:VyperParser.DecoratorContext):
        pass


    # Enter a parse tree produced by VyperParser#decorators.
    def enterDecorators(self, ctx:VyperParser.DecoratorsContext):
        pass

    # Exit a parse tree produced by VyperParser#decorators.
    def exitDecorators(self, ctx:VyperParser.DecoratorsContext):
        pass


    # Enter a parse tree produced by VyperParser#parameter.
    def enterParameter(self, ctx:VyperParser.ParameterContext):
        pass

    # Exit a parse tree produced by VyperParser#parameter.
    def exitParameter(self, ctx:VyperParser.ParameterContext):
        pass


    # Enter a parse tree produced by VyperParser#parameters.
    def enterParameters(self, ctx:VyperParser.ParametersContext):
        pass

    # Exit a parse tree produced by VyperParser#parameters.
    def exitParameters(self, ctx:VyperParser.ParametersContext):
        pass


    # Enter a parse tree produced by VyperParser#returns_.
    def enterReturns_(self, ctx:VyperParser.Returns_Context):
        pass

    # Exit a parse tree produced by VyperParser#returns_.
    def exitReturns_(self, ctx:VyperParser.Returns_Context):
        pass


    # Enter a parse tree produced by VyperParser#functionsig.
    def enterFunctionsig(self, ctx:VyperParser.FunctionsigContext):
        pass

    # Exit a parse tree produced by VyperParser#functionsig.
    def exitFunctionsig(self, ctx:VyperParser.FunctionsigContext):
        pass


    # Enter a parse tree produced by VyperParser#functiondef.
    def enterFunctiondef(self, ctx:VyperParser.FunctiondefContext):
        pass

    # Exit a parse tree produced by VyperParser#functiondef.
    def exitFunctiondef(self, ctx:VyperParser.FunctiondefContext):
        pass


    # Enter a parse tree produced by VyperParser#eventmember.
    def enterEventmember(self, ctx:VyperParser.EventmemberContext):
        pass

    # Exit a parse tree produced by VyperParser#eventmember.
    def exitEventmember(self, ctx:VyperParser.EventmemberContext):
        pass


    # Enter a parse tree produced by VyperParser#indexedeventarg.
    def enterIndexedeventarg(self, ctx:VyperParser.IndexedeventargContext):
        pass

    # Exit a parse tree produced by VyperParser#indexedeventarg.
    def exitIndexedeventarg(self, ctx:VyperParser.IndexedeventargContext):
        pass


    # Enter a parse tree produced by VyperParser#eventbody.
    def enterEventbody(self, ctx:VyperParser.EventbodyContext):
        pass

    # Exit a parse tree produced by VyperParser#eventbody.
    def exitEventbody(self, ctx:VyperParser.EventbodyContext):
        pass


    # Enter a parse tree produced by VyperParser#eventdef.
    def enterEventdef(self, ctx:VyperParser.EventdefContext):
        pass

    # Exit a parse tree produced by VyperParser#eventdef.
    def exitEventdef(self, ctx:VyperParser.EventdefContext):
        pass


    # Enter a parse tree produced by VyperParser#enummember.
    def enterEnummember(self, ctx:VyperParser.EnummemberContext):
        pass

    # Exit a parse tree produced by VyperParser#enummember.
    def exitEnummember(self, ctx:VyperParser.EnummemberContext):
        pass


    # Enter a parse tree produced by VyperParser#enumbody.
    def enterEnumbody(self, ctx:VyperParser.EnumbodyContext):
        pass

    # Exit a parse tree produced by VyperParser#enumbody.
    def exitEnumbody(self, ctx:VyperParser.EnumbodyContext):
        pass


    # Enter a parse tree produced by VyperParser#enumdef.
    def enterEnumdef(self, ctx:VyperParser.EnumdefContext):
        pass

    # Exit a parse tree produced by VyperParser#enumdef.
    def exitEnumdef(self, ctx:VyperParser.EnumdefContext):
        pass


    # Enter a parse tree produced by VyperParser#arraydef.
    def enterArraydef(self, ctx:VyperParser.ArraydefContext):
        pass

    # Exit a parse tree produced by VyperParser#arraydef.
    def exitArraydef(self, ctx:VyperParser.ArraydefContext):
        pass


    # Enter a parse tree produced by VyperParser#simple_arraydef.
    def enterSimple_arraydef(self, ctx:VyperParser.Simple_arraydefContext):
        pass

    # Exit a parse tree produced by VyperParser#simple_arraydef.
    def exitSimple_arraydef(self, ctx:VyperParser.Simple_arraydefContext):
        pass


    # Enter a parse tree produced by VyperParser#dynarraydef.
    def enterDynarraydef(self, ctx:VyperParser.DynarraydefContext):
        pass

    # Exit a parse tree produced by VyperParser#dynarraydef.
    def exitDynarraydef(self, ctx:VyperParser.DynarraydefContext):
        pass


    # Enter a parse tree produced by VyperParser#index.
    def enterIndex(self, ctx:VyperParser.IndexContext):
        pass

    # Exit a parse tree produced by VyperParser#index.
    def exitIndex(self, ctx:VyperParser.IndexContext):
        pass


    # Enter a parse tree produced by VyperParser#dynindex.
    def enterDynindex(self, ctx:VyperParser.DynindexContext):
        pass

    # Exit a parse tree produced by VyperParser#dynindex.
    def exitDynindex(self, ctx:VyperParser.DynindexContext):
        pass


    # Enter a parse tree produced by VyperParser#tupledef.
    def enterTupledef(self, ctx:VyperParser.TupledefContext):
        pass

    # Exit a parse tree produced by VyperParser#tupledef.
    def exitTupledef(self, ctx:VyperParser.TupledefContext):
        pass


    # Enter a parse tree produced by VyperParser#mapdef.
    def enterMapdef(self, ctx:VyperParser.MapdefContext):
        pass

    # Exit a parse tree produced by VyperParser#mapdef.
    def exitMapdef(self, ctx:VyperParser.MapdefContext):
        pass


    # Enter a parse tree produced by VyperParser#type_.
    def enterType_(self, ctx:VyperParser.Type_Context):
        pass

    # Exit a parse tree produced by VyperParser#type_.
    def exitType_(self, ctx:VyperParser.Type_Context):
        pass


    # Enter a parse tree produced by VyperParser#structmember.
    def enterStructmember(self, ctx:VyperParser.StructmemberContext):
        pass

    # Exit a parse tree produced by VyperParser#structmember.
    def exitStructmember(self, ctx:VyperParser.StructmemberContext):
        pass


    # Enter a parse tree produced by VyperParser#structdef.
    def enterStructdef(self, ctx:VyperParser.StructdefContext):
        pass

    # Exit a parse tree produced by VyperParser#structdef.
    def exitStructdef(self, ctx:VyperParser.StructdefContext):
        pass


    # Enter a parse tree produced by VyperParser#mutability.
    def enterMutability(self, ctx:VyperParser.MutabilityContext):
        pass

    # Exit a parse tree produced by VyperParser#mutability.
    def exitMutability(self, ctx:VyperParser.MutabilityContext):
        pass


    # Enter a parse tree produced by VyperParser#interfacefunction.
    def enterInterfacefunction(self, ctx:VyperParser.InterfacefunctionContext):
        pass

    # Exit a parse tree produced by VyperParser#interfacefunction.
    def exitInterfacefunction(self, ctx:VyperParser.InterfacefunctionContext):
        pass


    # Enter a parse tree produced by VyperParser#interfacedef.
    def enterInterfacedef(self, ctx:VyperParser.InterfacedefContext):
        pass

    # Exit a parse tree produced by VyperParser#interfacedef.
    def exitInterfacedef(self, ctx:VyperParser.InterfacedefContext):
        pass


    # Enter a parse tree produced by VyperParser#stmt.
    def enterStmt(self, ctx:VyperParser.StmtContext):
        pass

    # Exit a parse tree produced by VyperParser#stmt.
    def exitStmt(self, ctx:VyperParser.StmtContext):
        pass


    # Enter a parse tree produced by VyperParser#declaration.
    def enterDeclaration(self, ctx:VyperParser.DeclarationContext):
        pass

    # Exit a parse tree produced by VyperParser#declaration.
    def exitDeclaration(self, ctx:VyperParser.DeclarationContext):
        pass


    # Enter a parse tree produced by VyperParser#multipleassign.
    def enterMultipleassign(self, ctx:VyperParser.MultipleassignContext):
        pass

    # Exit a parse tree produced by VyperParser#multipleassign.
    def exitMultipleassign(self, ctx:VyperParser.MultipleassignContext):
        pass


    # Enter a parse tree produced by VyperParser#assign.
    def enterAssign(self, ctx:VyperParser.AssignContext):
        pass

    # Exit a parse tree produced by VyperParser#assign.
    def exitAssign(self, ctx:VyperParser.AssignContext):
        pass


    # Enter a parse tree produced by VyperParser#augoperator.
    def enterAugoperator(self, ctx:VyperParser.AugoperatorContext):
        pass

    # Exit a parse tree produced by VyperParser#augoperator.
    def exitAugoperator(self, ctx:VyperParser.AugoperatorContext):
        pass


    # Enter a parse tree produced by VyperParser#augassign.
    def enterAugassign(self, ctx:VyperParser.AugassignContext):
        pass

    # Exit a parse tree produced by VyperParser#augassign.
    def exitAugassign(self, ctx:VyperParser.AugassignContext):
        pass


    # Enter a parse tree produced by VyperParser#passstmt.
    def enterPassstmt(self, ctx:VyperParser.PassstmtContext):
        pass

    # Exit a parse tree produced by VyperParser#passstmt.
    def exitPassstmt(self, ctx:VyperParser.PassstmtContext):
        pass


    # Enter a parse tree produced by VyperParser#breakstmt.
    def enterBreakstmt(self, ctx:VyperParser.BreakstmtContext):
        pass

    # Exit a parse tree produced by VyperParser#breakstmt.
    def exitBreakstmt(self, ctx:VyperParser.BreakstmtContext):
        pass


    # Enter a parse tree produced by VyperParser#continuestmt.
    def enterContinuestmt(self, ctx:VyperParser.ContinuestmtContext):
        pass

    # Exit a parse tree produced by VyperParser#continuestmt.
    def exitContinuestmt(self, ctx:VyperParser.ContinuestmtContext):
        pass


    # Enter a parse tree produced by VyperParser#logstmt.
    def enterLogstmt(self, ctx:VyperParser.LogstmtContext):
        pass

    # Exit a parse tree produced by VyperParser#logstmt.
    def exitLogstmt(self, ctx:VyperParser.LogstmtContext):
        pass


    # Enter a parse tree produced by VyperParser#returnstmt.
    def enterReturnstmt(self, ctx:VyperParser.ReturnstmtContext):
        pass

    # Exit a parse tree produced by VyperParser#returnstmt.
    def exitReturnstmt(self, ctx:VyperParser.ReturnstmtContext):
        pass


    # Enter a parse tree produced by VyperParser#raisestmt.
    def enterRaisestmt(self, ctx:VyperParser.RaisestmtContext):
        pass

    # Exit a parse tree produced by VyperParser#raisestmt.
    def exitRaisestmt(self, ctx:VyperParser.RaisestmtContext):
        pass


    # Enter a parse tree produced by VyperParser#assertstmt.
    def enterAssertstmt(self, ctx:VyperParser.AssertstmtContext):
        pass

    # Exit a parse tree produced by VyperParser#assertstmt.
    def exitAssertstmt(self, ctx:VyperParser.AssertstmtContext):
        pass


    # Enter a parse tree produced by VyperParser#body.
    def enterBody(self, ctx:VyperParser.BodyContext):
        pass

    # Exit a parse tree produced by VyperParser#body.
    def exitBody(self, ctx:VyperParser.BodyContext):
        pass


    # Enter a parse tree produced by VyperParser#condexec.
    def enterCondexec(self, ctx:VyperParser.CondexecContext):
        pass

    # Exit a parse tree produced by VyperParser#condexec.
    def exitCondexec(self, ctx:VyperParser.CondexecContext):
        pass


    # Enter a parse tree produced by VyperParser#defaultexec.
    def enterDefaultexec(self, ctx:VyperParser.DefaultexecContext):
        pass

    # Exit a parse tree produced by VyperParser#defaultexec.
    def exitDefaultexec(self, ctx:VyperParser.DefaultexecContext):
        pass


    # Enter a parse tree produced by VyperParser#ifstmt.
    def enterIfstmt(self, ctx:VyperParser.IfstmtContext):
        pass

    # Exit a parse tree produced by VyperParser#ifstmt.
    def exitIfstmt(self, ctx:VyperParser.IfstmtContext):
        pass


    # Enter a parse tree produced by VyperParser#loopvariable.
    def enterLoopvariable(self, ctx:VyperParser.LoopvariableContext):
        pass

    # Exit a parse tree produced by VyperParser#loopvariable.
    def exitLoopvariable(self, ctx:VyperParser.LoopvariableContext):
        pass


    # Enter a parse tree produced by VyperParser#loopiterator.
    def enterLoopiterator(self, ctx:VyperParser.LoopiteratorContext):
        pass

    # Exit a parse tree produced by VyperParser#loopiterator.
    def exitLoopiterator(self, ctx:VyperParser.LoopiteratorContext):
        pass


    # Enter a parse tree produced by VyperParser#forstmt.
    def enterForstmt(self, ctx:VyperParser.ForstmtContext):
        pass

    # Exit a parse tree produced by VyperParser#forstmt.
    def exitForstmt(self, ctx:VyperParser.ForstmtContext):
        pass


    # Enter a parse tree produced by VyperParser#expr.
    def enterExpr(self, ctx:VyperParser.ExprContext):
        pass

    # Exit a parse tree produced by VyperParser#expr.
    def exitExpr(self, ctx:VyperParser.ExprContext):
        pass


    # Enter a parse tree produced by VyperParser#variableaccess.
    def enterVariableaccess(self, ctx:VyperParser.VariableaccessContext):
        pass

    # Exit a parse tree produced by VyperParser#variableaccess.
    def exitVariableaccess(self, ctx:VyperParser.VariableaccessContext):
        pass


    # Enter a parse tree produced by VyperParser#getattr.
    def enterGetattr(self, ctx:VyperParser.GetattrContext):
        pass

    # Exit a parse tree produced by VyperParser#getattr.
    def exitGetattr(self, ctx:VyperParser.GetattrContext):
        pass


    # Enter a parse tree produced by VyperParser#getitem.
    def enterGetitem(self, ctx:VyperParser.GetitemContext):
        pass

    # Exit a parse tree produced by VyperParser#getitem.
    def exitGetitem(self, ctx:VyperParser.GetitemContext):
        pass


    # Enter a parse tree produced by VyperParser#call.
    def enterCall(self, ctx:VyperParser.CallContext):
        pass

    # Exit a parse tree produced by VyperParser#call.
    def exitCall(self, ctx:VyperParser.CallContext):
        pass


    # Enter a parse tree produced by VyperParser#arg.
    def enterArg(self, ctx:VyperParser.ArgContext):
        pass

    # Exit a parse tree produced by VyperParser#arg.
    def exitArg(self, ctx:VyperParser.ArgContext):
        pass


    # Enter a parse tree produced by VyperParser#kwarg.
    def enterKwarg(self, ctx:VyperParser.KwargContext):
        pass

    # Exit a parse tree produced by VyperParser#kwarg.
    def exitKwarg(self, ctx:VyperParser.KwargContext):
        pass


    # Enter a parse tree produced by VyperParser#argument.
    def enterArgument(self, ctx:VyperParser.ArgumentContext):
        pass

    # Exit a parse tree produced by VyperParser#argument.
    def exitArgument(self, ctx:VyperParser.ArgumentContext):
        pass


    # Enter a parse tree produced by VyperParser#arguments.
    def enterArguments(self, ctx:VyperParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by VyperParser#arguments.
    def exitArguments(self, ctx:VyperParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by VyperParser#tuple.
    def enterTuple(self, ctx:VyperParser.TupleContext):
        pass

    # Exit a parse tree produced by VyperParser#tuple.
    def exitTuple(self, ctx:VyperParser.TupleContext):
        pass


    # Enter a parse tree produced by VyperParser#list.
    def enterList(self, ctx:VyperParser.ListContext):
        pass

    # Exit a parse tree produced by VyperParser#list.
    def exitList(self, ctx:VyperParser.ListContext):
        pass


    # Enter a parse tree produced by VyperParser#dict.
    def enterDict(self, ctx:VyperParser.DictContext):
        pass

    # Exit a parse tree produced by VyperParser#dict.
    def exitDict(self, ctx:VyperParser.DictContext):
        pass


    # Enter a parse tree produced by VyperParser#operation.
    def enterOperation(self, ctx:VyperParser.OperationContext):
        pass

    # Exit a parse tree produced by VyperParser#operation.
    def exitOperation(self, ctx:VyperParser.OperationContext):
        pass


    # Enter a parse tree produced by VyperParser#boolor.
    def enterBoolor(self, ctx:VyperParser.BoolorContext):
        pass

    # Exit a parse tree produced by VyperParser#boolor.
    def exitBoolor(self, ctx:VyperParser.BoolorContext):
        pass


    # Enter a parse tree produced by VyperParser#booland.
    def enterBooland(self, ctx:VyperParser.BoolandContext):
        pass

    # Exit a parse tree produced by VyperParser#booland.
    def exitBooland(self, ctx:VyperParser.BoolandContext):
        pass


    # Enter a parse tree produced by VyperParser#boolnot.
    def enterBoolnot(self, ctx:VyperParser.BoolnotContext):
        pass

    # Exit a parse tree produced by VyperParser#boolnot.
    def exitBoolnot(self, ctx:VyperParser.BoolnotContext):
        pass


    # Enter a parse tree produced by VyperParser#comparator.
    def enterComparator(self, ctx:VyperParser.ComparatorContext):
        pass

    # Exit a parse tree produced by VyperParser#comparator.
    def exitComparator(self, ctx:VyperParser.ComparatorContext):
        pass


    # Enter a parse tree produced by VyperParser#bitwiseor.
    def enterBitwiseor(self, ctx:VyperParser.BitwiseorContext):
        pass

    # Exit a parse tree produced by VyperParser#bitwiseor.
    def exitBitwiseor(self, ctx:VyperParser.BitwiseorContext):
        pass


    # Enter a parse tree produced by VyperParser#bitwisexor.
    def enterBitwisexor(self, ctx:VyperParser.BitwisexorContext):
        pass

    # Exit a parse tree produced by VyperParser#bitwisexor.
    def exitBitwisexor(self, ctx:VyperParser.BitwisexorContext):
        pass


    # Enter a parse tree produced by VyperParser#bitwiseand.
    def enterBitwiseand(self, ctx:VyperParser.BitwiseandContext):
        pass

    # Exit a parse tree produced by VyperParser#bitwiseand.
    def exitBitwiseand(self, ctx:VyperParser.BitwiseandContext):
        pass


    # Enter a parse tree produced by VyperParser#shift.
    def enterShift(self, ctx:VyperParser.ShiftContext):
        pass

    # Exit a parse tree produced by VyperParser#shift.
    def exitShift(self, ctx:VyperParser.ShiftContext):
        pass


    # Enter a parse tree produced by VyperParser#summation.
    def enterSummation(self, ctx:VyperParser.SummationContext):
        pass

    # Exit a parse tree produced by VyperParser#summation.
    def exitSummation(self, ctx:VyperParser.SummationContext):
        pass


    # Enter a parse tree produced by VyperParser#product.
    def enterProduct(self, ctx:VyperParser.ProductContext):
        pass

    # Exit a parse tree produced by VyperParser#product.
    def exitProduct(self, ctx:VyperParser.ProductContext):
        pass


    # Enter a parse tree produced by VyperParser#unary.
    def enterUnary(self, ctx:VyperParser.UnaryContext):
        pass

    # Exit a parse tree produced by VyperParser#unary.
    def exitUnary(self, ctx:VyperParser.UnaryContext):
        pass


    # Enter a parse tree produced by VyperParser#power.
    def enterPower(self, ctx:VyperParser.PowerContext):
        pass

    # Exit a parse tree produced by VyperParser#power.
    def exitPower(self, ctx:VyperParser.PowerContext):
        pass


    # Enter a parse tree produced by VyperParser#empty.
    def enterEmpty(self, ctx:VyperParser.EmptyContext):
        pass

    # Exit a parse tree produced by VyperParser#empty.
    def exitEmpty(self, ctx:VyperParser.EmptyContext):
        pass


    # Enter a parse tree produced by VyperParser#abidecode.
    def enterAbidecode(self, ctx:VyperParser.AbidecodeContext):
        pass

    # Exit a parse tree produced by VyperParser#abidecode.
    def exitAbidecode(self, ctx:VyperParser.AbidecodeContext):
        pass


    # Enter a parse tree produced by VyperParser#specialbuiltins.
    def enterSpecialbuiltins(self, ctx:VyperParser.SpecialbuiltinsContext):
        pass

    # Exit a parse tree produced by VyperParser#specialbuiltins.
    def exitSpecialbuiltins(self, ctx:VyperParser.SpecialbuiltinsContext):
        pass


    # Enter a parse tree produced by VyperParser#atom.
    def enterAtom(self, ctx:VyperParser.AtomContext):
        pass

    # Exit a parse tree produced by VyperParser#atom.
    def exitAtom(self, ctx:VyperParser.AtomContext):
        pass


    # Enter a parse tree produced by VyperParser#number.
    def enterNumber(self, ctx:VyperParser.NumberContext):
        pass

    # Exit a parse tree produced by VyperParser#number.
    def exitNumber(self, ctx:VyperParser.NumberContext):
        pass


    # Enter a parse tree produced by VyperParser#literal.
    def enterLiteral(self, ctx:VyperParser.LiteralContext):
        pass

    # Exit a parse tree produced by VyperParser#literal.
    def exitLiteral(self, ctx:VyperParser.LiteralContext):
        pass



del VyperParser