import sqlite3
import os
from db.instruments import Instrument, Asset

class Datastore:
    class __Datastore:
        def __init__(self, dbpath):
            print("dbpath = ", dbpath)
            if os.path.isfile(dbpath):
                self.db = sqlite3.connect(dbpath)
                self.db.row_factory = sqlite3.Row
                print("Using database at path: ", dbpath)
            else:
                self.db = sqlite3.connect(dbpath)
                self.db.row_factory = sqlite3.Row
                self.generateNewDatabase()
                print("Existing database not found. Generating new one at path: ", dbpath)

        def generateNewDatabase(self):
            cursor = self.db.cursor()
            cursor.execute('''
                CREATE TABLE instruments(
                    code TEXT PRIMARY KEY,
                    currentPrice   REAL,
                    bid            REAL,
                    spread         REAL,
                    lastUpdate     INTEGER    
                )
            ''')
            cursor.execute('''
                CREATE TABLE assets(
                    assetId INTEGER PRIMARY KEY,
                    instrumentCode TEXT,
                    entryDate      INTEGER,
                    entryPrice     REAL,
                    targetPrice    REAL,
                    stopLossPrice  REAL,
                    qty            Integer,
                    technicals     TEXT,
                    fundamentals   TEXT,
                    commons        TEXT,
                    marginRate     REAL,
                    exitDate       REAL,
                    exitPrice      REAL,
                    FOREIGN KEY(instrumentCode) REFERENCES instruments(code)
                )
            ''')
            self.db.commit()

        def updateCreateInstrument(self, instrument):
            """
            Will insert instrument into database or create it if it does not exist.
            :param instrument: instance of instrument object.
            :return: instrumentId or -1 on failure
            """
            cursor = self.db.cursor()
            cursor.execute('''SELECT code FROM instruments WHERE code = ?''', (instrument.code,))
            data = cursor.fetchone()
            if instrument.code is None:
                return -1

            if data is None:
                print("Creating new instrument: ", instrument.code)
                cursor.execute('''
                        INSERT INTO instruments(code, currentPrice, bid, spread, lastUpdate)
                        VALUES (?,?,?,?,?)''', (instrument.code, instrument.currentPrice, instrument.bid, instrument.spread, instrument.lastUpdate))
                returnCode = cursor.lastrowid
            else:
                print("Updating existing instrument: ", instrument.code)
                if instrument.currentPrice == 0:
                    print("Did not update instrument with 0 price.")
                    returnCode = -1
                else:
                    cursor.execute('''
                            UPDATE instruments SET 
                            currentPrice =?, 
                            lastUpdate =? ,
                            bid =?,
                            spread = ?
                            WHERE code =? ''', (instrument.currentPrice, instrument.lastUpdate, instrument.bid, instrument.spread, instrument.code)
                                   )
                    returnCode = cursor.lastrowid
            self.db.commit()
            cursor.close()
            return returnCode

        def getInstrument(self, instrumentCode):
            """
            Gets instrument from sqlite database. Will return none if instrument code not found.
            :param instrumentCode:
            :return: instrument
            """
            cursor = self.db.cursor()
            cursor.execute('''SELECT * FROM instruments WHERE code=?''', (instrumentCode,))
            data = cursor.fetchone()
            if data is not None:
                inst = Instrument(data[0], data[1], data[2], False)
                cursor.close()
                return inst
            else:
                cursor.close()
                return None

        def getInstruments(self):
            """
            Gets all instruments from sqlite database. Will return none if no instruments found.
            :param instrumentCode:
            :return: instrument
            """
            cursor = self.db.cursor()
            cursor.execute('''SELECT * FROM instruments''')
            data = []
            for asset in cursor.fetchall():
                data.append(dict(asset))
            if len(data) < 1:
                return None
            return data

        def updateCreateAsset(self, theAsset):
            """
            Inserts new asset into database if assetId does not exist.
            If assetId exists database will update matching row.
            :param theAsset:
            :return: assetId or -1 on failure
            """
            id = None
            cursor = self.db.cursor()
            cursor.execute('''SELECT assetId FROM assets WHERE assetId = ?''', (theAsset.assetId,))
            data = cursor.fetchone()
            if data is None:
                print("Creating new asset")
                if(theAsset.instrumentCode is None):
                    print("Failed to create new asset. Instrument code IS REQUIRED")
                    return -1

                #Ensure foreign key exists
                cursor.execute('''SELECT code FROM instruments WHERE code = ?''', (theAsset.instrumentCode,))
                data = cursor.fetchone()
                if(data is None):
                    print("Failed to create new asset. Instrument code does not exist in database")
                    return -1
                cursor.execute('''
                        INSERT INTO assets(instrumentCode, 
                                           entryDate,
                                           entryPrice,
                                           targetPrice,
                                           stopLossPrice,
                                           qty,
                                           technicals,
                                           fundamentals,
                                           commons,
                                           marginRate,
                                           exitDate,
                                           exitPrice)
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''',
                        (theAsset.instrumentCode, theAsset.entryDate,
                         theAsset.entryPrice, theAsset.targetPrice,
                         theAsset.stopLossPrice, theAsset.qty, theAsset.technicals,
                         theAsset.fundamentals, theAsset.commons, theAsset.marginRate,
                         theAsset.exitDate, theAsset.exitPrice))
                id = cursor.lastrowid
            else:
                print("Updating existing asset: ", theAsset.assetId)
                cursor.execute('''
                        UPDATE assets SET
                        entryDate =?,
                        entryPrice =?,
                        targetPrice =?,
                        stopLossPrice =?,
                        qty =?,
                        technicals =?,
                        fundamentals =?,
                        commons =?,
                        marginRate =?,
                        exitDate =?,
                        exitPrice =?
                        WHERE assetId = ?''', (theAsset.entryDate,
                         theAsset.entryPrice, theAsset.targetPrice,
                         theAsset.stopLossPrice, theAsset.qty, theAsset.technicals,
                         theAsset.fundamentals, theAsset.commons, theAsset.marginRate,
                         theAsset.exitDate, theAsset.exitPrice, theAsset.assetId)
                       )
                id = theAsset.assetId
            self.db.commit()
            cursor.close()
            return id




        def getAsset(self, assetId):
            """
            Gets asset from sqlite database. Will return none if assetId not found.
            :param assetId:
            :return: Asset
            """
            cursor = self.db.cursor()
            cursor.execute('''SELECT * FROM assets WHERE assetId=?''', (assetId,))
            data = cursor.fetchone()
            if data is not None:
                asset = Asset(data, False)
                cursor.close()
                print("Asset ID = ", asset.assetId)
                return asset
            else:
                cursor.close()
                return None

        def deleteAsset(self, assetId):
            """
            will delete and asset from the journal.
            :param assetId:
            :return: True on success False on failure
            """
            cursor = self.db.cursor()
            success = True
            try:
                cursor.execute('''DELETE FROM assets WHERE assetId=?''', (assetId,))
                self.db.commit()
            except:
                success = False
            finally:
                cursor.close()
                return success

        def getClosedAssets(self):
            """
            Gets all currently closed assets from database;
            :return:
            """
            cursor = self.db.cursor()
            cursor.execute('''SELECT * FROM assets WHERE exitDate > 0''')
            closedAssets = []
            for asset in cursor.fetchall():
                closedAssets.append(dict(asset))
            return closedAssets


        def closeDatastore(self):
            self.db.close()

    instance = None
    def __init__(self, dbpath):
        if not Datastore.instance:
            Datastore.instance = Datastore.__Datastore(dbpath)
        else:
            Datastore.instance.val = dbpath

    def __getattr__(self, name):
        return getattr(self.instance, name)
