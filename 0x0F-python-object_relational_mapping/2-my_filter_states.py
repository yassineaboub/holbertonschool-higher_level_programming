#!/usr/bin/python3
"""script that takes in an argument and displays all values"""
import MySQLdb
from sys import argv
if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("""SELECT id, name FROM states WHERE name = '{}' ORDER
              BY states.id ASC""".format(argv[4]))
    res = c.fetchall()
    for row in res:
        print(row)
