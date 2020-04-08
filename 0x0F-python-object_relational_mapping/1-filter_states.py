#!/usr/bin/python3
"""script that lists all states with a name starting
with N from the database"""
import MySQLdb
from sys import argv
if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("""SELECT id, name FROM states WHERE name LIKE 'N%' ORDER
              BY states.id ASC""")
    res = c.fetchall()
    for row in res:
        print(row)
    c.close()
    db.close()
