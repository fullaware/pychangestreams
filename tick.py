from pymongo import MongoClient
import urllib.parse
import time

username=urllib.parse.quote_plus('test')
password=urllib.parse.quote_plus('test')

client = MongoClient('mongodb+srv://%s:%s@192.168.33.188' % (username,password))
db = client.test

# db.tick.update({_id:1},{$inc:{tick:1}, $currentDate:{modified:{$type:"date"}}},true)

count = 1

while count != 0:
    db.tick.update({'_id':1},{'$inc':{'tick':-1}, '$currentDate':{'modified':{'$type':'date'}}},True);
    time.sleep(1)
