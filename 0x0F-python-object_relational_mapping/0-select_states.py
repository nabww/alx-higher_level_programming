#!/usr/bin/python3
#python script to select all occurences of the states in the table states

import sys
import MySQLdb

if __name__ == "___main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
