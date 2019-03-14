'use strict';


/**
 * Get CandleStick past data
 * Access this route to get specific account info using userID
 *
 * crypto String Crypto chart needed
 * step String can be 1d, 1h, 5m, 1m
 * dateStart String Date of the first candlestick
 * dateStop String Date of the last candlestick
 * returns CandlestickData
 **/
exports.candlesticksCryptoStepDateStartDateStopGET = function(crypto,step,dateStart,dateStop) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "volume" : 3585886.5,
  "high" : 116.51,
  "low" : 115.75,
  "close" : 116.02,
  "open" : 115.85
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}

