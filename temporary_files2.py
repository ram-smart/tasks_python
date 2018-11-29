import json
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--key", help="dictionary key")
parser.add_argument("--val", help="the value of the dictionary key")
args = parser.parse_args()

print(type(args.key))
print(type(args.val))

if args.key != None and args.val != None:
    print("Ok")
else:
    print("Bug")