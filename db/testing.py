from DAO import Datastore
from instruments import Instrument, Asset
import time

dbpath = 'tradingJournal.sqlite'


ds = Datastore(dbpath)

print("creating new instrument")
ds.updateCreateInstrument(Instrument("EUR_USD", 5.33, 1000, False))
inst2 = Instrument("USD_AUD", 9.2, 10000)
inst = ds.getInstrument("EUR_USD")
print("Found Instrument: ", inst.currentPrice)

#Creating a new Asset
firstAsset = Asset({"assetId" : 1,"instrumentCode" : "EUR_USD", "entryDate" : 1234, "entryPrice" : 5.68, "targetPrice" : 9,
                                "stopLossPrice" : "2", "qty": 600})

firstAsset.exitPrice = 755
firstAsset.saveToDatabase()

assetId = ds.updateCreateAsset(firstAsset)

asst = ds.getAsset(assetId)
asst.exitDate = time.time()
asst.saveToDatabase()

print(asst.assetId, asst.instrumentCode)
#print(ds.deleteAsset(asst.assetId))
asst.exitDate = 9999
asst.saveToDatabase()

for theAsset in ds.getClosedAssets():
    print(theAsset)

for theInstrument in ds.getInstruments():
    print(theInstrument)

ds.closeDatastore()