#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_b == (1, ):
        tuple_b = (1, 0)
    if not tuple_b:
        tuple_b = (0, 0)
    tuple3 = tuple(sum(i) for i in zip(tuple_a, tuple_b))
    return tuple3
