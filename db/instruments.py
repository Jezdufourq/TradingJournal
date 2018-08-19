import time
from db import DAO


class Instrument:
    code = ""
    currentPrice = None #ask
    bid = None
    spread = None
    lastUpdate = 0


    def __init__(self, instrumentCode, currentPrice=0, bid=0, spread=0, lastUpdate=0, saveOnCreate=True):
        self.code = instrumentCode
        self.currentPrice = currentPrice
        self.lastUpdate = lastUpdate
        self.bid = bid
        self.spread = spread
        if saveOnCreate:
            self.saveToDatabase()

    def updatePrice(self, bidSpreadAsk, updateTime=0):
        self.currentPrice = bidSpreadAsk[2]
        self.bid = bidSpreadAsk[0]
        self.spread = bidSpreadAsk[1]
        if updateTime == 0:
            self.lastUpdate = time.time()
        else:
            self.lastUpdate = updateTime
        self.saveToDatabase()

    def saveToDatabase(self):
        DAO.Datastore.instance.updateCreateInstrument(self)


class Asset:
    assetId       = None
    instrumentCode= None
    entryDate     = None
    entryPrice    = None
    targetPrice   = None
    stopLossPrice = None
    qty           = None
    technicals    = None
    fundamentals  = None
    commons       = None
    marginRate    = None
    exitDate      = None
    exitPrice     = None

    def __init__(self, assetParams, saveOnCreate=True):
        # check for default values and build object.
        assetParams = dict(assetParams)
        if "assetId" in assetParams:
            self.assetId = assetParams["assetId"]
        if "instrumentCode" in assetParams:
            self.instrumentCode = assetParams["instrumentCode"]
        if "entryDate" in assetParams:
            self.entryDate = assetParams["entryDate"]
        if "entryPrice" in assetParams:
            self.entryPrice = assetParams["entryPrice"]
        if "targetPrice" in assetParams:
            self.targetPrice = assetParams["targetPrice"]
        if "stopLossPrice" in assetParams:
            self.stopLossPrice = assetParams["stopLossPrice"]
        if "qty" in assetParams:
            self.qty = assetParams["qty"]
        if "technicals" in assetParams:
            self.technicals = assetParams["technicals"]
        if "fundamentals" in assetParams:
            self.fundamentals = assetParams["fundamentals"]
        if "commons" in assetParams:
            self.commons = assetParams["commons"]
        if "marginRate" in assetParams:
            self.marginRate = assetParams["marginRate"]
        if "exitDate" in assetParams:
            self.exitData = assetParams["exitDate"]
        if "exitPrice" in assetParams:
            self.exitPrice = assetParams["exitPrice"]


        #check for save on create and insert/update
        if saveOnCreate:
            self.saveToDatabase()

    def saveToDatabase(self):
        DAO.Datastore.instance.updateCreateAsset(self)

