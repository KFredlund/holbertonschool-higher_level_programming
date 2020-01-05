#!/usr/bin/python3
def text_indentation(text):
    """Function that prints a text with 2 new lines after each of these
    chars: '.', '?', ':'
    Args:
        text: text to parse and print 2 new lines after chars
    Returns: Text with 2 new lines after each spec char
    Raises:
        TypeError: If text is not a string
    Docstring Examples:
        see dir: /tests/5-text_indentation.txt
    """
    i = 0

    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    text = text.strip()
    while i < len(text):
        if text[0] is " ":
            i += 1
        elif text[i] is ".":
            print(text[i], end="")
            print('\n')
            if text[i] is " ":
                i += 1
        elif text[i] is "?":
            print(text[i], end="")
            print('\n')
            if text[i] is " ":
                i += 1
        elif text[i] is ":":
            print(text[i], end="")
            print('\n')
            if text[i] is " ":
                i += 1
        else:
            print(text[i], end="")
        i += 1
