#!/usr/bin/python3
i = 0


def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > len(my_list):
        return my_list
    for i in range(0, idx + 1):
        numb = i + 1
    my_list.remove(numb)
    my_list.insert(idx, element)
    return my_list
