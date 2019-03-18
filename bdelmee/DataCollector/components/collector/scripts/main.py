import bitmexStream
import database
import time

if __name__ == '__main__':

    try:
        database = database.Database()
        stream = bitmexStream.Stream(database)
        
        while True:
            time.sleep(1000)

    except KeyboardInterrupt:
        print('\nInterrupt received, stopping...')
        stream.close()
        database.close()