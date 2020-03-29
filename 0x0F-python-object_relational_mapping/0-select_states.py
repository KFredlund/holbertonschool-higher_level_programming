#!/usr/bin/python3
import MySQLdb
import sys
"""
python3 -c 'print(__import__("my_module").my_function.__doc__)'
python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
"""


def print_table_states():
    """ A method that prints the states from a table """
    db = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="Bk08262012",
        db="hbtn_0e_0_usa"
    )
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states")
    states_list = cur.fetchmany(5)
    for x in states_list:
        print(x)

if __name__ == '__main__':
    print_table_states()
