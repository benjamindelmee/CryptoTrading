import psycopg2
import os

if __name__ == '__main__':

    conn_string = "host='{host}' dbname='{dbname}' user='{user}' password='{password}'".format(
        host = os.getenv('DB_HOST', '127.0.0.1'),
        dbname = 'bitmex',
        user = 'user',
        password = '3hGQv25CRdQQb8Cy'
    )

    host = os.getenv('DB_HOST', '127.0.0.1')

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    print("Connected!\n")