#!/usr/bin/python3
import MySQLdb
import sys


def print_table_states():
    """ A method that prints the states from a table """
    db = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="Bk08262012",
        db="hbtn_0e_0_usa"
    )
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY states.id")
    states_list = cur.fetchall()

    for x in states_list:
        print(x)

if __name__ == '__main__':
    print_table_states()
