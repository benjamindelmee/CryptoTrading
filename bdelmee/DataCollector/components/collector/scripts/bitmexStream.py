import websocket
import threading
import time
import json

class Stream(threading.Thread):

    url = 'xwss://www.bitmex.com/realtime?subscribe=trade:XBTUSD'

    def __init__(self, database):
        super(Stream, self).__init__()
        self._init(database)
        self.start()

    def _init(self, database):
        self._database = database
        self._closed = False
        self._ws = websocket.WebSocketApp(Stream.url,
            on_message=self._on_message,
            on_close=self._on_close,
            on_open=self._on_open,
            on_error=self._on_error
        )

    def close(self):
        self._closed = True
        self._ws.close()
        self.join()

    # no need to call this method by yourself
    # automatically executed into a new thread
    def run(self):
        while True:
            self._ws.run_forever()            
            
            if self._closed:
                # user interrupted the connection... leave
                break
            else:
                print('BitMEX: impossible to connect. Trying again in 5s...')
                time.sleep(5)  # TODO: implement an incremental sleep

    def _on_message(self, message):
        data = json.loads(message)
        # TODO
        # # self._database.writeTrade(data['data'])

    def _on_error(self, error):
        print('BitMEX: ' + str(error))

    def _on_close(self):
        print("BitMEX: disconnected")

    def _on_open(self):
        print("BitMEX: connected")