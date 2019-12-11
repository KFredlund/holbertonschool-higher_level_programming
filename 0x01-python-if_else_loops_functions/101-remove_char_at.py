#!/usr/bin/python3
def remove_char_at(str, n):
    array = list(str)
    for i in range(0, len(str) - 1):
        if i >= n:
            array[i] = array[i + 1]
    result = "".join(array)
    return result[:-1]
