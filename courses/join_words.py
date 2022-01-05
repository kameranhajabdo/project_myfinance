import sys

args = sys.argv[1:]

strings = [ x for x in args if not x.isnumeric()]

print(strings)

