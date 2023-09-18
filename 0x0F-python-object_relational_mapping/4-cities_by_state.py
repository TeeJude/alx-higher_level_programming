i#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    a = db.cursor()
    a.execute("SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id")
    rows = a.fetchall()
    for row in rows:
        print(row)
    a.close()
    db.close()
