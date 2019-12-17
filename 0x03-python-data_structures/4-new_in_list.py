#!/usr/bin/python3
i = 0
newlist = []


def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > len(my_list):
        return my_list
    for i in range(0, len(my_list)):
        newlist.append(i + 1)
    for i in range(0, idx):
        numb = i
    newlist.remove(numb + 2)
    newlist.insert(idx, element)
    return newlist
