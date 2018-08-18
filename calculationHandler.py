import numpy as nump
import tkinter as tk
import sqlite3 as sq
import logging

"""
Revision: 2.0
Author: Jeremiah Dufourq

Packages included:
 - numpy
 - tkinter

Notes:
This script covers the calculations for implementation in the trading journal project. There are three classes,
entryCalculation, assetLive and portfolioMetric. Each of these classes are detailed below.
"""

class entryCalculation(object):
    def calcRRR(self, entryPrice, targetPrice, stopLoss):
        """
            Inputs:
             - entryPrice (float) - user entered, price at which entered
             - targetPrice (float) - user entered, maximum value to win
             - stopLoss (float) - user entered, maximum value to loose
            Output:
             - calcRRR (int) - Calculated Risk Reward Value
        """
        try:
            return abs((targetPrice - entryPrice)/(stopLoss - entryPrice))
        except ZeroDivisionError as error:
            # Output expected ZeroDivisionErrors.
            logging.error(error)

        except Exception as exception:
            # Output unexpected Exceptions.
            logging.exception("unknown exception")

    def calcMargin(self, entryPrice, assetMargin, assetQty):
        """
        Inputs:
         - entryPrice (float) - user entered, price at which entered
         - assetMargin (float) - asset specific, gathered from OANDA API
         - assetQty (float) - user entered, amount of contracts
        Output:
         - calcMargin (float) - Calculated the margin put down in dollars
        """
        return abs(entryPrice * assetMargin * assetQty)

    def calcMarketval(self, entryPrice, assetQty):
        """
        Inputs:
         - entryPrice (float) - user entered, price at which entered
         - stopLoss (float) - user entered, maximum value to loose
         - assetQty (float) - user entered, amount of contracts
        Output:
         - stoplossVal (float) - Calculated market value in dollars of the stop loss
        """
        return abs(entryPrice * assetQty)

    def stoplossVal(self, entryPrice, stopLoss, assetQty):
        """
        Inputs:
         - entryPrice (float) - user entered, price at which entered
         - stopLoss (float) - user entered, maximum value to loose
         - assetQty (float) - user entered, amount of contracts
        Output:
         - stoplossPercent (float) - Calculated market value in percent of the stop loss
        """
        return abs((entryPrice - stopLoss) * assetQty)

    def stoplossPercent(self, entryPrice, stopLoss, assetQty):
        """
        Inputs:
         - entryPrice (float) - user entered, price at which entered
         - targetPrice (float) - user entered, maximum value to win
         - assetQty (float) - user entered, amount of contracts
        Output:
         - targetVal (float) - Calculated market value in dollars of the target value
        """
        try:
            return abs((((entryPrice - stopLoss) * assetQty) / (entryPrice * assetQty)) * 100)

        except ZeroDivisionError as error:
            # Output expected ZeroDivisionErrors.
            logging.error(error)

        except Exception as exception:
            # Output unexpected Exceptions.
            logging.exception("unknown exception")

    def targetVal(self, entryPrice, targetPrice, assetQty):
        """
        Inputs:
         - entryPrice (float) - user entered, price at which entered
         - targetPrice (float) - user entered, maximum value to win
         - assetQty (float) - user entered, amount of contracts
        Output:
         - targetPercent (float) - Calculated market value in percent of the target value
        """
        return abs((targetPrice - entryPrice) * assetQty)

    def targetPercent(self, entryPrice, targetPrice, assetQty):
        """
        Inputs:
         - entryPrice (float) - user entered, price at which entered
         - currentPrice (float) - current price off the asset
         - positionStatus (float) - status of the trade (LONG = 1, SHORT = 0)
         - assetQty (float) - user entered, amount of contracts
        Output:
         - closeValue (float) - market value of the closing position
        """
        return abs((((targetPrice - entryPrice) * assetQty) / (entryPrice * assetQty)) * 100)

    def closeValue(self, entryPrice, currentPrice, positionStatus, assetQty):
        """
          Inputs:
           - entryPrice (float) - user entered, price at which entered
           - currentPrice (float) - current price off the asset
           - positionStatus (float) - status of the trade (LONG = 1, SHORT = 0)
           - assetQty (float) - user entered, amount of contracts
          Output:
           - closeValue (float) - market value of the closing position
        """
        if (positionStatus):
            return((currentPrice - entryPrice) * assetQty)
        else:
            return((entryPrice - currentPrice) * assetQty)

    def closePercent(self, entryPrice, currentPrice, positionStatus, assetQty):
        """
        Inputs:
         - entryPrice (float) - user entered, price at which entered
         - currentPrice (float) - current price off the asset
         - positionStatus (float) - status of the trade (LONG = 1, SHORT = 0)
         - assetQty (float) - user entered, amount of contracts
        Output:
         - closeValue (float) - market value of the closing position
        """
        if (positionStatus):
            return((currentPrice - entryPrice) * assetQty) / (assetQty * entryPrice)
        else:
            return((entryPrice - currentPrice) * assetQty) / (assetQty * entryPrice)
pass

class assetLive(object):
    def livePLval(self, entryPrice, currentPrice):
        """
        Inputs:
         - entryPrice (float) - user entered, price at which entered
         - currentPrice (float) - current price off the asset
        Output:
         - livePLval (float) - calculates the live PL value in dollars
        """
        return (currentPrice - entryPrice)

    def livePLpercent(self, entryPrice, currentPrice):
        """
        Inputs:
         - entryPrice (float) - user entered, price at which entered
         - currentPrice (float) - current price off the asset
        Output:
         - livePLpercent (float) - calculates the live PL value in percent
        """
        return ((currentPrice - entryPrice) / (entryPrice))

# # OTHER THINGS TO CALCULATE
# # - WIN RATE
# # AVERAGE -RISK TO REWARD RATIO
# # CURRENT EXPECTANCY
# # MAXIMUM CONSECUTIVE LOSS
# # MAXIMUM DRAWDOWN
# # NUMBER OF TRADES
# # PROFITABILITY
# # AVERAGE HOLDING TIME

# # PROJECT SHARPE RATIO
# # CURRENT SHARPE RATIO

# class portfolioMetric(object):
#
#     """
#         Inputs:
#          - entryPrice (float) - user entered, price at which entered
#          - targetPrice (float) - user entered, maximum value to win
#          - assetQty (float) - user entered, amount of contracts
#         Output:
#          - targetPercent (float) - Calculated market value in percent of the target value
#     """
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




