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
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states")
    states_list = cur.fetchall()
    for x in states_list:
        print(x)

if __name__ == '__main__':
    print_table_states()
