import numpy as nump
import tkinter as tk
import sqlite3 as sq
import logging

"""
Revision: 1.0
Author: Jeremiah Dufourq

Packages included:
 - numpy
 - tkinter

Notes:
This script covers the calculations for implementation in the trading journal project. There are three classes,
entryCalculation, assetLive and portfolioMetric. Each of these classes are detailed below.
"""

class entryCalculation(object):
    # This class calculates the entry position metrics for the entry ticket.
    #
    # def __init__(self, calcRRR, calcMargin):
    #     pass

    """
        Inputs:
         - entryPrice (float) - user entered, price at which entered 
         - targetPrice (float) - user entered, maximum value to win
         - stopLoss (float) - user entered, maximum value to loose
        Output:
         - calcRRR (int) - Calculated Risk Reward Value
    """
    def calcRRR(self, entryPrice, targetPrice, stopLoss):
        try:
            return abs((targetPrice - entryPrice)/(stopLoss - entryPrice))

        except ZeroDivisionError as error:
            # Output expected ZeroDivisionErrors.
            logging.error(error)

        except Exception as exception:
            # Output unexpected Exceptions.
            logging.exception("unknown exception")

    """
        Inputs:
         - entryPrice (float) - user entered, price at which entered
         - assetMargin (float) - asset specific, gathered from OANDA API
         - assetQty (float) - user entered, amount of contracts
        Output:
         - calcMargin (float) - Calculated the margin put down in dollars
    """
    def calcMargin(self, entryPrice, assetMargin, assetQty):
        return abs(entryPrice * assetMargin * assetQty)

    """
        Inputs:
         - entryPrice (float) - user entered, price at which entered
         - assetQty (float) - user entered, amount of contracts
        Output:
         - calcMarketval (float) - Calculated market value of the asset
    """
    def calcMarketval(self, entryPrice, assetQty):
        return abs(entryPrice * assetQty)

    """
        Inputs:
         - entryPrice (float) - user entered, price at which entered
         - stopLoss (float) - user entered, maximum value to loose
         - assetQty (float) - user entered, amount of contracts
        Output:
         - stoplossVal (float) - Calculated market value in dollars of the stop loss
    """
    def stoplossVal(self, entryPrice, stopLoss, assetQty):
        return abs((entryPrice - stopLoss) * assetQty)

    """
        Inputs:
         - entryPrice (float) - user entered, price at which entered
         - stopLoss (float) - user entered, maximum value to loose
         - assetQty (float) - user entered, amount of contracts
        Output:
         - stoplossPercent (float) - Calculated market value in percent of the stop loss
    """
    def stoplossPercent(self, entryPrice, stopLoss, assetQty):
        try:
            return abs((((entryPrice - stopLoss) * assetQty) / (entryPrice * assetQty)) * 100)

        except ZeroDivisionError as error:
            # Output expected ZeroDivisionErrors.
            logging.error(error)

        except Exception as exception:
            # Output unexpected Exceptions.
            logging.exception("unknown exception")

    """
        Inputs:
         - entryPrice (float) - user entered, price at which entered
         - targetPrice (float) - user entered, maximum value to win
         - assetQty (float) - user entered, amount of contracts
        Output:
         - targetVal (float) - Calculated market value in dollars of the target value
    """
    def targetVal(self, entryPrice, targetPrice, assetQty):
        return abs((targetPrice - entryPrice) * assetQty)

    """
        Inputs:
         - entryPrice (float) - user entered, price at which entered
         - targetPrice (float) - user entered, maximum value to win
         - assetQty (float) - user entered, amount of contracts
        Output:
         - targetPercent (float) - Calculated market value in percent of the target value
    """
    def targetPercent(self, entryPrice, targetPrice, assetQty):
        return abs((((targetPrice - entryPrice) * assetQty) / (entryPrice * assetQty)) * 100)
pass

# class assetLive(object):
#     # Initial variables
#     def __init__(self):
#         pass
#
#     def livePLval(self, entryPrice, currentPrice):
#         return (currentPrice - entryPrice)
#
#     def livePLpercent(self, entryPrice, currentPrice):
#         return ((currentPrice - entryPrice) / (entryPrice))
#
# # OTHER THINGS TO CALCULATE
# # - WIN RATE
# # AVERAGE -RISK TO REWARD RATIO
# # CURRENT EXPECTANCY
# # MAXIMUM CONSECUTIVE LOSS
# # MAXIMUM DRAWDOWN
# # NUMBER OF TRADES
# # PROFITABILITY
# # AVERAGE HOLDING TIME
#
#
# # PROJECT SHARPE RATIO
# # CURRENT SHARPE RATIO
#
# class portfolioMetric(object):
#
#     def winRate(self, closedCount, ):
#
#     def averageRRR(self, ):
#
#     def numberTrades(self, closedCount):
#         return closedCount
#
#     def averageHoldingtime(self, closedPos, startDate, endDate):
#         if (closedPos):
#             return startDate - endDate
#         else:
#             pass
#     def potfolioExposure(self,):
#         pass




