#!/usr/bin/python3
"""Connects to the table states using mysqldb api"""
import MySQLdb
import sys


def search_name():
    username, password, database, state_name = sys.argv[1:]
    conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            passwd=password,
            db=database
        )

    cur = conn.cursor()
    sql_query = ("SELECT * FROM states "
    "WHERE name='{}' "
    "ORDER BY id").format(state_name)

    cur.execute(sql_query)
    result = cur.fetchall()

    for row in result:
        print(row)

    cur.close()
    conn.close()


if __name__ == '__main__':
    search_name()
