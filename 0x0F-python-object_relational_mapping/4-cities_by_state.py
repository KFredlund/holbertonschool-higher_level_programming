#!/usr/bin/python3
import MySQLdb
import sys


def join_table_states():
    """ A method that filters the states from a table """
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM states, \
                cities WHERE states.id = cities.state_id")
    states_list = cur.fetchall()
    for x in states_list:
        print(x)

if __name__ == '__main__':
    join_table_states()
