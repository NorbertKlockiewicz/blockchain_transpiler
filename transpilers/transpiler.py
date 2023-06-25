import os

from antlr4 import InputStream, CommonTokenStream

from transpilers.dist.SolidityLexer import SolidityLexer
from transpilers.dist.SolidityParser import SolidityParser
from transpilers.dist.VyperLexer import VyperLexer
from transpilers.dist.VyperParser import VyperParser
from transpilers.dist.YulLexer import YulLexer
from transpilers.dist.YulParser import YulParser
from .vyper_to_solidity_visitor import VyperToSolidityVisitor
from .yul_to_solidity_visitor import YulToSolidityVisitor


class Transpiler:
    def __init__(self, input_file, _from, _to):
        self._input_file = input_file
        self._from = _from
        self._to = _to

    def _parse(self, lexer) -> CommonTokenStream:
        code = open(self._input_file, "r").read()

        input_stream = InputStream(code)

        _lexer = lexer(input_stream)

        return CommonTokenStream(_lexer)

    def _parse_solidity(self) -> SolidityParser.SourceUnitContext:
        parser = SolidityParser(self._parse(SolidityLexer))

        return parser.sourceUnit()

    def _parse_vyper(self) -> VyperParser.ModuleContext:
        parser = VyperParser(self._parse(VyperLexer))

        return parser.module()

    def _parse_yul(self) -> YulParser.SourceUnitContext:
        parser = YulParser(self._parse(YulLexer))

        return parser.sourceUnit()

    def transpile(self):

        match self._from, self._to:
            case ["vyper", "solidity"]:
                output_file = os.path.splitext(os.path.basename(self._input_file))[0] + ".sol"

                with open(output_file, "w") as f:
                    parse_tree = self._parse_vyper()

                    visitor = VyperToSolidityVisitor(f)
                    visitor.visitModule(parse_tree)

                    output_file = os.path.abspath(output_file)
                    print("Output written to " + output_file)

            # case ["solidity", "vyper"]:
            #     output_file = os.path.splitext(os.path.basename(self._input_file))[0] + ".vy"
            #
            #     with open(output_file, "w") as f:
            #         parse_tree = self._parse_solidity()
            #
            #         visitor = SolidityToVyperVisitor(f)
            #         visitor.visitSourceUnit(parse_tree)
            #         output_file = os.path.abspath(output_file)
            #         print("Output written to " + output_file)

            case ["yul", "solidity"]:
                output_file = os.path.splitext(os.path.basename(self._input_file))[0] + ".sol"

                with open(output_file, "w") as f:
                    parse_tree = self._parse_yul()

                    visitor = YulToSolidityVisitor()
                    visitor.visitSourceUnit(parse_tree)

                    f.write(visitor.get_solidity_code())

                    output_file = os.path.abspath(output_file)
                    print("Output written to " + output_file)
