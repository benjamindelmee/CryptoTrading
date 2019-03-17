import websocket
import psycopg2

import database

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

    database = database.Database()

    database.writeTrade('2019-03-16T17:47:47.558Z', 'XBTUSD', 'Buy', '190.5', '3982.5')

    database.close()