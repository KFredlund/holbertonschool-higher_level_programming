#!/usr/bin/python3
import MySQLdb
import sys


def filter_table_states():
    """ A method that filters the states from a table """
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    state_name = sys.argv[4]
    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                WHERE states.name = %s", (state_name,))
    states_list = cur.fetchall()
    for x in states_list:
        print(x)

if __name__ == '__main__':
    filter_table_states()
