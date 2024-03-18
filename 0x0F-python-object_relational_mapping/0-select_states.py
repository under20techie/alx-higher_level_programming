#!/usr/bin/python3
import MySQLdb
import sys
'''Connects to the table states using mysqldb api'''


username, password, database = sys.argv[1:]

def access_states():
    conn = MySQLdb.connect(host='localhost', port=3306, user=username,passwd=password, db=database)

    cur = conn.cursor()
    cur.execute('SELECT * FROM states ORDER BY states.id ASC')
    result = cur.fetchall()

    for row in result:
        print(row)

    cur.close()
    conn.close()
if __name__ == '__main__':
    access_states()
