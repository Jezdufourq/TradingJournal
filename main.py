from db.DAO import Datastore
from configparser import ConfigParser
from db.instruments import Instrument, Asset
import sqlite3
import os

# Init Database
conf = {
    'dbpath' : '',
    'apikey' : '',
    'apiAccNumber' : '',
    'lastInstrumentUpdate' : ''
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
    except:
        print("there was an error reading the config file. I would give deets but... You'll get over it.")
else:
    # build default config file
    config = ConfigParser()
    config.read('config.ini')
    config.add_section('db')
    config.add_section('api')
    config.add_section('instruments')
    config.set('db', 'path', 'tradingJournal.sqlite')
    config.set('api', 'apikey', '8f46dc882fe2a2500612be3e94abb7d6-fbe8d2e0d101bad62069e441852444c4')
    config.set('api', 'account', '')
    config.set('instruments', 'lastUpdate', '0')
    with open('config.ini', 'w') as f:
        config.write(f)

ds = Datastore(conf['dbpath'])

# Check age of last
# Pull initial data from OANDA



# Tkinter Setup etc..


# Main Loop


ds.closeDatastore()

