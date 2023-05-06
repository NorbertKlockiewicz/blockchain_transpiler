# Generated from Erlang.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ErlangParser import ErlangParser
else:
    from ErlangParser import ErlangParser

# This class defines a complete generic visitor for a parse tree produced by ErlangParser.

class ErlangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ErlangParser#forms.
    def visitForms(self, ctx:ErlangParser.FormsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#form.
    def visitForm(self, ctx:ErlangParser.FormContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#tokAtom.
    def visitTokAtom(self, ctx:ErlangParser.TokAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#tokVar.
    def visitTokVar(self, ctx:ErlangParser.TokVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#tokFloat.
    def visitTokFloat(self, ctx:ErlangParser.TokFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#tokInteger.
    def visitTokInteger(self, ctx:ErlangParser.TokIntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#tokChar.
    def visitTokChar(self, ctx:ErlangParser.TokCharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#tokString.
    def visitTokString(self, ctx:ErlangParser.TokStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#attribute.
    def visitAttribute(self, ctx:ErlangParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#typeSpec.
    def visitTypeSpec(self, ctx:ErlangParser.TypeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#specFun.
    def visitSpecFun(self, ctx:ErlangParser.SpecFunContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#typedAttrVal.
    def visitTypedAttrVal(self, ctx:ErlangParser.TypedAttrValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#typedRecordFields.
    def visitTypedRecordFields(self, ctx:ErlangParser.TypedRecordFieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#typedExprs.
    def visitTypedExprs(self, ctx:ErlangParser.TypedExprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#typedExpr.
    def visitTypedExpr(self, ctx:ErlangParser.TypedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#typeSigs.
    def visitTypeSigs(self, ctx:ErlangParser.TypeSigsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#typeSig.
    def visitTypeSig(self, ctx:ErlangParser.TypeSigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#typeGuards.
    def visitTypeGuards(self, ctx:ErlangParser.TypeGuardsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#typeGuard.
    def visitTypeGuard(self, ctx:ErlangParser.TypeGuardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#topTypes.
    def visitTopTypes(self, ctx:ErlangParser.TopTypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#topType.
    def visitTopType(self, ctx:ErlangParser.TopTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#topType100.
    def visitTopType100(self, ctx:ErlangParser.TopType100Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#type200.
    def visitType200(self, ctx:ErlangParser.Type200Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#type300.
    def visitType300(self, ctx:ErlangParser.Type300Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#type400.
    def visitType400(self, ctx:ErlangParser.Type400Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#type500.
    def visitType500(self, ctx:ErlangParser.Type500Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#type_.
    def visitType_(self, ctx:ErlangParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#funType100.
    def visitFunType100(self, ctx:ErlangParser.FunType100Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#funType.
    def visitFunType(self, ctx:ErlangParser.FunTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#mapPairTypes.
    def visitMapPairTypes(self, ctx:ErlangParser.MapPairTypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#mapPairType.
    def visitMapPairType(self, ctx:ErlangParser.MapPairTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#fieldTypes.
    def visitFieldTypes(self, ctx:ErlangParser.FieldTypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#fieldType.
    def visitFieldType(self, ctx:ErlangParser.FieldTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#binaryType.
    def visitBinaryType(self, ctx:ErlangParser.BinaryTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#binBaseType.
    def visitBinBaseType(self, ctx:ErlangParser.BinBaseTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#binUnitType.
    def visitBinUnitType(self, ctx:ErlangParser.BinUnitTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#attrVal.
    def visitAttrVal(self, ctx:ErlangParser.AttrValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#function_.
    def visitFunction_(self, ctx:ErlangParser.Function_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#functionClause.
    def visitFunctionClause(self, ctx:ErlangParser.FunctionClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#clauseArgs.
    def visitClauseArgs(self, ctx:ErlangParser.ClauseArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#clauseGuard.
    def visitClauseGuard(self, ctx:ErlangParser.ClauseGuardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#clauseBody.
    def visitClauseBody(self, ctx:ErlangParser.ClauseBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#expr.
    def visitExpr(self, ctx:ErlangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#expr100.
    def visitExpr100(self, ctx:ErlangParser.Expr100Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#expr150.
    def visitExpr150(self, ctx:ErlangParser.Expr150Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#expr160.
    def visitExpr160(self, ctx:ErlangParser.Expr160Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#expr200.
    def visitExpr200(self, ctx:ErlangParser.Expr200Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#expr300.
    def visitExpr300(self, ctx:ErlangParser.Expr300Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#expr400.
    def visitExpr400(self, ctx:ErlangParser.Expr400Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#expr500.
    def visitExpr500(self, ctx:ErlangParser.Expr500Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#expr600.
    def visitExpr600(self, ctx:ErlangParser.Expr600Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#expr650.
    def visitExpr650(self, ctx:ErlangParser.Expr650Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#expr700.
    def visitExpr700(self, ctx:ErlangParser.Expr700Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#expr800.
    def visitExpr800(self, ctx:ErlangParser.Expr800Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#exprMax.
    def visitExprMax(self, ctx:ErlangParser.ExprMaxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#patExpr.
    def visitPatExpr(self, ctx:ErlangParser.PatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#patExpr200.
    def visitPatExpr200(self, ctx:ErlangParser.PatExpr200Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#patExpr300.
    def visitPatExpr300(self, ctx:ErlangParser.PatExpr300Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#patExpr400.
    def visitPatExpr400(self, ctx:ErlangParser.PatExpr400Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#patExpr500.
    def visitPatExpr500(self, ctx:ErlangParser.PatExpr500Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#patExpr600.
    def visitPatExpr600(self, ctx:ErlangParser.PatExpr600Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#patExpr650.
    def visitPatExpr650(self, ctx:ErlangParser.PatExpr650Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#patExpr700.
    def visitPatExpr700(self, ctx:ErlangParser.PatExpr700Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#patExpr800.
    def visitPatExpr800(self, ctx:ErlangParser.PatExpr800Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#patExprMax.
    def visitPatExprMax(self, ctx:ErlangParser.PatExprMaxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#mapPatExpr.
    def visitMapPatExpr(self, ctx:ErlangParser.MapPatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#recordPatExpr.
    def visitRecordPatExpr(self, ctx:ErlangParser.RecordPatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#list_.
    def visitList_(self, ctx:ErlangParser.List_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#tail.
    def visitTail(self, ctx:ErlangParser.TailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#binary.
    def visitBinary(self, ctx:ErlangParser.BinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#binElements.
    def visitBinElements(self, ctx:ErlangParser.BinElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#binElement.
    def visitBinElement(self, ctx:ErlangParser.BinElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#bitExpr.
    def visitBitExpr(self, ctx:ErlangParser.BitExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#optBitSizeExpr.
    def visitOptBitSizeExpr(self, ctx:ErlangParser.OptBitSizeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#optBitTypeList.
    def visitOptBitTypeList(self, ctx:ErlangParser.OptBitTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#bitTypeList.
    def visitBitTypeList(self, ctx:ErlangParser.BitTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#bitType.
    def visitBitType(self, ctx:ErlangParser.BitTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#bitSizeExpr.
    def visitBitSizeExpr(self, ctx:ErlangParser.BitSizeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#listComprehension.
    def visitListComprehension(self, ctx:ErlangParser.ListComprehensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#binaryComprehension.
    def visitBinaryComprehension(self, ctx:ErlangParser.BinaryComprehensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#lcExprs.
    def visitLcExprs(self, ctx:ErlangParser.LcExprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#lcExpr.
    def visitLcExpr(self, ctx:ErlangParser.LcExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#tuple_.
    def visitTuple_(self, ctx:ErlangParser.Tuple_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#mapExpr.
    def visitMapExpr(self, ctx:ErlangParser.MapExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#mapTuple.
    def visitMapTuple(self, ctx:ErlangParser.MapTupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#mapField.
    def visitMapField(self, ctx:ErlangParser.MapFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#mapFieldAssoc.
    def visitMapFieldAssoc(self, ctx:ErlangParser.MapFieldAssocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#mapFieldExact.
    def visitMapFieldExact(self, ctx:ErlangParser.MapFieldExactContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#mapKey.
    def visitMapKey(self, ctx:ErlangParser.MapKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#recordExpr.
    def visitRecordExpr(self, ctx:ErlangParser.RecordExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#recordTuple.
    def visitRecordTuple(self, ctx:ErlangParser.RecordTupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#recordFields.
    def visitRecordFields(self, ctx:ErlangParser.RecordFieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#recordField.
    def visitRecordField(self, ctx:ErlangParser.RecordFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#functionCall.
    def visitFunctionCall(self, ctx:ErlangParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#ifExpr.
    def visitIfExpr(self, ctx:ErlangParser.IfExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#ifClauses.
    def visitIfClauses(self, ctx:ErlangParser.IfClausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#ifClause.
    def visitIfClause(self, ctx:ErlangParser.IfClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#caseExpr.
    def visitCaseExpr(self, ctx:ErlangParser.CaseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#crClauses.
    def visitCrClauses(self, ctx:ErlangParser.CrClausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#crClause.
    def visitCrClause(self, ctx:ErlangParser.CrClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#receiveExpr.
    def visitReceiveExpr(self, ctx:ErlangParser.ReceiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#funExpr.
    def visitFunExpr(self, ctx:ErlangParser.FunExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#atomOrVar.
    def visitAtomOrVar(self, ctx:ErlangParser.AtomOrVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#integerOrVar.
    def visitIntegerOrVar(self, ctx:ErlangParser.IntegerOrVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#funClauses.
    def visitFunClauses(self, ctx:ErlangParser.FunClausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#funClause.
    def visitFunClause(self, ctx:ErlangParser.FunClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#tryExpr.
    def visitTryExpr(self, ctx:ErlangParser.TryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#tryCatch.
    def visitTryCatch(self, ctx:ErlangParser.TryCatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#tryClauses.
    def visitTryClauses(self, ctx:ErlangParser.TryClausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#tryClause.
    def visitTryClause(self, ctx:ErlangParser.TryClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#tryOptStackTrace.
    def visitTryOptStackTrace(self, ctx:ErlangParser.TryOptStackTraceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#argumentList.
    def visitArgumentList(self, ctx:ErlangParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#patArgumentList.
    def visitPatArgumentList(self, ctx:ErlangParser.PatArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#exprs.
    def visitExprs(self, ctx:ErlangParser.ExprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#patExprs.
    def visitPatExprs(self, ctx:ErlangParser.PatExprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#guard_.
    def visitGuard_(self, ctx:ErlangParser.Guard_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#atomic.
    def visitAtomic(self, ctx:ErlangParser.AtomicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#prefixOp.
    def visitPrefixOp(self, ctx:ErlangParser.PrefixOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#multOp.
    def visitMultOp(self, ctx:ErlangParser.MultOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#addOp.
    def visitAddOp(self, ctx:ErlangParser.AddOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#listOp.
    def visitListOp(self, ctx:ErlangParser.ListOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ErlangParser#compOp.
    def visitCompOp(self, ctx:ErlangParser.CompOpContext):
        return self.visitChildren(ctx)



del ErlangParser