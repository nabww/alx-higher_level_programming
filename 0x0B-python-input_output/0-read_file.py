#!/usr/bin/python3
"""

read_file function module.

define read_file_function.

"""


def read_file(filename=""):
    """Read text file (UTF8) and print to stdout
    filename (file):
    """

    with open(filename, 'r') as myfile:
        print(myfile.read(), end="")
