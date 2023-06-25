from io import StringIO

from antlr4 import *

from VyperToSolidityTranspiler import VyperToSolidityTranspiler
from dist.SolidityParser import SolidityParser
from dist.SolidityLexer import SolidityLexer
from dist.YulLexer import YulLexer
from dist.YulParser import YulParser
from dist.VyperLexer import VyperLexer
from dist.VyperParser import VyperParser
from YulToSolidityTranspiler import YulToSolidityTranspiler
from YulToVyperTranspiler import YulToVyperTranspiler

# Define the input code to be parsed
solidity_script = open("./scripts/solidity_1.sol", "r").read()
yul_script = open("scripts/yul/yul_for.yul", "r").read()
vyper_script = open("./scripts/vyper/blind_auction.vy", "r").read()

def parse_solidity(code):
    input_stream = InputStream(code)

    lexer = SolidityLexer(input_stream)

    token_stream = CommonTokenStream(lexer)

    parser = SolidityParser(token_stream)

    parse_tree = parser.sourceUnit()
    print(parse_tree.toStringTree(recog=parser))


def parse_yul_to_solidity(code):
    input_stream = InputStream(code)

    lexer = YulLexer(input_stream)

    token_stream = CommonTokenStream(lexer)

    parser = YulParser(token_stream)

    parse_tree = parser.sourceUnit()
    visitor = YulToSolidityTranspiler()
    visitor.visitSourceUnit(parse_tree)
    with open("./transpiledCode/YulToSolidity.sol", "w") as f:
        f.write(visitor.get_solidity_code())


def parse_yul_to_vyper(code):
    input_stream = InputStream(code)

    lexer = YulLexer(input_stream)

    token_stream = CommonTokenStream(lexer)

    parser = YulParser(token_stream)

    parse_tree = parser.sourceUnit()
    visitor = YulToVyperTranspiler()
    visitor.visitSourceUnit(parse_tree)
    with open("./transpiledCode/YulToVyper.vy", "w") as f:
        f.write(visitor.get_vyper_code())


def parse_vyper(code):
    input_stream = InputStream(code)

    lexer = VyperLexer(input_stream)

    token_stream = CommonTokenStream(lexer)

    parser = VyperParser(token_stream)

    parse_tree = parser.module()
    print(parse_tree.toStringTree(recog=parser))
    with open("./transpiledCode/VyperToSolidity.sol", "a+") as f:
        visitor = VyperToSolidityTranspiler(f)
        visitor.visitModule(parse_tree)


# parse_yul_to_vyper(yul_script)
parse_yul_to_solidity(yul_script)
# parse_vyper(vyper_script)
