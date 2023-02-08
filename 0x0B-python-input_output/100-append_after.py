#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing a specific string.

    Parameters:
        filename (str): The name of the file to be written to. Default value is an empty string.
        search_string (str): The string to search for in each line of the file. Default value is an empty string.
        new_string (str): The string to be inserted after each line containing the search string. Default value is an empty string.

    Returns:
        None
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')

