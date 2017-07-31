import argparse
import sys

from core import parse_file, print_code_tree

parser = argparse.ArgumentParser(description='Semantic Merge Python Parser Plugin')
parser.add_argument('mode', type=str,
                    help='Mode of parser. Only supported mode: \n\t - shell: parser will continue running until receive "end" on the "stdin"')
parser.add_argument('path_to_the_flag', type=str,
                    help='Path to flag file.')

args = parser.parse_args()

if not args.mode == 'shell':
    parser.print_help()
    sys.exit(-1)

input_file = input()

while not input_file == 'end':
    output_file = input()

    code_tree = parse_file(input_file)
    print_code_tree(output_file, code_tree)
