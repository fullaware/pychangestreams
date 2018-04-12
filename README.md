# pychangestreams

Quick code sample showing Python interacting with MongoDB 3.6 Change Stream feature looking for any updates to a collection.


https://docs.mongodb.com/manual/changeStreams/index.html


Tested with Python 3
Requires pymongo and dnspython

Execute `python3 tick.py` to create a collection in the test database with a `modified` field that's ISODate and a `tick` field that will increment every second.

In a separate window, execute `python3 watch.py`.

You'll see a similar update stream:

```
{'_id': {'_data': b'\x82Z\xcf\xb3/\x00\x00\x00\x14F\x1e_id\x00+\x02\x00Z\x10'
                  b'\x04\x93Q5\xb2\x9eBFe\xbc\xf5H\xee\xc1V\xeb\x9d\x04',
         '_typeBits': b'\x01'},
 'documentKey': {'_id': 1.0},
 'fullDocument': {'_id': 1.0,
                  'modified': datetime.datetime(2018, 4, 12, 19, 27, 43, 125000),
                  'tick': 322.0},
 'ns': {'coll': 'tick', 'db': 'test'},
 'operationType': 'update',
 'updateDescription': {'removedFields': [],
                       'updatedFields': {'modified': datetime.datetime(2018, 4, 12, 19, 27, 43, 125000),
                                         'tick': 322.0}}}
```
