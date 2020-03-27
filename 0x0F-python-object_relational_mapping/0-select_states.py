#!/usr/bin/python3
import MySQLdb
db = MySQLdb.connect(
    host="localhost",
    user="user_0d_1",
    passwd="Bk08262012",
    db="hbtn_0e_0_usa"
)
cur = db.cursor()
result = cur.execute("SELECT id, name FROM states")
print(result)
cur.close()
db.close()
