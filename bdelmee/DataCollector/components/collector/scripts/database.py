import psycopg2
import queue
import threading

class database(threading.Thread):
    
    def __init__(self):
        super.__init__(self)
        self._init()
        self.start()
    
    def _init(self):
        self.queue = queue.Queue(maxsize=5000)
        self.conn_string = "host='{host}' dbname='{dbname}' user='{user}' password='{password}'".format(
            # fallback values are used for development only
            host = os.getenv('DB_HOST', '127.0.0.1'),
            dbname = os.getenv('DB_NAME', 'db'),
            user = os.getenv('DB_USER', 'user'),
            password = os.getenv('DB_PASSWORD', '3hGQv25CRdQQb8Cy')
        )
    
    def run(self):
        while True:
            item = self.queue.get(block=True)
            if item['type'] == 'trade':
                _writeTrade(item)

    def writeTrade(self, timestamp, symbol, side, size, price):
        self.queue.put({
            'type': 'trade',
            'data': {
                'timestamp': timestamp,
                'symbol': symbol,
                'side': side,
                'size': size,
                'price': price'
            }
        })
    
    @_connected_to_database
    def _writeTrade(self, trade):
        self.cursor.execute('INSERT INTO trades (timestamp, symbol, side, size, price) VALUES (%(timestamp)s, %(symbol)s, %(side)s, %(size)s, %(price)s)', {
            'timestamp': trade['data']['timestamp'],
            'symbol': trade['data']['symbol'],
            'side': trade['data']['side'],
            'size': trade['data']['size'],
            'price': trade['data']['price']
        })
        self.conn.commit()

    def _connect(self):
        # TODO: loop until connected
        
        # # get a connection, if a connect cannot be made an exception will be raised here
        # conn = psycopg2.connect(conn_string)

        # # conn.cursor will return a cursor object, you can use this cursor to perform queries
        # cursor = conn.cursor()
        pass

    def _connected_to_database(f):
        def wrapper(*args, **kwargs):
            args[0]._connect()
            return f(*args, **kwargs)
        return wrapper