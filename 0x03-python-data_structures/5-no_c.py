#!/usr/bin/python3
def no_c(my_string):
    counter_c = my_string.count('c')
    counter_C = my_string.count('C')
    my_string = list(my_string)
    while counter_c:
        my_string.remove('c')
        counter_c -= 1
    while counter_C:
        my_string.remove('C')
        counter_C -= 1
    my_string = ''.join(my_string)
    return my_string
