# CandleStick Data scrapper API v0.1

### Purpose

The purpose of this project is to design an API intended to be used by a AI to make algorithm backtestings.

### Data format

Candlestick data will be stored in a local database (we shall define which database type to use) with different steps : 
1 Day candlesticks
1 Hour candlesticks
5 min candlesticks
1 min candlesticks

REQ010 - This API shall allow the user to choose any currency he wants (to be defined).
Note : /api/v01/btcusd/

REQ020 - This API shall allow the user to ask for any type of candlesticks he wants in the range of 1d, 1h, 5m or 1min.
Note : api/v01/btcusd/5m

REQ030 - This API shall allow the user to ask for any period of times he wants.
Note : api/v01/btcusd/5m/20190103/20191403

REQ040  : The API shall outputs data in JSON object containing following information : Open, close, high, low, volume.