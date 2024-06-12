import argparse


def greet(a, b):
    print("Hello!", a, b)


def farewell():
    print("Goodbye!")


parse = argparse.ArgumentParser()
parse.add_argument("--greet", action='store_true')
parse.add_argument("--a", type=int)
parse.add_argument("--b", type=int)
parse.add_argument("--farewell", action='store_true')
args = parse.parse_args()

if args.greet:
    greet(args.a, args.b)
elif args.farewell:
    farewell()
