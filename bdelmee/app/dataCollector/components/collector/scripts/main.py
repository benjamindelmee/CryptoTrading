import websocket
import psycopg2
import os

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    print("### opened ###")

if __name__ == '__main__':

    # url = 'wss://www.bitmex.com/realtime?subscribe=trade:XBTUSD'

    # ws = websocket.WebSocketApp(url,
    #     on_message=on_message,
    #     on_close=on_close,
    #     on_open=on_open,
    #     on_error=on_error
    # )

    # ws.run_forever()

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