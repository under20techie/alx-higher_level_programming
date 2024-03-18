#!/usr/bin/python3
"""Connects to the table states using mysqldb api"""
import MySQLdb
import sys

def search_name():
    username, password, database = sys.argv[1:]
    conn = MySQLdb.connect(host='localhost', port=3306, passwd=password, db=database)

    cur = conn.cursor()
    sql_query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id"
    cur.execute(sql_query)
    result = cur.fetchall()

    for row in result:
        print(row)
    cur.close()
    conn.close()

if __name__ == '__main__':
    search_name()
