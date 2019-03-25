import psycopg2
import queue
import threading
import time
import os

# decorator
def _connected_to_database(f):
        def wrapper(*args, **kwargs):
            args[0]._ensure_connection()
            return f(*args, **kwargs)
        return wrapper

class Database(threading.Thread):
    """Database abstraction used to insert data

    When a call to a writeXXX() function is made, the data is put into a queue
    and inserted asynchronously into the database (quickly after). When the method
    close() is called, all the data in the queue are inserted into the database and
    the connection is closed.
    """
    
    def __init__(self):
        super(Database, self).__init__()
        self._init()
        self.start()
    
    def _init(self):
        # queue to store the insert orders
        self._queue = queue.Queue(maxsize=5000)

        # database connection parameters
        # fallback values are used for development only
        self._host = os.getenv('DB_HOST', '127.0.0.1')
        self._dbname = os.getenv('DB_NAME', 'bitmex')
        self._user = os.getenv('DB_USER', 'user')
        self._password = os.getenv('DB_PASSWORD', '3hGQv25CRdQQb8Cy')

        # connector the database
        self._conn = None

        # tell if the connection must be considered as closed
        self._closed = False

    def writeTrade(self, timestamp, symbol, side, size, price):
        if not self._closed:
            self._queue.put({
                'type': 'trade',
                'data': {
                    'timestamp': timestamp,
                    'symbol': symbol,
                    'side': side,
                    'size': size,
                    'price': price
                }
            })

    def close(self):
        if self._closed:
            # do not execute if already closed
            return
        else:
            self._closed = True
            # wait for the last insertions to be performed
            self.join()
            if self._conn:
                self._conn.close()
                print('Dabase: disconnected')

    # no need to call this method by yourself
    # automatically executed into a new thread
    @_connected_to_database
    def run(self):
        while not self._closed:
            try:
                item = self._queue.get(block=True, timeout=1)
                if item['type'] == 'trade':
                    self._writeTrade(item)
            except queue.Empty:
                if self._closed:
                    # empty queue and thread waiting to be closed... leave
                    break
    
    @_connected_to_database
    def _writeTrade(self, trade):
        with self._conn.cursor() as cursor:
            cursor.execute('INSERT INTO trades (timestamp, symbol, side, size, price) VALUES (%(timestamp)s, %(symbol)s, %(side)s, %(size)s, %(price)s)', {
                'timestamp': trade['data']['timestamp'],
                'symbol': trade['data']['symbol'],
                'side': trade['data']['side'],
                'size': trade['data']['size'],
                'price': trade['data']['price']
            })
            self._conn.commit()

    def _ensure_connection(self):

        # bug in psycopg2: the .closed attribute isn't updated when the connection is close by the server
        # patch: begin
        try:
            if self._conn != None:

                # do a random operation
                # if an error is raised, then the connexion is closed
                self._conn.poll()

                # if this code is reached, the connexion is open
                monkey_patch = False

            else:
                monkey_patch = True

        except psycopg2.OperationalError:
            monkey_patch = True
        # patch: end

        #while not self._closed and (self._conn == None or self._conn.closed != 0):
        while not self._closed and (self._conn == None or monkey_patch):  # if not already connected
            try:
                self._conn = psycopg2.connect(
                    host=self._host,
                    dbname=self._dbname,
                    user=self._user,
                    password=self._password
                )
                print('Database: connected')
                monkey_patch = False
            except psycopg2.Error as err:
                print('Database: {} impossible to connect. Trying again in 5s...'.format(type(err)))
                time.sleep(5)