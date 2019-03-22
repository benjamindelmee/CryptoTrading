import bitmexStream
import database
import time
import signal
import sys

def sigHandler(signalNumber, frame):
    if signalNumber == signal.SIGTERM:
        end()
    else:
        pass

def end():
    print('\nInterrupt received, stopping...')
    stream.close()
    database.close()
    sys.exit(0)


if __name__ == '__main__':

    try:
        database = database.Database()
        stream = bitmexStream.Stream(database)

        signal.signal(signal.SIGTERM, sigHandler)

        while True:
            time.sleep(1000)

    except KeyboardInterrupt:
        end()