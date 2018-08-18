import numpy as nump
import tkinter as tk
import sqlite3 as sq
import statistics as stats
import pyfolio as pyf
import math as mt

# The entry ticket is denoted by the date at which it was entered
class entryCalculation(object):
    # Initial variables
    def __init__(self, calcRRR, calcMargin):
        pass
    
    def calcRRR(self, entryPrice, targetPrice, stopLoss):
        return abs((targetPrice - entryPrice)/(stopLoss - entryPrice))

    def calcMargin(self, entryPrice, assetMargin, assetQty):
        return abs(entryPrice * assetMargin * assetQty)
    
    def calcMarketval(self, entryPrice, assetQty):
        return abs(entryPrice * assetQty)
    
    def stoplossVal(self, entryPrice, stopLoss, assetQty):
        return abs((entryPrice - stopLoss) * assetQty)
    
    def stoplossPercent(self, entryPrice, stopLoss, assetQty):
        return abs(((entryPrice - stopLoss) * assetQty) / (entryPrice * assetQty))

    def targetVal(self, entryPrice, targetPrice, assetQty):
        return abs((targetPrice - entryPrice) * assetQty)
    
    def targetPercent(self, entryPrice, targetPrice, assetQty):
        return abs((targetPrice - entryPrice) * assetQty)
pass

class assetLive(object):
    # Initial variables
    def __init__(self):
        pass
    
    def livePLval(self, entryPrice, currentPrice):
        return (currentPrice - entryPrice)
    
    def livePLpercent(self, entryPrice, currentPrice):
        return ((currentPrice - entryPrice) / (entryPrice))
    
    def liveRisk(self, currentPrice, entryPrice):
        return
pass

class portfolioCalculation(object):
    
    def __init__(self):
        pass
    
    def accountValue(self, ):