# Generated from Erlang.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ErlangParser import ErlangParser
else:
    from ErlangParser import ErlangParser

# This class defines a complete listener for a parse tree produced by ErlangParser.
class ErlangListener(ParseTreeListener):

    # Enter a parse tree produced by ErlangParser#forms.
    def enterForms(self, ctx:ErlangParser.FormsContext):
        pass

    # Exit a parse tree produced by ErlangParser#forms.
    def exitForms(self, ctx:ErlangParser.FormsContext):
        pass


    # Enter a parse tree produced by ErlangParser#form.
    def enterForm(self, ctx:ErlangParser.FormContext):
        pass

    # Exit a parse tree produced by ErlangParser#form.
    def exitForm(self, ctx:ErlangParser.FormContext):
        pass


    # Enter a parse tree produced by ErlangParser#tokAtom.
    def enterTokAtom(self, ctx:ErlangParser.TokAtomContext):
        pass

    # Exit a parse tree produced by ErlangParser#tokAtom.
    def exitTokAtom(self, ctx:ErlangParser.TokAtomContext):
        pass


    # Enter a parse tree produced by ErlangParser#tokVar.
    def enterTokVar(self, ctx:ErlangParser.TokVarContext):
        pass

    # Exit a parse tree produced by ErlangParser#tokVar.
    def exitTokVar(self, ctx:ErlangParser.TokVarContext):
        pass


    # Enter a parse tree produced by ErlangParser#tokFloat.
    def enterTokFloat(self, ctx:ErlangParser.TokFloatContext):
        pass

    # Exit a parse tree produced by ErlangParser#tokFloat.
    def exitTokFloat(self, ctx:ErlangParser.TokFloatContext):
        pass


    # Enter a parse tree produced by ErlangParser#tokInteger.
    def enterTokInteger(self, ctx:ErlangParser.TokIntegerContext):
        pass

    # Exit a parse tree produced by ErlangParser#tokInteger.
    def exitTokInteger(self, ctx:ErlangParser.TokIntegerContext):
        pass


    # Enter a parse tree produced by ErlangParser#tokChar.
    def enterTokChar(self, ctx:ErlangParser.TokCharContext):
        pass

    # Exit a parse tree produced by ErlangParser#tokChar.
    def exitTokChar(self, ctx:ErlangParser.TokCharContext):
        pass


    # Enter a parse tree produced by ErlangParser#tokString.
    def enterTokString(self, ctx:ErlangParser.TokStringContext):
        pass

    # Exit a parse tree produced by ErlangParser#tokString.
    def exitTokString(self, ctx:ErlangParser.TokStringContext):
        pass


    # Enter a parse tree produced by ErlangParser#attribute.
    def enterAttribute(self, ctx:ErlangParser.AttributeContext):
        pass

    # Exit a parse tree produced by ErlangParser#attribute.
    def exitAttribute(self, ctx:ErlangParser.AttributeContext):
        pass


    # Enter a parse tree produced by ErlangParser#typeSpec.
    def enterTypeSpec(self, ctx:ErlangParser.TypeSpecContext):
        pass

    # Exit a parse tree produced by ErlangParser#typeSpec.
    def exitTypeSpec(self, ctx:ErlangParser.TypeSpecContext):
        pass


    # Enter a parse tree produced by ErlangParser#specFun.
    def enterSpecFun(self, ctx:ErlangParser.SpecFunContext):
        pass

    # Exit a parse tree produced by ErlangParser#specFun.
    def exitSpecFun(self, ctx:ErlangParser.SpecFunContext):
        pass


    # Enter a parse tree produced by ErlangParser#typedAttrVal.
    def enterTypedAttrVal(self, ctx:ErlangParser.TypedAttrValContext):
        pass

    # Exit a parse tree produced by ErlangParser#typedAttrVal.
    def exitTypedAttrVal(self, ctx:ErlangParser.TypedAttrValContext):
        pass


    # Enter a parse tree produced by ErlangParser#typedRecordFields.
    def enterTypedRecordFields(self, ctx:ErlangParser.TypedRecordFieldsContext):
        pass

    # Exit a parse tree produced by ErlangParser#typedRecordFields.
    def exitTypedRecordFields(self, ctx:ErlangParser.TypedRecordFieldsContext):
        pass


    # Enter a parse tree produced by ErlangParser#typedExprs.
    def enterTypedExprs(self, ctx:ErlangParser.TypedExprsContext):
        pass

    # Exit a parse tree produced by ErlangParser#typedExprs.
    def exitTypedExprs(self, ctx:ErlangParser.TypedExprsContext):
        pass


    # Enter a parse tree produced by ErlangParser#typedExpr.
    def enterTypedExpr(self, ctx:ErlangParser.TypedExprContext):
        pass

    # Exit a parse tree produced by ErlangParser#typedExpr.
    def exitTypedExpr(self, ctx:ErlangParser.TypedExprContext):
        pass


    # Enter a parse tree produced by ErlangParser#typeSigs.
    def enterTypeSigs(self, ctx:ErlangParser.TypeSigsContext):
        pass

    # Exit a parse tree produced by ErlangParser#typeSigs.
    def exitTypeSigs(self, ctx:ErlangParser.TypeSigsContext):
        pass


    # Enter a parse tree produced by ErlangParser#typeSig.
    def enterTypeSig(self, ctx:ErlangParser.TypeSigContext):
        pass

    # Exit a parse tree produced by ErlangParser#typeSig.
    def exitTypeSig(self, ctx:ErlangParser.TypeSigContext):
        pass


    # Enter a parse tree produced by ErlangParser#typeGuards.
    def enterTypeGuards(self, ctx:ErlangParser.TypeGuardsContext):
        pass

    # Exit a parse tree produced by ErlangParser#typeGuards.
    def exitTypeGuards(self, ctx:ErlangParser.TypeGuardsContext):
        pass


    # Enter a parse tree produced by ErlangParser#typeGuard.
    def enterTypeGuard(self, ctx:ErlangParser.TypeGuardContext):
        pass

    # Exit a parse tree produced by ErlangParser#typeGuard.
    def exitTypeGuard(self, ctx:ErlangParser.TypeGuardContext):
        pass


    # Enter a parse tree produced by ErlangParser#topTypes.
    def enterTopTypes(self, ctx:ErlangParser.TopTypesContext):
        pass

    # Exit a parse tree produced by ErlangParser#topTypes.
    def exitTopTypes(self, ctx:ErlangParser.TopTypesContext):
        pass


    # Enter a parse tree produced by ErlangParser#topType.
    def enterTopType(self, ctx:ErlangParser.TopTypeContext):
        pass

    # Exit a parse tree produced by ErlangParser#topType.
    def exitTopType(self, ctx:ErlangParser.TopTypeContext):
        pass


    # Enter a parse tree produced by ErlangParser#topType100.
    def enterTopType100(self, ctx:ErlangParser.TopType100Context):
        pass

    # Exit a parse tree produced by ErlangParser#topType100.
    def exitTopType100(self, ctx:ErlangParser.TopType100Context):
        pass


    # Enter a parse tree produced by ErlangParser#type200.
    def enterType200(self, ctx:ErlangParser.Type200Context):
        pass

    # Exit a parse tree produced by ErlangParser#type200.
    def exitType200(self, ctx:ErlangParser.Type200Context):
        pass


    # Enter a parse tree produced by ErlangParser#type300.
    def enterType300(self, ctx:ErlangParser.Type300Context):
        pass

    # Exit a parse tree produced by ErlangParser#type300.
    def exitType300(self, ctx:ErlangParser.Type300Context):
        pass


    # Enter a parse tree produced by ErlangParser#type400.
    def enterType400(self, ctx:ErlangParser.Type400Context):
        pass

    # Exit a parse tree produced by ErlangParser#type400.
    def exitType400(self, ctx:ErlangParser.Type400Context):
        pass


    # Enter a parse tree produced by ErlangParser#type500.
    def enterType500(self, ctx:ErlangParser.Type500Context):
        pass

    # Exit a parse tree produced by ErlangParser#type500.
    def exitType500(self, ctx:ErlangParser.Type500Context):
        pass


    # Enter a parse tree produced by ErlangParser#type_.
    def enterType_(self, ctx:ErlangParser.Type_Context):
        pass

    # Exit a parse tree produced by ErlangParser#type_.
    def exitType_(self, ctx:ErlangParser.Type_Context):
        pass


    # Enter a parse tree produced by ErlangParser#funType100.
    def enterFunType100(self, ctx:ErlangParser.FunType100Context):
        pass

    # Exit a parse tree produced by ErlangParser#funType100.
    def exitFunType100(self, ctx:ErlangParser.FunType100Context):
        pass


    # Enter a parse tree produced by ErlangParser#funType.
    def enterFunType(self, ctx:ErlangParser.FunTypeContext):
        pass

    # Exit a parse tree produced by ErlangParser#funType.
    def exitFunType(self, ctx:ErlangParser.FunTypeContext):
        pass


    # Enter a parse tree produced by ErlangParser#mapPairTypes.
    def enterMapPairTypes(self, ctx:ErlangParser.MapPairTypesContext):
        pass

    # Exit a parse tree produced by ErlangParser#mapPairTypes.
    def exitMapPairTypes(self, ctx:ErlangParser.MapPairTypesContext):
        pass


    # Enter a parse tree produced by ErlangParser#mapPairType.
    def enterMapPairType(self, ctx:ErlangParser.MapPairTypeContext):
        pass

    # Exit a parse tree produced by ErlangParser#mapPairType.
    def exitMapPairType(self, ctx:ErlangParser.MapPairTypeContext):
        pass


    # Enter a parse tree produced by ErlangParser#fieldTypes.
    def enterFieldTypes(self, ctx:ErlangParser.FieldTypesContext):
        pass

    # Exit a parse tree produced by ErlangParser#fieldTypes.
    def exitFieldTypes(self, ctx:ErlangParser.FieldTypesContext):
        pass


    # Enter a parse tree produced by ErlangParser#fieldType.
    def enterFieldType(self, ctx:ErlangParser.FieldTypeContext):
        pass

    # Exit a parse tree produced by ErlangParser#fieldType.
    def exitFieldType(self, ctx:ErlangParser.FieldTypeContext):
        pass


    # Enter a parse tree produced by ErlangParser#binaryType.
    def enterBinaryType(self, ctx:ErlangParser.BinaryTypeContext):
        pass

    # Exit a parse tree produced by ErlangParser#binaryType.
    def exitBinaryType(self, ctx:ErlangParser.BinaryTypeContext):
        pass


    # Enter a parse tree produced by ErlangParser#binBaseType.
    def enterBinBaseType(self, ctx:ErlangParser.BinBaseTypeContext):
        pass

    # Exit a parse tree produced by ErlangParser#binBaseType.
    def exitBinBaseType(self, ctx:ErlangParser.BinBaseTypeContext):
        pass


    # Enter a parse tree produced by ErlangParser#binUnitType.
    def enterBinUnitType(self, ctx:ErlangParser.BinUnitTypeContext):
        pass

    # Exit a parse tree produced by ErlangParser#binUnitType.
    def exitBinUnitType(self, ctx:ErlangParser.BinUnitTypeContext):
        pass


    # Enter a parse tree produced by ErlangParser#attrVal.
    def enterAttrVal(self, ctx:ErlangParser.AttrValContext):
        pass

    # Exit a parse tree produced by ErlangParser#attrVal.
    def exitAttrVal(self, ctx:ErlangParser.AttrValContext):
        pass


    # Enter a parse tree produced by ErlangParser#function_.
    def enterFunction_(self, ctx:ErlangParser.Function_Context):
        pass

    # Exit a parse tree produced by ErlangParser#function_.
    def exitFunction_(self, ctx:ErlangParser.Function_Context):
        pass


    # Enter a parse tree produced by ErlangParser#functionClause.
    def enterFunctionClause(self, ctx:ErlangParser.FunctionClauseContext):
        pass

    # Exit a parse tree produced by ErlangParser#functionClause.
    def exitFunctionClause(self, ctx:ErlangParser.FunctionClauseContext):
        pass


    # Enter a parse tree produced by ErlangParser#clauseArgs.
    def enterClauseArgs(self, ctx:ErlangParser.ClauseArgsContext):
        pass

    # Exit a parse tree produced by ErlangParser#clauseArgs.
    def exitClauseArgs(self, ctx:ErlangParser.ClauseArgsContext):
        pass


    # Enter a parse tree produced by ErlangParser#clauseGuard.
    def enterClauseGuard(self, ctx:ErlangParser.ClauseGuardContext):
        pass

    # Exit a parse tree produced by ErlangParser#clauseGuard.
    def exitClauseGuard(self, ctx:ErlangParser.ClauseGuardContext):
        pass


    # Enter a parse tree produced by ErlangParser#clauseBody.
    def enterClauseBody(self, ctx:ErlangParser.ClauseBodyContext):
        pass

    # Exit a parse tree produced by ErlangParser#clauseBody.
    def exitClauseBody(self, ctx:ErlangParser.ClauseBodyContext):
        pass


    # Enter a parse tree produced by ErlangParser#expr.
    def enterExpr(self, ctx:ErlangParser.ExprContext):
        pass

    # Exit a parse tree produced by ErlangParser#expr.
    def exitExpr(self, ctx:ErlangParser.ExprContext):
        pass


    # Enter a parse tree produced by ErlangParser#expr100.
    def enterExpr100(self, ctx:ErlangParser.Expr100Context):
        pass

    # Exit a parse tree produced by ErlangParser#expr100.
    def exitExpr100(self, ctx:ErlangParser.Expr100Context):
        pass


    # Enter a parse tree produced by ErlangParser#expr150.
    def enterExpr150(self, ctx:ErlangParser.Expr150Context):
        pass

    # Exit a parse tree produced by ErlangParser#expr150.
    def exitExpr150(self, ctx:ErlangParser.Expr150Context):
        pass


    # Enter a parse tree produced by ErlangParser#expr160.
    def enterExpr160(self, ctx:ErlangParser.Expr160Context):
        pass

    # Exit a parse tree produced by ErlangParser#expr160.
    def exitExpr160(self, ctx:ErlangParser.Expr160Context):
        pass


    # Enter a parse tree produced by ErlangParser#expr200.
    def enterExpr200(self, ctx:ErlangParser.Expr200Context):
        pass

    # Exit a parse tree produced by ErlangParser#expr200.
    def exitExpr200(self, ctx:ErlangParser.Expr200Context):
        pass


    # Enter a parse tree produced by ErlangParser#expr300.
    def enterExpr300(self, ctx:ErlangParser.Expr300Context):
        pass

    # Exit a parse tree produced by ErlangParser#expr300.
    def exitExpr300(self, ctx:ErlangParser.Expr300Context):
        pass


    # Enter a parse tree produced by ErlangParser#expr400.
    def enterExpr400(self, ctx:ErlangParser.Expr400Context):
        pass

    # Exit a parse tree produced by ErlangParser#expr400.
    def exitExpr400(self, ctx:ErlangParser.Expr400Context):
        pass


    # Enter a parse tree produced by ErlangParser#expr500.
    def enterExpr500(self, ctx:ErlangParser.Expr500Context):
        pass

    # Exit a parse tree produced by ErlangParser#expr500.
    def exitExpr500(self, ctx:ErlangParser.Expr500Context):
        pass


    # Enter a parse tree produced by ErlangParser#expr600.
    def enterExpr600(self, ctx:ErlangParser.Expr600Context):
        pass

    # Exit a parse tree produced by ErlangParser#expr600.
    def exitExpr600(self, ctx:ErlangParser.Expr600Context):
        pass


    # Enter a parse tree produced by ErlangParser#expr650.
    def enterExpr650(self, ctx:ErlangParser.Expr650Context):
        pass

    # Exit a parse tree produced by ErlangParser#expr650.
    def exitExpr650(self, ctx:ErlangParser.Expr650Context):
        pass


    # Enter a parse tree produced by ErlangParser#expr700.
    def enterExpr700(self, ctx:ErlangParser.Expr700Context):
        pass

    # Exit a parse tree produced by ErlangParser#expr700.
    def exitExpr700(self, ctx:ErlangParser.Expr700Context):
        pass


    # Enter a parse tree produced by ErlangParser#expr800.
    def enterExpr800(self, ctx:ErlangParser.Expr800Context):
        pass

    # Exit a parse tree produced by ErlangParser#expr800.
    def exitExpr800(self, ctx:ErlangParser.Expr800Context):
        pass


    # Enter a parse tree produced by ErlangParser#exprMax.
    def enterExprMax(self, ctx:ErlangParser.ExprMaxContext):
        pass

    # Exit a parse tree produced by ErlangParser#exprMax.
    def exitExprMax(self, ctx:ErlangParser.ExprMaxContext):
        pass


    # Enter a parse tree produced by ErlangParser#patExpr.
    def enterPatExpr(self, ctx:ErlangParser.PatExprContext):
        pass

    # Exit a parse tree produced by ErlangParser#patExpr.
    def exitPatExpr(self, ctx:ErlangParser.PatExprContext):
        pass


    # Enter a parse tree produced by ErlangParser#patExpr200.
    def enterPatExpr200(self, ctx:ErlangParser.PatExpr200Context):
        pass

    # Exit a parse tree produced by ErlangParser#patExpr200.
    def exitPatExpr200(self, ctx:ErlangParser.PatExpr200Context):
        pass


    # Enter a parse tree produced by ErlangParser#patExpr300.
    def enterPatExpr300(self, ctx:ErlangParser.PatExpr300Context):
        pass

    # Exit a parse tree produced by ErlangParser#patExpr300.
    def exitPatExpr300(self, ctx:ErlangParser.PatExpr300Context):
        pass


    # Enter a parse tree produced by ErlangParser#patExpr400.
    def enterPatExpr400(self, ctx:ErlangParser.PatExpr400Context):
        pass

    # Exit a parse tree produced by ErlangParser#patExpr400.
    def exitPatExpr400(self, ctx:ErlangParser.PatExpr400Context):
        pass


    # Enter a parse tree produced by ErlangParser#patExpr500.
    def enterPatExpr500(self, ctx:ErlangParser.PatExpr500Context):
        pass

    # Exit a parse tree produced by ErlangParser#patExpr500.
    def exitPatExpr500(self, ctx:ErlangParser.PatExpr500Context):
        pass


    # Enter a parse tree produced by ErlangParser#patExpr600.
    def enterPatExpr600(self, ctx:ErlangParser.PatExpr600Context):
        pass

    # Exit a parse tree produced by ErlangParser#patExpr600.
    def exitPatExpr600(self, ctx:ErlangParser.PatExpr600Context):
        pass


    # Enter a parse tree produced by ErlangParser#patExpr650.
    def enterPatExpr650(self, ctx:ErlangParser.PatExpr650Context):
        pass

    # Exit a parse tree produced by ErlangParser#patExpr650.
    def exitPatExpr650(self, ctx:ErlangParser.PatExpr650Context):
        pass


    # Enter a parse tree produced by ErlangParser#patExpr700.
    def enterPatExpr700(self, ctx:ErlangParser.PatExpr700Context):
        pass

    # Exit a parse tree produced by ErlangParser#patExpr700.
    def exitPatExpr700(self, ctx:ErlangParser.PatExpr700Context):
        pass


    # Enter a parse tree produced by ErlangParser#patExpr800.
    def enterPatExpr800(self, ctx:ErlangParser.PatExpr800Context):
        pass

    # Exit a parse tree produced by ErlangParser#patExpr800.
    def exitPatExpr800(self, ctx:ErlangParser.PatExpr800Context):
        pass


    # Enter a parse tree produced by ErlangParser#patExprMax.
    def enterPatExprMax(self, ctx:ErlangParser.PatExprMaxContext):
        pass

    # Exit a parse tree produced by ErlangParser#patExprMax.
    def exitPatExprMax(self, ctx:ErlangParser.PatExprMaxContext):
        pass


    # Enter a parse tree produced by ErlangParser#mapPatExpr.
    def enterMapPatExpr(self, ctx:ErlangParser.MapPatExprContext):
        pass

    # Exit a parse tree produced by ErlangParser#mapPatExpr.
    def exitMapPatExpr(self, ctx:ErlangParser.MapPatExprContext):
        pass


    # Enter a parse tree produced by ErlangParser#recordPatExpr.
    def enterRecordPatExpr(self, ctx:ErlangParser.RecordPatExprContext):
        pass

    # Exit a parse tree produced by ErlangParser#recordPatExpr.
    def exitRecordPatExpr(self, ctx:ErlangParser.RecordPatExprContext):
        pass


    # Enter a parse tree produced by ErlangParser#list_.
    def enterList_(self, ctx:ErlangParser.List_Context):
        pass

    # Exit a parse tree produced by ErlangParser#list_.
    def exitList_(self, ctx:ErlangParser.List_Context):
        pass


    # Enter a parse tree produced by ErlangParser#tail.
    def enterTail(self, ctx:ErlangParser.TailContext):
        pass

    # Exit a parse tree produced by ErlangParser#tail.
    def exitTail(self, ctx:ErlangParser.TailContext):
        pass


    # Enter a parse tree produced by ErlangParser#binary.
    def enterBinary(self, ctx:ErlangParser.BinaryContext):
        pass

    # Exit a parse tree produced by ErlangParser#binary.
    def exitBinary(self, ctx:ErlangParser.BinaryContext):
        pass


    # Enter a parse tree produced by ErlangParser#binElements.
    def enterBinElements(self, ctx:ErlangParser.BinElementsContext):
        pass

    # Exit a parse tree produced by ErlangParser#binElements.
    def exitBinElements(self, ctx:ErlangParser.BinElementsContext):
        pass


    # Enter a parse tree produced by ErlangParser#binElement.
    def enterBinElement(self, ctx:ErlangParser.BinElementContext):
        pass

    # Exit a parse tree produced by ErlangParser#binElement.
    def exitBinElement(self, ctx:ErlangParser.BinElementContext):
        pass


    # Enter a parse tree produced by ErlangParser#bitExpr.
    def enterBitExpr(self, ctx:ErlangParser.BitExprContext):
        pass

    # Exit a parse tree produced by ErlangParser#bitExpr.
    def exitBitExpr(self, ctx:ErlangParser.BitExprContext):
        pass


    # Enter a parse tree produced by ErlangParser#optBitSizeExpr.
    def enterOptBitSizeExpr(self, ctx:ErlangParser.OptBitSizeExprContext):
        pass

    # Exit a parse tree produced by ErlangParser#optBitSizeExpr.
    def exitOptBitSizeExpr(self, ctx:ErlangParser.OptBitSizeExprContext):
        pass


    # Enter a parse tree produced by ErlangParser#optBitTypeList.
    def enterOptBitTypeList(self, ctx:ErlangParser.OptBitTypeListContext):
        pass

    # Exit a parse tree produced by ErlangParser#optBitTypeList.
    def exitOptBitTypeList(self, ctx:ErlangParser.OptBitTypeListContext):
        pass


    # Enter a parse tree produced by ErlangParser#bitTypeList.
    def enterBitTypeList(self, ctx:ErlangParser.BitTypeListContext):
        pass

    # Exit a parse tree produced by ErlangParser#bitTypeList.
    def exitBitTypeList(self, ctx:ErlangParser.BitTypeListContext):
        pass


    # Enter a parse tree produced by ErlangParser#bitType.
    def enterBitType(self, ctx:ErlangParser.BitTypeContext):
        pass

    # Exit a parse tree produced by ErlangParser#bitType.
    def exitBitType(self, ctx:ErlangParser.BitTypeContext):
        pass


    # Enter a parse tree produced by ErlangParser#bitSizeExpr.
    def enterBitSizeExpr(self, ctx:ErlangParser.BitSizeExprContext):
        pass

    # Exit a parse tree produced by ErlangParser#bitSizeExpr.
    def exitBitSizeExpr(self, ctx:ErlangParser.BitSizeExprContext):
        pass


    # Enter a parse tree produced by ErlangParser#listComprehension.
    def enterListComprehension(self, ctx:ErlangParser.ListComprehensionContext):
        pass

    # Exit a parse tree produced by ErlangParser#listComprehension.
    def exitListComprehension(self, ctx:ErlangParser.ListComprehensionContext):
        pass


    # Enter a parse tree produced by ErlangParser#binaryComprehension.
    def enterBinaryComprehension(self, ctx:ErlangParser.BinaryComprehensionContext):
        pass

    # Exit a parse tree produced by ErlangParser#binaryComprehension.
    def exitBinaryComprehension(self, ctx:ErlangParser.BinaryComprehensionContext):
        pass


    # Enter a parse tree produced by ErlangParser#lcExprs.
    def enterLcExprs(self, ctx:ErlangParser.LcExprsContext):
        pass

    # Exit a parse tree produced by ErlangParser#lcExprs.
    def exitLcExprs(self, ctx:ErlangParser.LcExprsContext):
        pass


    # Enter a parse tree produced by ErlangParser#lcExpr.
    def enterLcExpr(self, ctx:ErlangParser.LcExprContext):
        pass

    # Exit a parse tree produced by ErlangParser#lcExpr.
    def exitLcExpr(self, ctx:ErlangParser.LcExprContext):
        pass


    # Enter a parse tree produced by ErlangParser#tuple_.
    def enterTuple_(self, ctx:ErlangParser.Tuple_Context):
        pass

    # Exit a parse tree produced by ErlangParser#tuple_.
    def exitTuple_(self, ctx:ErlangParser.Tuple_Context):
        pass


    # Enter a parse tree produced by ErlangParser#mapExpr.
    def enterMapExpr(self, ctx:ErlangParser.MapExprContext):
        pass

    # Exit a parse tree produced by ErlangParser#mapExpr.
    def exitMapExpr(self, ctx:ErlangParser.MapExprContext):
        pass


    # Enter a parse tree produced by ErlangParser#mapTuple.
    def enterMapTuple(self, ctx:ErlangParser.MapTupleContext):
        pass

    # Exit a parse tree produced by ErlangParser#mapTuple.
    def exitMapTuple(self, ctx:ErlangParser.MapTupleContext):
        pass


    # Enter a parse tree produced by ErlangParser#mapField.
    def enterMapField(self, ctx:ErlangParser.MapFieldContext):
        pass

    # Exit a parse tree produced by ErlangParser#mapField.
    def exitMapField(self, ctx:ErlangParser.MapFieldContext):
        pass


    # Enter a parse tree produced by ErlangParser#mapFieldAssoc.
    def enterMapFieldAssoc(self, ctx:ErlangParser.MapFieldAssocContext):
        pass

    # Exit a parse tree produced by ErlangParser#mapFieldAssoc.
    def exitMapFieldAssoc(self, ctx:ErlangParser.MapFieldAssocContext):
        pass


    # Enter a parse tree produced by ErlangParser#mapFieldExact.
    def enterMapFieldExact(self, ctx:ErlangParser.MapFieldExactContext):
        pass

    # Exit a parse tree produced by ErlangParser#mapFieldExact.
    def exitMapFieldExact(self, ctx:ErlangParser.MapFieldExactContext):
        pass


    # Enter a parse tree produced by ErlangParser#mapKey.
    def enterMapKey(self, ctx:ErlangParser.MapKeyContext):
        pass

    # Exit a parse tree produced by ErlangParser#mapKey.
    def exitMapKey(self, ctx:ErlangParser.MapKeyContext):
        pass


    # Enter a parse tree produced by ErlangParser#recordExpr.
    def enterRecordExpr(self, ctx:ErlangParser.RecordExprContext):
        pass

    # Exit a parse tree produced by ErlangParser#recordExpr.
    def exitRecordExpr(self, ctx:ErlangParser.RecordExprContext):
        pass


    # Enter a parse tree produced by ErlangParser#recordTuple.
    def enterRecordTuple(self, ctx:ErlangParser.RecordTupleContext):
        pass

    # Exit a parse tree produced by ErlangParser#recordTuple.
    def exitRecordTuple(self, ctx:ErlangParser.RecordTupleContext):
        pass


    # Enter a parse tree produced by ErlangParser#recordFields.
    def enterRecordFields(self, ctx:ErlangParser.RecordFieldsContext):
        pass

    # Exit a parse tree produced by ErlangParser#recordFields.
    def exitRecordFields(self, ctx:ErlangParser.RecordFieldsContext):
        pass


    # Enter a parse tree produced by ErlangParser#recordField.
    def enterRecordField(self, ctx:ErlangParser.RecordFieldContext):
        pass

    # Exit a parse tree produced by ErlangParser#recordField.
    def exitRecordField(self, ctx:ErlangParser.RecordFieldContext):
        pass


    # Enter a parse tree produced by ErlangParser#functionCall.
    def enterFunctionCall(self, ctx:ErlangParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by ErlangParser#functionCall.
    def exitFunctionCall(self, ctx:ErlangParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by ErlangParser#ifExpr.
    def enterIfExpr(self, ctx:ErlangParser.IfExprContext):
        pass

    # Exit a parse tree produced by ErlangParser#ifExpr.
    def exitIfExpr(self, ctx:ErlangParser.IfExprContext):
        pass


    # Enter a parse tree produced by ErlangParser#ifClauses.
    def enterIfClauses(self, ctx:ErlangParser.IfClausesContext):
        pass

    # Exit a parse tree produced by ErlangParser#ifClauses.
    def exitIfClauses(self, ctx:ErlangParser.IfClausesContext):
        pass


    # Enter a parse tree produced by ErlangParser#ifClause.
    def enterIfClause(self, ctx:ErlangParser.IfClauseContext):
        pass

    # Exit a parse tree produced by ErlangParser#ifClause.
    def exitIfClause(self, ctx:ErlangParser.IfClauseContext):
        pass


    # Enter a parse tree produced by ErlangParser#caseExpr.
    def enterCaseExpr(self, ctx:ErlangParser.CaseExprContext):
        pass

    # Exit a parse tree produced by ErlangParser#caseExpr.
    def exitCaseExpr(self, ctx:ErlangParser.CaseExprContext):
        pass


    # Enter a parse tree produced by ErlangParser#crClauses.
    def enterCrClauses(self, ctx:ErlangParser.CrClausesContext):
        pass

    # Exit a parse tree produced by ErlangParser#crClauses.
    def exitCrClauses(self, ctx:ErlangParser.CrClausesContext):
        pass


    # Enter a parse tree produced by ErlangParser#crClause.
    def enterCrClause(self, ctx:ErlangParser.CrClauseContext):
        pass

    # Exit a parse tree produced by ErlangParser#crClause.
    def exitCrClause(self, ctx:ErlangParser.CrClauseContext):
        pass


    # Enter a parse tree produced by ErlangParser#receiveExpr.
    def enterReceiveExpr(self, ctx:ErlangParser.ReceiveExprContext):
        pass

    # Exit a parse tree produced by ErlangParser#receiveExpr.
    def exitReceiveExpr(self, ctx:ErlangParser.ReceiveExprContext):
        pass


    # Enter a parse tree produced by ErlangParser#funExpr.
    def enterFunExpr(self, ctx:ErlangParser.FunExprContext):
        pass

    # Exit a parse tree produced by ErlangParser#funExpr.
    def exitFunExpr(self, ctx:ErlangParser.FunExprContext):
        pass


    # Enter a parse tree produced by ErlangParser#atomOrVar.
    def enterAtomOrVar(self, ctx:ErlangParser.AtomOrVarContext):
        pass

    # Exit a parse tree produced by ErlangParser#atomOrVar.
    def exitAtomOrVar(self, ctx:ErlangParser.AtomOrVarContext):
        pass


    # Enter a parse tree produced by ErlangParser#integerOrVar.
    def enterIntegerOrVar(self, ctx:ErlangParser.IntegerOrVarContext):
        pass

    # Exit a parse tree produced by ErlangParser#integerOrVar.
    def exitIntegerOrVar(self, ctx:ErlangParser.IntegerOrVarContext):
        pass


    # Enter a parse tree produced by ErlangParser#funClauses.
    def enterFunClauses(self, ctx:ErlangParser.FunClausesContext):
        pass

    # Exit a parse tree produced by ErlangParser#funClauses.
    def exitFunClauses(self, ctx:ErlangParser.FunClausesContext):
        pass


    # Enter a parse tree produced by ErlangParser#funClause.
    def enterFunClause(self, ctx:ErlangParser.FunClauseContext):
        pass

    # Exit a parse tree produced by ErlangParser#funClause.
    def exitFunClause(self, ctx:ErlangParser.FunClauseContext):
        pass


    # Enter a parse tree produced by ErlangParser#tryExpr.
    def enterTryExpr(self, ctx:ErlangParser.TryExprContext):
        pass

    # Exit a parse tree produced by ErlangParser#tryExpr.
    def exitTryExpr(self, ctx:ErlangParser.TryExprContext):
        pass


    # Enter a parse tree produced by ErlangParser#tryCatch.
    def enterTryCatch(self, ctx:ErlangParser.TryCatchContext):
        pass

    # Exit a parse tree produced by ErlangParser#tryCatch.
    def exitTryCatch(self, ctx:ErlangParser.TryCatchContext):
        pass


    # Enter a parse tree produced by ErlangParser#tryClauses.
    def enterTryClauses(self, ctx:ErlangParser.TryClausesContext):
        pass

    # Exit a parse tree produced by ErlangParser#tryClauses.
    def exitTryClauses(self, ctx:ErlangParser.TryClausesContext):
        pass


    # Enter a parse tree produced by ErlangParser#tryClause.
    def enterTryClause(self, ctx:ErlangParser.TryClauseContext):
        pass

    # Exit a parse tree produced by ErlangParser#tryClause.
    def exitTryClause(self, ctx:ErlangParser.TryClauseContext):
        pass


    # Enter a parse tree produced by ErlangParser#tryOptStackTrace.
    def enterTryOptStackTrace(self, ctx:ErlangParser.TryOptStackTraceContext):
        pass

    # Exit a parse tree produced by ErlangParser#tryOptStackTrace.
    def exitTryOptStackTrace(self, ctx:ErlangParser.TryOptStackTraceContext):
        pass


    # Enter a parse tree produced by ErlangParser#argumentList.
    def enterArgumentList(self, ctx:ErlangParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by ErlangParser#argumentList.
    def exitArgumentList(self, ctx:ErlangParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by ErlangParser#patArgumentList.
    def enterPatArgumentList(self, ctx:ErlangParser.PatArgumentListContext):
        pass

    # Exit a parse tree produced by ErlangParser#patArgumentList.
    def exitPatArgumentList(self, ctx:ErlangParser.PatArgumentListContext):
        pass


    # Enter a parse tree produced by ErlangParser#exprs.
    def enterExprs(self, ctx:ErlangParser.ExprsContext):
        pass

    # Exit a parse tree produced by ErlangParser#exprs.
    def exitExprs(self, ctx:ErlangParser.ExprsContext):
        pass


    # Enter a parse tree produced by ErlangParser#patExprs.
    def enterPatExprs(self, ctx:ErlangParser.PatExprsContext):
        pass

    # Exit a parse tree produced by ErlangParser#patExprs.
    def exitPatExprs(self, ctx:ErlangParser.PatExprsContext):
        pass


    # Enter a parse tree produced by ErlangParser#guard_.
    def enterGuard_(self, ctx:ErlangParser.Guard_Context):
        pass

    # Exit a parse tree produced by ErlangParser#guard_.
    def exitGuard_(self, ctx:ErlangParser.Guard_Context):
        pass


    # Enter a parse tree produced by ErlangParser#atomic.
    def enterAtomic(self, ctx:ErlangParser.AtomicContext):
        pass

    # Exit a parse tree produced by ErlangParser#atomic.
    def exitAtomic(self, ctx:ErlangParser.AtomicContext):
        pass


    # Enter a parse tree produced by ErlangParser#prefixOp.
    def enterPrefixOp(self, ctx:ErlangParser.PrefixOpContext):
        pass

    # Exit a parse tree produced by ErlangParser#prefixOp.
    def exitPrefixOp(self, ctx:ErlangParser.PrefixOpContext):
        pass


    # Enter a parse tree produced by ErlangParser#multOp.
    def enterMultOp(self, ctx:ErlangParser.MultOpContext):
        pass

    # Exit a parse tree produced by ErlangParser#multOp.
    def exitMultOp(self, ctx:ErlangParser.MultOpContext):
        pass


    # Enter a parse tree produced by ErlangParser#addOp.
    def enterAddOp(self, ctx:ErlangParser.AddOpContext):
        pass

    # Exit a parse tree produced by ErlangParser#addOp.
    def exitAddOp(self, ctx:ErlangParser.AddOpContext):
        pass


    # Enter a parse tree produced by ErlangParser#listOp.
    def enterListOp(self, ctx:ErlangParser.ListOpContext):
        pass

    # Exit a parse tree produced by ErlangParser#listOp.
    def exitListOp(self, ctx:ErlangParser.ListOpContext):
        pass


    # Enter a parse tree produced by ErlangParser#compOp.
    def enterCompOp(self, ctx:ErlangParser.CompOpContext):
        pass

    # Exit a parse tree produced by ErlangParser#compOp.
    def exitCompOp(self, ctx:ErlangParser.CompOpContext):
        pass



del ErlangParser