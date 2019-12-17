#!/usr/bin/python3
i = 0


def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx > len(my_list):
        return None
    for i in range(0, idx):
        numb = i
    return (my_list[numb + 1])
