# Generated from Vyper.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .VyperParser import VyperParser
else:
    from VyperParser import VyperParser

# This class defines a complete generic visitor for a parse tree produced by VyperParser.

class VyperVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by VyperParser#single_input.
    def visitSingle_input(self, ctx:VyperParser.Single_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#file_input.
    def visitFile_input(self, ctx:VyperParser.File_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#eval_input.
    def visitEval_input(self, ctx:VyperParser.Eval_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#decorator.
    def visitDecorator(self, ctx:VyperParser.DecoratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#decorators.
    def visitDecorators(self, ctx:VyperParser.DecoratorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#decorated.
    def visitDecorated(self, ctx:VyperParser.DecoratedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#funcdef.
    def visitFuncdef(self, ctx:VyperParser.FuncdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#parameters.
    def visitParameters(self, ctx:VyperParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#typedargslist.
    def visitTypedargslist(self, ctx:VyperParser.TypedargslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#tfpdef.
    def visitTfpdef(self, ctx:VyperParser.TfpdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#varargslist.
    def visitVarargslist(self, ctx:VyperParser.VarargslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#vfpdef.
    def visitVfpdef(self, ctx:VyperParser.VfpdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#stmt.
    def visitStmt(self, ctx:VyperParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#simple_stmt.
    def visitSimple_stmt(self, ctx:VyperParser.Simple_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#small_stmt.
    def visitSmall_stmt(self, ctx:VyperParser.Small_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#expr_stmt.
    def visitExpr_stmt(self, ctx:VyperParser.Expr_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#testlist_star_expr.
    def visitTestlist_star_expr(self, ctx:VyperParser.Testlist_star_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#augassign.
    def visitAugassign(self, ctx:VyperParser.AugassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#del_stmt.
    def visitDel_stmt(self, ctx:VyperParser.Del_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#pass_stmt.
    def visitPass_stmt(self, ctx:VyperParser.Pass_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#flow_stmt.
    def visitFlow_stmt(self, ctx:VyperParser.Flow_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#break_stmt.
    def visitBreak_stmt(self, ctx:VyperParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#continue_stmt.
    def visitContinue_stmt(self, ctx:VyperParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#return_stmt.
    def visitReturn_stmt(self, ctx:VyperParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#yield_stmt.
    def visitYield_stmt(self, ctx:VyperParser.Yield_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#raise_stmt.
    def visitRaise_stmt(self, ctx:VyperParser.Raise_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#import_stmt.
    def visitImport_stmt(self, ctx:VyperParser.Import_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#import_name.
    def visitImport_name(self, ctx:VyperParser.Import_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#import_from.
    def visitImport_from(self, ctx:VyperParser.Import_fromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#import_as_name.
    def visitImport_as_name(self, ctx:VyperParser.Import_as_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#dotted_as_name.
    def visitDotted_as_name(self, ctx:VyperParser.Dotted_as_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#import_as_names.
    def visitImport_as_names(self, ctx:VyperParser.Import_as_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#dotted_as_names.
    def visitDotted_as_names(self, ctx:VyperParser.Dotted_as_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#dotted_name.
    def visitDotted_name(self, ctx:VyperParser.Dotted_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#global_stmt.
    def visitGlobal_stmt(self, ctx:VyperParser.Global_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#contract_global_stmt.
    def visitContract_global_stmt(self, ctx:VyperParser.Contract_global_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#nonlocal_stmt.
    def visitNonlocal_stmt(self, ctx:VyperParser.Nonlocal_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#assert_stmt.
    def visitAssert_stmt(self, ctx:VyperParser.Assert_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#compound_stmt.
    def visitCompound_stmt(self, ctx:VyperParser.Compound_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#if_stmt.
    def visitIf_stmt(self, ctx:VyperParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#while_stmt.
    def visitWhile_stmt(self, ctx:VyperParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#for_stmt.
    def visitFor_stmt(self, ctx:VyperParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#try_stmt.
    def visitTry_stmt(self, ctx:VyperParser.Try_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#with_stmt.
    def visitWith_stmt(self, ctx:VyperParser.With_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#with_item.
    def visitWith_item(self, ctx:VyperParser.With_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#except_clause.
    def visitExcept_clause(self, ctx:VyperParser.Except_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#suite.
    def visitSuite(self, ctx:VyperParser.SuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#test.
    def visitTest(self, ctx:VyperParser.TestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#test_nocond.
    def visitTest_nocond(self, ctx:VyperParser.Test_nocondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#lambdef.
    def visitLambdef(self, ctx:VyperParser.LambdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#lambdef_nocond.
    def visitLambdef_nocond(self, ctx:VyperParser.Lambdef_nocondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#or_test.
    def visitOr_test(self, ctx:VyperParser.Or_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#and_test.
    def visitAnd_test(self, ctx:VyperParser.And_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#not_test.
    def visitNot_test(self, ctx:VyperParser.Not_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#comparison.
    def visitComparison(self, ctx:VyperParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#comp_op.
    def visitComp_op(self, ctx:VyperParser.Comp_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#star_expr.
    def visitStar_expr(self, ctx:VyperParser.Star_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#expr.
    def visitExpr(self, ctx:VyperParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#xor_expr.
    def visitXor_expr(self, ctx:VyperParser.Xor_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#and_expr.
    def visitAnd_expr(self, ctx:VyperParser.And_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#shift_expr.
    def visitShift_expr(self, ctx:VyperParser.Shift_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#arith_expr.
    def visitArith_expr(self, ctx:VyperParser.Arith_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#term.
    def visitTerm(self, ctx:VyperParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#factor.
    def visitFactor(self, ctx:VyperParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#power.
    def visitPower(self, ctx:VyperParser.PowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#atom.
    def visitAtom(self, ctx:VyperParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#testlist_comp.
    def visitTestlist_comp(self, ctx:VyperParser.Testlist_compContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#trailer.
    def visitTrailer(self, ctx:VyperParser.TrailerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#subscriptlist.
    def visitSubscriptlist(self, ctx:VyperParser.SubscriptlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#subscript.
    def visitSubscript(self, ctx:VyperParser.SubscriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#sliceop.
    def visitSliceop(self, ctx:VyperParser.SliceopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#exprlist.
    def visitExprlist(self, ctx:VyperParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#testlist.
    def visitTestlist(self, ctx:VyperParser.TestlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#dictorsetmaker.
    def visitDictorsetmaker(self, ctx:VyperParser.DictorsetmakerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#classdef.
    def visitClassdef(self, ctx:VyperParser.ClassdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#arglist.
    def visitArglist(self, ctx:VyperParser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#argument.
    def visitArgument(self, ctx:VyperParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#comp_iter.
    def visitComp_iter(self, ctx:VyperParser.Comp_iterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#comp_for.
    def visitComp_for(self, ctx:VyperParser.Comp_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#comp_if.
    def visitComp_if(self, ctx:VyperParser.Comp_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#yield_expr.
    def visitYield_expr(self, ctx:VyperParser.Yield_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#yield_arg.
    def visitYield_arg(self, ctx:VyperParser.Yield_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#strr.
    def visitStrr(self, ctx:VyperParser.StrrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#number.
    def visitNumber(self, ctx:VyperParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VyperParser#integer.
    def visitInteger(self, ctx:VyperParser.IntegerContext):
        return self.visitChildren(ctx)



del VyperParser