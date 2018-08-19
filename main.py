from db.DAO import Datastore
from configparser import ConfigParser
import time
from db.instruments import Instrument, Asset
import sqlite3
import api.make_requests as req
import os
from math import ceil

# Init conf defaults
conf = {
    'dbpath' : 'db/tradingJournal.sqlite',
    'apikey' : '8f46dc882fe2a2500612be3e94abb7d6-fbe8d2e0d101bad62069e441852444c4',
    'apiAccNumber' : '',
    'lastInstrumentUpdate' : '0',
    'maxInstrumentRefreshInterval' : '0'
}

# Import Config from ini File if it exists
if os.path.isfile('config.ini'):
    try:
        config = ConfigParser()
        config.read('config.ini')
        conf['dbpath'] = config.get('db', 'path')
        conf['apikey'] = config.get('api', 'apikey')
        conf['apiAccNumber'] = config.get('api', 'account')
        conf['lastInstrumentUpdate'] = config.get('instruments', 'lastUpdate')
        conf['maxInstrumentRefreshInterval'] = config.get('instruments', 'maxRefreshInterval')
    except:
        print("there was an error reading the config file. I would give deets but... You'll get over it.")
else:
    # build default config file
    config = ConfigParser()
    config.read('config.ini')
    config.add_section('db')
    config.add_section('api')
    config.add_section('instruments')
    config.set('db', 'path', 'db/tradingJournal.sqlite')
    config.set('api', 'apikey', '8f46dc882fe2a2500612be3e94abb7d6-fbe8d2e0d101bad62069e441852444c4')
    config.set('api', 'account', '')
    config.set('instruments', 'lastUpdate', '0')
    config.set('instruments', 'maxRefreshInterval', '900')
    with open('config.ini', 'w') as f:
        config.write(f)

def updatePersistentInstrumentTime(lastUpdateTime):
    config = ConfigParser()
    config.read('config.ini')
    config.set('instruments', 'lastUpdate', str(updateTime))
    with open('config.ini', 'w') as f:
        config.write(f)

ds = Datastore(conf['dbpath'])
# Check age of last instruments update and pull initial data from OANDA
if (time.time() - ceil(float(conf['lastInstrumentUpdate']))) > ceil(float(conf['maxInstrumentRefreshInterval'])):
    updateTime = time.time()
    inst_data = req.get_all_pricing()
    for key in inst_data:
        Instrument(key, inst_data[key]['ask_price'], inst_data[key]['bid_price'], inst_data[key]['spread'], None, None, updateTime)
    updatePersistentInstrumentTime(updateTime)
    # reload instrumnets.

# Tkinter Setup etc..
import frontend_script

# Main Loop


ds.closeDatastore()

