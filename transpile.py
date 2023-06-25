""" Transpile a smart contract from one language to another.
    Possible transpilations: vyper to solidity, solidity to vyper, yul to solidity
"""
import sys
import argparse
import os

from transpilers import Transpiler

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input_file', help="Input file")

    parser.add_argument('-f', '-from', help="The language to transpile from", required=True, choices=['vyper', 'yul', 'solidity'])
    parser.add_argument('-t', '-to', help="The language to transpile to", required=True, choices=['vyper', 'yul', 'solidity'])

    args = parser.parse_args()

    if args.input_file is None:
        print("No input file specified")
        sys.exit(1)

    if not os.path.isfile(args.input_file):
        print("Input file does not exist")
        sys.exit(1)

    if args.f == args.t:
        print("Cannot transpile from and to the same language")
        sys.exit(1)

    possible_transpilations = [('vyper', 'solidity'), ('solidity', 'vyper'), ('yul', 'solidity')]
    if (args.f, args.t) not in possible_transpilations:
        print("Cannot transpile from {} to {}".format(args.f, args.t))
        sys.exit(1)

    transpiler = Transpiler(args.input_file, args.f, args.t)
    transpiler.transpile()