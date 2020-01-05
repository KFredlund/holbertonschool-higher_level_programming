#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        res = fct(*args)
        return res
    except Exception as er:
        print("Exception: {}".format(er), file=stderr)
        return None
