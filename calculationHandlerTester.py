
# import calculationHandler.py
from calculationHandler import entryCalculation


entryPrice = 10
targetPrice = 12
stopLoss = 9
assetMargin = 0.3
assetQty = 10

calculationH = entryCalculation()

print("calc RRR", calculationH.calcRRR(entryPrice, targetPrice, stopLoss))

print("calc Margin", calculationH.calcMargin(entryPrice, assetMargin, assetQty))

print("calc Marketval", calculationH.calcMarketval(entryPrice, assetQty))

print("stoploss Val", calculationH.stoplossVal(entryPrice, stopLoss, assetQty))

print("stoploss percent", calculationH.stoplossPercent(entryPrice, stopLoss, assetQty))

print("target val", calculationH.targetVal(entryPrice, targetPrice, assetQty))

print("target percent", calculationH.targetPercent(entryPrice, targetPrice, assetQty))




