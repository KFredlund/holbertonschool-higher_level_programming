#!/usr/bin/python3
import MySQLdb
import sys
"""
python3 -c 'print(__import__("my_module").my_function.__doc__)'
python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
"""


def filter_table_states():
    """ A method that filters the states from a table """
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states
                WHERE name LIKE 'N%' ORDER BY states.id")
    states_list = cur.fetchall()
    for x in states_list:
        print(x)

if __name__ == '__main__':
    filter_table_states()
