#!/usr/bin/python3
"""Connects to the table states using mysqldb api"""
import MySQLdb
import sys


def access_cities():
    '''Acess_cities func'''

    username, password, database, state_name = sys.argv[1:]
    conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

    cur = conn.cursor()
    sql_query = ('SELECT name FROM cities'
    'WHERE state_id=(SELECT id FROM states WHERE name=%s)'
    'ORDER BY id ASC')
    cur.execute(sql_query, (state_name,))
    result = cur.fetchall()

    city_names = ', '.join(row[0] for row in result)
    print(city_names)

    cur.close()
    conn.close()


if __name__ == '__main__':
    access_cities()
