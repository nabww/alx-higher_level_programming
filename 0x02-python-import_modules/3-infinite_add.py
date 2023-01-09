#!/usr/bin/python3
import sys
arguments = sys.argv[1:]
result = 0

for argument in arguments:
    result += int(argument)

print(result)
