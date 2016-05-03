from __future__ import print_function, division

from operator import (
    and_,
    or_,
)

import sys


def readlist(filename):
    with (sys.stdin if filename == "-" else open(filename)) as f:
        return f.read().split("\n")[:-1]

def readset(filename):
    return set(readlist(filename))

def and_op(*inputs):
    return reduce(and_, inputs)

def or_op(*inputs):
    return reduce(or_, inputs, set())

def sub_op(a, b):
    return a - b

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(prog='bt')
    subparsers = parser.add_subparsers(help="sub-command help")

    parser_and = subparsers.add_parser('and')
    parser_and.add_argument('inputs', type=str, nargs="*")
    parser_and.set_defaults(op=and_op)

    parser_or = subparsers.add_parser('or')
    parser_or.add_argument('inputs', type=str, nargs="*")
    parser_or.set_defaults(op=or_op)

    parser_sub = subparsers.add_parser('sub')
    parser_sub.add_argument('inputs', type=str, nargs=2)
    parser_sub.set_defaults(op=sub_op)


    args = parser.parse_args()

    map(print, args.op(*map(readset, args.inputs)))
