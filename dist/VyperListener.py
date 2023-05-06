# Generated from Vyper.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .VyperParser import VyperParser
else:
    from VyperParser import VyperParser

# This class defines a complete listener for a parse tree produced by VyperParser.
class VyperListener(ParseTreeListener):

    # Enter a parse tree produced by VyperParser#single_input.
    def enterSingle_input(self, ctx:VyperParser.Single_inputContext):
        pass

    # Exit a parse tree produced by VyperParser#single_input.
    def exitSingle_input(self, ctx:VyperParser.Single_inputContext):
        pass


    # Enter a parse tree produced by VyperParser#file_input.
    def enterFile_input(self, ctx:VyperParser.File_inputContext):
        pass

    # Exit a parse tree produced by VyperParser#file_input.
    def exitFile_input(self, ctx:VyperParser.File_inputContext):
        pass


    # Enter a parse tree produced by VyperParser#eval_input.
    def enterEval_input(self, ctx:VyperParser.Eval_inputContext):
        pass

    # Exit a parse tree produced by VyperParser#eval_input.
    def exitEval_input(self, ctx:VyperParser.Eval_inputContext):
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


    # Enter a parse tree produced by VyperParser#decorated.
    def enterDecorated(self, ctx:VyperParser.DecoratedContext):
        pass

    # Exit a parse tree produced by VyperParser#decorated.
    def exitDecorated(self, ctx:VyperParser.DecoratedContext):
        pass


    # Enter a parse tree produced by VyperParser#funcdef.
    def enterFuncdef(self, ctx:VyperParser.FuncdefContext):
        pass

    # Exit a parse tree produced by VyperParser#funcdef.
    def exitFuncdef(self, ctx:VyperParser.FuncdefContext):
        pass


    # Enter a parse tree produced by VyperParser#parameters.
    def enterParameters(self, ctx:VyperParser.ParametersContext):
        pass

    # Exit a parse tree produced by VyperParser#parameters.
    def exitParameters(self, ctx:VyperParser.ParametersContext):
        pass


    # Enter a parse tree produced by VyperParser#typedargslist.
    def enterTypedargslist(self, ctx:VyperParser.TypedargslistContext):
        pass

    # Exit a parse tree produced by VyperParser#typedargslist.
    def exitTypedargslist(self, ctx:VyperParser.TypedargslistContext):
        pass


    # Enter a parse tree produced by VyperParser#tfpdef.
    def enterTfpdef(self, ctx:VyperParser.TfpdefContext):
        pass

    # Exit a parse tree produced by VyperParser#tfpdef.
    def exitTfpdef(self, ctx:VyperParser.TfpdefContext):
        pass


    # Enter a parse tree produced by VyperParser#varargslist.
    def enterVarargslist(self, ctx:VyperParser.VarargslistContext):
        pass

    # Exit a parse tree produced by VyperParser#varargslist.
    def exitVarargslist(self, ctx:VyperParser.VarargslistContext):
        pass


    # Enter a parse tree produced by VyperParser#vfpdef.
    def enterVfpdef(self, ctx:VyperParser.VfpdefContext):
        pass

    # Exit a parse tree produced by VyperParser#vfpdef.
    def exitVfpdef(self, ctx:VyperParser.VfpdefContext):
        pass


    # Enter a parse tree produced by VyperParser#stmt.
    def enterStmt(self, ctx:VyperParser.StmtContext):
        pass

    # Exit a parse tree produced by VyperParser#stmt.
    def exitStmt(self, ctx:VyperParser.StmtContext):
        pass


    # Enter a parse tree produced by VyperParser#simple_stmt.
    def enterSimple_stmt(self, ctx:VyperParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by VyperParser#simple_stmt.
    def exitSimple_stmt(self, ctx:VyperParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by VyperParser#small_stmt.
    def enterSmall_stmt(self, ctx:VyperParser.Small_stmtContext):
        pass

    # Exit a parse tree produced by VyperParser#small_stmt.
    def exitSmall_stmt(self, ctx:VyperParser.Small_stmtContext):
        pass


    # Enter a parse tree produced by VyperParser#expr_stmt.
    def enterExpr_stmt(self, ctx:VyperParser.Expr_stmtContext):
        pass

    # Exit a parse tree produced by VyperParser#expr_stmt.
    def exitExpr_stmt(self, ctx:VyperParser.Expr_stmtContext):
        pass


    # Enter a parse tree produced by VyperParser#testlist_star_expr.
    def enterTestlist_star_expr(self, ctx:VyperParser.Testlist_star_exprContext):
        pass

    # Exit a parse tree produced by VyperParser#testlist_star_expr.
    def exitTestlist_star_expr(self, ctx:VyperParser.Testlist_star_exprContext):
        pass


    # Enter a parse tree produced by VyperParser#augassign.
    def enterAugassign(self, ctx:VyperParser.AugassignContext):
        pass

    # Exit a parse tree produced by VyperParser#augassign.
    def exitAugassign(self, ctx:VyperParser.AugassignContext):
        pass


    # Enter a parse tree produced by VyperParser#del_stmt.
    def enterDel_stmt(self, ctx:VyperParser.Del_stmtContext):
        pass

    # Exit a parse tree produced by VyperParser#del_stmt.
    def exitDel_stmt(self, ctx:VyperParser.Del_stmtContext):
        pass


    # Enter a parse tree produced by VyperParser#pass_stmt.
    def enterPass_stmt(self, ctx:VyperParser.Pass_stmtContext):
        pass

    # Exit a parse tree produced by VyperParser#pass_stmt.
    def exitPass_stmt(self, ctx:VyperParser.Pass_stmtContext):
        pass


    # Enter a parse tree produced by VyperParser#flow_stmt.
    def enterFlow_stmt(self, ctx:VyperParser.Flow_stmtContext):
        pass

    # Exit a parse tree produced by VyperParser#flow_stmt.
    def exitFlow_stmt(self, ctx:VyperParser.Flow_stmtContext):
        pass


    # Enter a parse tree produced by VyperParser#break_stmt.
    def enterBreak_stmt(self, ctx:VyperParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by VyperParser#break_stmt.
    def exitBreak_stmt(self, ctx:VyperParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by VyperParser#continue_stmt.
    def enterContinue_stmt(self, ctx:VyperParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by VyperParser#continue_stmt.
    def exitContinue_stmt(self, ctx:VyperParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by VyperParser#return_stmt.
    def enterReturn_stmt(self, ctx:VyperParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by VyperParser#return_stmt.
    def exitReturn_stmt(self, ctx:VyperParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by VyperParser#yield_stmt.
    def enterYield_stmt(self, ctx:VyperParser.Yield_stmtContext):
        pass

    # Exit a parse tree produced by VyperParser#yield_stmt.
    def exitYield_stmt(self, ctx:VyperParser.Yield_stmtContext):
        pass


    # Enter a parse tree produced by VyperParser#raise_stmt.
    def enterRaise_stmt(self, ctx:VyperParser.Raise_stmtContext):
        pass

    # Exit a parse tree produced by VyperParser#raise_stmt.
    def exitRaise_stmt(self, ctx:VyperParser.Raise_stmtContext):
        pass


    # Enter a parse tree produced by VyperParser#import_stmt.
    def enterImport_stmt(self, ctx:VyperParser.Import_stmtContext):
        pass

    # Exit a parse tree produced by VyperParser#import_stmt.
    def exitImport_stmt(self, ctx:VyperParser.Import_stmtContext):
        pass


    # Enter a parse tree produced by VyperParser#import_name.
    def enterImport_name(self, ctx:VyperParser.Import_nameContext):
        pass

    # Exit a parse tree produced by VyperParser#import_name.
    def exitImport_name(self, ctx:VyperParser.Import_nameContext):
        pass


    # Enter a parse tree produced by VyperParser#import_from.
    def enterImport_from(self, ctx:VyperParser.Import_fromContext):
        pass

    # Exit a parse tree produced by VyperParser#import_from.
    def exitImport_from(self, ctx:VyperParser.Import_fromContext):
        pass


    # Enter a parse tree produced by VyperParser#import_as_name.
    def enterImport_as_name(self, ctx:VyperParser.Import_as_nameContext):
        pass

    # Exit a parse tree produced by VyperParser#import_as_name.
    def exitImport_as_name(self, ctx:VyperParser.Import_as_nameContext):
        pass


    # Enter a parse tree produced by VyperParser#dotted_as_name.
    def enterDotted_as_name(self, ctx:VyperParser.Dotted_as_nameContext):
        pass

    # Exit a parse tree produced by VyperParser#dotted_as_name.
    def exitDotted_as_name(self, ctx:VyperParser.Dotted_as_nameContext):
        pass


    # Enter a parse tree produced by VyperParser#import_as_names.
    def enterImport_as_names(self, ctx:VyperParser.Import_as_namesContext):
        pass

    # Exit a parse tree produced by VyperParser#import_as_names.
    def exitImport_as_names(self, ctx:VyperParser.Import_as_namesContext):
        pass


    # Enter a parse tree produced by VyperParser#dotted_as_names.
    def enterDotted_as_names(self, ctx:VyperParser.Dotted_as_namesContext):
        pass

    # Exit a parse tree produced by VyperParser#dotted_as_names.
    def exitDotted_as_names(self, ctx:VyperParser.Dotted_as_namesContext):
        pass


    # Enter a parse tree produced by VyperParser#dotted_name.
    def enterDotted_name(self, ctx:VyperParser.Dotted_nameContext):
        pass

    # Exit a parse tree produced by VyperParser#dotted_name.
    def exitDotted_name(self, ctx:VyperParser.Dotted_nameContext):
        pass


    # Enter a parse tree produced by VyperParser#global_stmt.
    def enterGlobal_stmt(self, ctx:VyperParser.Global_stmtContext):
        pass

    # Exit a parse tree produced by VyperParser#global_stmt.
    def exitGlobal_stmt(self, ctx:VyperParser.Global_stmtContext):
        pass


    # Enter a parse tree produced by VyperParser#contract_global_stmt.
    def enterContract_global_stmt(self, ctx:VyperParser.Contract_global_stmtContext):
        pass

    # Exit a parse tree produced by VyperParser#contract_global_stmt.
    def exitContract_global_stmt(self, ctx:VyperParser.Contract_global_stmtContext):
        pass


    # Enter a parse tree produced by VyperParser#nonlocal_stmt.
    def enterNonlocal_stmt(self, ctx:VyperParser.Nonlocal_stmtContext):
        pass

    # Exit a parse tree produced by VyperParser#nonlocal_stmt.
    def exitNonlocal_stmt(self, ctx:VyperParser.Nonlocal_stmtContext):
        pass


    # Enter a parse tree produced by VyperParser#assert_stmt.
    def enterAssert_stmt(self, ctx:VyperParser.Assert_stmtContext):
        pass

    # Exit a parse tree produced by VyperParser#assert_stmt.
    def exitAssert_stmt(self, ctx:VyperParser.Assert_stmtContext):
        pass


    # Enter a parse tree produced by VyperParser#compound_stmt.
    def enterCompound_stmt(self, ctx:VyperParser.Compound_stmtContext):
        pass

    # Exit a parse tree produced by VyperParser#compound_stmt.
    def exitCompound_stmt(self, ctx:VyperParser.Compound_stmtContext):
        pass


    # Enter a parse tree produced by VyperParser#if_stmt.
    def enterIf_stmt(self, ctx:VyperParser.If_stmtContext):
        pass

    # Exit a parse tree produced by VyperParser#if_stmt.
    def exitIf_stmt(self, ctx:VyperParser.If_stmtContext):
        pass


    # Enter a parse tree produced by VyperParser#while_stmt.
    def enterWhile_stmt(self, ctx:VyperParser.While_stmtContext):
        pass

    # Exit a parse tree produced by VyperParser#while_stmt.
    def exitWhile_stmt(self, ctx:VyperParser.While_stmtContext):
        pass


    # Enter a parse tree produced by VyperParser#for_stmt.
    def enterFor_stmt(self, ctx:VyperParser.For_stmtContext):
        pass

    # Exit a parse tree produced by VyperParser#for_stmt.
    def exitFor_stmt(self, ctx:VyperParser.For_stmtContext):
        pass


    # Enter a parse tree produced by VyperParser#try_stmt.
    def enterTry_stmt(self, ctx:VyperParser.Try_stmtContext):
        pass

    # Exit a parse tree produced by VyperParser#try_stmt.
    def exitTry_stmt(self, ctx:VyperParser.Try_stmtContext):
        pass


    # Enter a parse tree produced by VyperParser#with_stmt.
    def enterWith_stmt(self, ctx:VyperParser.With_stmtContext):
        pass

    # Exit a parse tree produced by VyperParser#with_stmt.
    def exitWith_stmt(self, ctx:VyperParser.With_stmtContext):
        pass


    # Enter a parse tree produced by VyperParser#with_item.
    def enterWith_item(self, ctx:VyperParser.With_itemContext):
        pass

    # Exit a parse tree produced by VyperParser#with_item.
    def exitWith_item(self, ctx:VyperParser.With_itemContext):
        pass


    # Enter a parse tree produced by VyperParser#except_clause.
    def enterExcept_clause(self, ctx:VyperParser.Except_clauseContext):
        pass

    # Exit a parse tree produced by VyperParser#except_clause.
    def exitExcept_clause(self, ctx:VyperParser.Except_clauseContext):
        pass


    # Enter a parse tree produced by VyperParser#suite.
    def enterSuite(self, ctx:VyperParser.SuiteContext):
        pass

    # Exit a parse tree produced by VyperParser#suite.
    def exitSuite(self, ctx:VyperParser.SuiteContext):
        pass


    # Enter a parse tree produced by VyperParser#test.
    def enterTest(self, ctx:VyperParser.TestContext):
        pass

    # Exit a parse tree produced by VyperParser#test.
    def exitTest(self, ctx:VyperParser.TestContext):
        pass


    # Enter a parse tree produced by VyperParser#test_nocond.
    def enterTest_nocond(self, ctx:VyperParser.Test_nocondContext):
        pass

    # Exit a parse tree produced by VyperParser#test_nocond.
    def exitTest_nocond(self, ctx:VyperParser.Test_nocondContext):
        pass


    # Enter a parse tree produced by VyperParser#lambdef.
    def enterLambdef(self, ctx:VyperParser.LambdefContext):
        pass

    # Exit a parse tree produced by VyperParser#lambdef.
    def exitLambdef(self, ctx:VyperParser.LambdefContext):
        pass


    # Enter a parse tree produced by VyperParser#lambdef_nocond.
    def enterLambdef_nocond(self, ctx:VyperParser.Lambdef_nocondContext):
        pass

    # Exit a parse tree produced by VyperParser#lambdef_nocond.
    def exitLambdef_nocond(self, ctx:VyperParser.Lambdef_nocondContext):
        pass


    # Enter a parse tree produced by VyperParser#or_test.
    def enterOr_test(self, ctx:VyperParser.Or_testContext):
        pass

    # Exit a parse tree produced by VyperParser#or_test.
    def exitOr_test(self, ctx:VyperParser.Or_testContext):
        pass


    # Enter a parse tree produced by VyperParser#and_test.
    def enterAnd_test(self, ctx:VyperParser.And_testContext):
        pass

    # Exit a parse tree produced by VyperParser#and_test.
    def exitAnd_test(self, ctx:VyperParser.And_testContext):
        pass


    # Enter a parse tree produced by VyperParser#not_test.
    def enterNot_test(self, ctx:VyperParser.Not_testContext):
        pass

    # Exit a parse tree produced by VyperParser#not_test.
    def exitNot_test(self, ctx:VyperParser.Not_testContext):
        pass


    # Enter a parse tree produced by VyperParser#comparison.
    def enterComparison(self, ctx:VyperParser.ComparisonContext):
        pass

    # Exit a parse tree produced by VyperParser#comparison.
    def exitComparison(self, ctx:VyperParser.ComparisonContext):
        pass


    # Enter a parse tree produced by VyperParser#comp_op.
    def enterComp_op(self, ctx:VyperParser.Comp_opContext):
        pass

    # Exit a parse tree produced by VyperParser#comp_op.
    def exitComp_op(self, ctx:VyperParser.Comp_opContext):
        pass


    # Enter a parse tree produced by VyperParser#star_expr.
    def enterStar_expr(self, ctx:VyperParser.Star_exprContext):
        pass

    # Exit a parse tree produced by VyperParser#star_expr.
    def exitStar_expr(self, ctx:VyperParser.Star_exprContext):
        pass


    # Enter a parse tree produced by VyperParser#expr.
    def enterExpr(self, ctx:VyperParser.ExprContext):
        pass

    # Exit a parse tree produced by VyperParser#expr.
    def exitExpr(self, ctx:VyperParser.ExprContext):
        pass


    # Enter a parse tree produced by VyperParser#xor_expr.
    def enterXor_expr(self, ctx:VyperParser.Xor_exprContext):
        pass

    # Exit a parse tree produced by VyperParser#xor_expr.
    def exitXor_expr(self, ctx:VyperParser.Xor_exprContext):
        pass


    # Enter a parse tree produced by VyperParser#and_expr.
    def enterAnd_expr(self, ctx:VyperParser.And_exprContext):
        pass

    # Exit a parse tree produced by VyperParser#and_expr.
    def exitAnd_expr(self, ctx:VyperParser.And_exprContext):
        pass


    # Enter a parse tree produced by VyperParser#shift_expr.
    def enterShift_expr(self, ctx:VyperParser.Shift_exprContext):
        pass

    # Exit a parse tree produced by VyperParser#shift_expr.
    def exitShift_expr(self, ctx:VyperParser.Shift_exprContext):
        pass


    # Enter a parse tree produced by VyperParser#arith_expr.
    def enterArith_expr(self, ctx:VyperParser.Arith_exprContext):
        pass

    # Exit a parse tree produced by VyperParser#arith_expr.
    def exitArith_expr(self, ctx:VyperParser.Arith_exprContext):
        pass


    # Enter a parse tree produced by VyperParser#term.
    def enterTerm(self, ctx:VyperParser.TermContext):
        pass

    # Exit a parse tree produced by VyperParser#term.
    def exitTerm(self, ctx:VyperParser.TermContext):
        pass


    # Enter a parse tree produced by VyperParser#factor.
    def enterFactor(self, ctx:VyperParser.FactorContext):
        pass

    # Exit a parse tree produced by VyperParser#factor.
    def exitFactor(self, ctx:VyperParser.FactorContext):
        pass


    # Enter a parse tree produced by VyperParser#power.
    def enterPower(self, ctx:VyperParser.PowerContext):
        pass

    # Exit a parse tree produced by VyperParser#power.
    def exitPower(self, ctx:VyperParser.PowerContext):
        pass


    # Enter a parse tree produced by VyperParser#atom.
    def enterAtom(self, ctx:VyperParser.AtomContext):
        pass

    # Exit a parse tree produced by VyperParser#atom.
    def exitAtom(self, ctx:VyperParser.AtomContext):
        pass


    # Enter a parse tree produced by VyperParser#testlist_comp.
    def enterTestlist_comp(self, ctx:VyperParser.Testlist_compContext):
        pass

    # Exit a parse tree produced by VyperParser#testlist_comp.
    def exitTestlist_comp(self, ctx:VyperParser.Testlist_compContext):
        pass


    # Enter a parse tree produced by VyperParser#trailer.
    def enterTrailer(self, ctx:VyperParser.TrailerContext):
        pass

    # Exit a parse tree produced by VyperParser#trailer.
    def exitTrailer(self, ctx:VyperParser.TrailerContext):
        pass


    # Enter a parse tree produced by VyperParser#subscriptlist.
    def enterSubscriptlist(self, ctx:VyperParser.SubscriptlistContext):
        pass

    # Exit a parse tree produced by VyperParser#subscriptlist.
    def exitSubscriptlist(self, ctx:VyperParser.SubscriptlistContext):
        pass


    # Enter a parse tree produced by VyperParser#subscript.
    def enterSubscript(self, ctx:VyperParser.SubscriptContext):
        pass

    # Exit a parse tree produced by VyperParser#subscript.
    def exitSubscript(self, ctx:VyperParser.SubscriptContext):
        pass


    # Enter a parse tree produced by VyperParser#sliceop.
    def enterSliceop(self, ctx:VyperParser.SliceopContext):
        pass

    # Exit a parse tree produced by VyperParser#sliceop.
    def exitSliceop(self, ctx:VyperParser.SliceopContext):
        pass


    # Enter a parse tree produced by VyperParser#exprlist.
    def enterExprlist(self, ctx:VyperParser.ExprlistContext):
        pass

    # Exit a parse tree produced by VyperParser#exprlist.
    def exitExprlist(self, ctx:VyperParser.ExprlistContext):
        pass


    # Enter a parse tree produced by VyperParser#testlist.
    def enterTestlist(self, ctx:VyperParser.TestlistContext):
        pass

    # Exit a parse tree produced by VyperParser#testlist.
    def exitTestlist(self, ctx:VyperParser.TestlistContext):
        pass


    # Enter a parse tree produced by VyperParser#dictorsetmaker.
    def enterDictorsetmaker(self, ctx:VyperParser.DictorsetmakerContext):
        pass

    # Exit a parse tree produced by VyperParser#dictorsetmaker.
    def exitDictorsetmaker(self, ctx:VyperParser.DictorsetmakerContext):
        pass


    # Enter a parse tree produced by VyperParser#classdef.
    def enterClassdef(self, ctx:VyperParser.ClassdefContext):
        pass

    # Exit a parse tree produced by VyperParser#classdef.
    def exitClassdef(self, ctx:VyperParser.ClassdefContext):
        pass


    # Enter a parse tree produced by VyperParser#arglist.
    def enterArglist(self, ctx:VyperParser.ArglistContext):
        pass

    # Exit a parse tree produced by VyperParser#arglist.
    def exitArglist(self, ctx:VyperParser.ArglistContext):
        pass


    # Enter a parse tree produced by VyperParser#argument.
    def enterArgument(self, ctx:VyperParser.ArgumentContext):
        pass

    # Exit a parse tree produced by VyperParser#argument.
    def exitArgument(self, ctx:VyperParser.ArgumentContext):
        pass


    # Enter a parse tree produced by VyperParser#comp_iter.
    def enterComp_iter(self, ctx:VyperParser.Comp_iterContext):
        pass

    # Exit a parse tree produced by VyperParser#comp_iter.
    def exitComp_iter(self, ctx:VyperParser.Comp_iterContext):
        pass


    # Enter a parse tree produced by VyperParser#comp_for.
    def enterComp_for(self, ctx:VyperParser.Comp_forContext):
        pass

    # Exit a parse tree produced by VyperParser#comp_for.
    def exitComp_for(self, ctx:VyperParser.Comp_forContext):
        pass


    # Enter a parse tree produced by VyperParser#comp_if.
    def enterComp_if(self, ctx:VyperParser.Comp_ifContext):
        pass

    # Exit a parse tree produced by VyperParser#comp_if.
    def exitComp_if(self, ctx:VyperParser.Comp_ifContext):
        pass


    # Enter a parse tree produced by VyperParser#yield_expr.
    def enterYield_expr(self, ctx:VyperParser.Yield_exprContext):
        pass

    # Exit a parse tree produced by VyperParser#yield_expr.
    def exitYield_expr(self, ctx:VyperParser.Yield_exprContext):
        pass


    # Enter a parse tree produced by VyperParser#yield_arg.
    def enterYield_arg(self, ctx:VyperParser.Yield_argContext):
        pass

    # Exit a parse tree produced by VyperParser#yield_arg.
    def exitYield_arg(self, ctx:VyperParser.Yield_argContext):
        pass


    # Enter a parse tree produced by VyperParser#strr.
    def enterStrr(self, ctx:VyperParser.StrrContext):
        pass

    # Exit a parse tree produced by VyperParser#strr.
    def exitStrr(self, ctx:VyperParser.StrrContext):
        pass


    # Enter a parse tree produced by VyperParser#number.
    def enterNumber(self, ctx:VyperParser.NumberContext):
        pass

    # Exit a parse tree produced by VyperParser#number.
    def exitNumber(self, ctx:VyperParser.NumberContext):
        pass


    # Enter a parse tree produced by VyperParser#integer.
    def enterInteger(self, ctx:VyperParser.IntegerContext):
        pass

    # Exit a parse tree produced by VyperParser#integer.
    def exitInteger(self, ctx:VyperParser.IntegerContext):
        pass



del VyperParser