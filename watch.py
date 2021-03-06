from pymongo import MongoClient
import pprint
import urllib.parse

username=urllib.parse.quote_plus('test')
password=urllib.parse.quote_plus('test')

client = MongoClient('mongodb+srv://%s:%s@192.168.33.188' % (username,password))

db = client['sensorlog']

with db.sensors.watch(full_document='updateLookup') as change_stream:
    for document in change_stream:
        pprint.pprint(document)
