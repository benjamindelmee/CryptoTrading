'use strict';

var utils = require('../utils/writer.js');
var CandleSticksData = require('../service/CandleSticksDataService');

module.exports.candlesticksCryptoStepDateStartDateStopGET = function candlesticksCryptoStepDateStartDateStopGET (req, res, next) {
  var crypto = req.swagger.params['crypto'].value;
  var step = req.swagger.params['step'].value;
  var dateStart = req.swagger.params['dateStart'].value;
  var dateStop = req.swagger.params['dateStop'].value;
  CandleSticksData.candlesticksCryptoStepDateStartDateStopGET(crypto,step,dateStart,dateStop)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
