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
    cur.execute("SELECT cities.name FROM states, \
                cities WHERE states.name = %s and states.id \
                = cities.state_id", (state_name,))
    states_list = cur.fetchall()
    for x in states_list:
        print(", ".join(x), end=', ')
    print()
if __name__ == '__main__':
    filter_table_states()
