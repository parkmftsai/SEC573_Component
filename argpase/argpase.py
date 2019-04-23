import argparse 
def process_command():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', help='foo help')
    parser.add_argument('--text', '-t', default="park",type=str, required=False, help='Text for program')
    parser.add_argument('--int', '-i', default=0,type=int, required=False, help='I for program',nargs='+')

    return parser.parse_args()
if __name__ == '__main__':
    args = process_command()
    print(args.foo)
    print(args.text)
    print(args.int)
    print(args.list)
"""
from __future__ import print_function
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("pos1", help="positional argument 1")
parser.add_argument("-o", "--optional-arg", help="optional argument", dest="opt", default="default")
args = parser.parse_args()
print("positional arg:", args.pos1)
print("optional arg:", args.opt)
"""
