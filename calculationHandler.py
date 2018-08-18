import numpy as nump
import tkinter as tk
import sqlite3 as sq
import logging
import matplotlib as mat

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

class portfolioMetric(object):
    """
    This class calculates metrics of the portfolio after closing positions
    """

    def winRate(self, closedCount, exitPrice, entryPrice, stopLoss):
        """
        Inputs:
         - closedCount (float) - the amount of closed positions currently
         - exitPrice (float) - the price at which the user has exited the trade
         - entryPrice (float) - user entered, price at which entered
         - stopLoss (float) - stopLoss (float) - user entered, maximum value to loose
        Output:
         - winRate (float) - The percentage of winning trades
        """
        count = 0
        if (stopLoss > entryPrice):
            # This is a short position
            if(exitPrice < entryPrice):
                count += 1
            elif(exitPrice > entryPrice):
                count -= 1
            else:
                logging.exception("Unknown position")
        elif(stopLoss < entryPrice):
            # This is a long position
            if(exitPrice > entryPrice):
                count += 1
            elif(exitPrice < entryPrice):
                count -= 1
            else:
                logging.exception("Unknown position")
        else:
            logging.exception("unknown exception")

        return ((count / closedCount) * 100)

    # TO DO - IMPLEMENTATION
    def averageRRR(self, closedCount, entryPrice, stopLoss, targetPrice):
        riskReward = abs((targetPrice - entryPrice)/(stopLoss - entryPrice))


    def numberTrades(self, closedCount):
        """
        Inputs:
         - closedCount (float) - The amount of closed positions (based on exit date)
        Output:
         - numberTrades (float) - The number of trades made
        """
        return closedCount

    def averageHoldingtime(self, closedPos, startDate, endDate):
        """
        Inputs:
         - closedCount (float) - the amount of closed positions currently
         - exitPrice (float) - the price at which the user has exited the trade
         - entryPrice (float) - user entered, price at which entered
         - stopLoss (float) - stopLoss (float) - user entered, maximum value to loose
        Output:
         - winRate (float) - The percentage of winning trades
        """
        if (closedPos):
            return startDate - endDate
        else:
            pass

    # def potfolioExposure(self, entryPrice, exitPrice, targetPrice, stopLoss):
    #     # The portfolio exposure is the difference in the long and the short positions
    #     if (stopLoss > entryPrice):
    #         # This is a short position
    #     elif(stopLoss < entryPrice):
    #         # This is a long position
    #     else:
    #         logging.exception("unknown exception")
    #         pass
    #     return

    def pieWeighting(self, assetClass, assetQty, entryPrice, portfolioValue):
        """
        Inputs:
         - assetClass (float) - the amount of closed positions currently
         - exitPrice (float) - the price at which the user has exited the trade
         - entryPrice (float) - user entered, price at which entered
         - stopLoss (float) - stopLoss (float) - user entered, maximum value to loose
        Output:
         - winRate (float) - The percentage of winning trades
        """
        assetDict = {'assetClass':, 'weighting': }

        assetWeighting = assetQty * entryPrice
        weighting = assetWeighting / portfolioValue

        assetDict['assetClass'] = assetClass
        assetDict['weighting'] = weighting

        return assetDict