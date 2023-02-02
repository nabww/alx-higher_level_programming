#!/usr/bin/python3
def text_indentation(text):
    """text indent"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for i, char in enumerate(text):
        if char in "?:.":
            result += char + "\n\n"
            if i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        else:
            result += char
    print(result, end='')

