from io import StringIO

from antlr4 import *
from dist.SolidityParser import SolidityParser
from dist.SolidityLexer import SolidityLexer
from dist.YulLexer import YulLexer
from dist.YulParser import YulParser
from dist.VyperLexer import VyperLexer
from dist.VyperParser import VyperParser

# Define the input code to be parsed
solidity_script = open("./scripts/solidity_1.sol", "r").read()
yul_script = open("./scripts/yul_2.yul", "r").read()
vyper_script = open("./scripts/vyper_1.vy", "r").read()

def parse_solidity(code):
    input_stream = InputStream(code)

    lexer = SolidityLexer(input_stream)

    token_stream = CommonTokenStream(lexer)

    parser = SolidityParser(token_stream)

    parse_tree = parser.sourceUnit()
    print(parse_tree.toStringTree(recog=parser))


def parse_yul(code):
    input_stream = InputStream(code)

    lexer = YulLexer(input_stream)

    token_stream = CommonTokenStream(lexer)

    parser = YulParser(token_stream)

    parse_tree = parser.sourceUnit()
    print(parse_tree.toStringTree(recog=parser))


def parse_vyper(code):
    input_stream = InputStream(code)

    lexer = VyperLexer(input_stream)

    token_stream = CommonTokenStream(lexer)

    parser = VyperParser(token_stream)

    parse_tree = parser.single_input()
    print(parse_tree.toStringTree(recog=parser))


parse_yul(yul_script)
