#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s ORDER BY id ASC", (argv[4],))
    query_rows = cur.fetchall()
    print(", ".join(city[1] for city in query_rows))
    cur.close()
    conn.close()
