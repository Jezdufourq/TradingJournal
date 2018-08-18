from db.DAO import Datastore
from db.instruments import Instrument, Asset
import sqlite3
import os

# Init Database
dbpath = 'db/tradingJournal.sqlite'
ds = Datastore(dbpath)

# Pull initial data from OANDA


# Tkinter Setup etc..


# Main Loop


ds.closeDatastore()

