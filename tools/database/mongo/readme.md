# Mongo commands

use

```
use database
```

show

```
show collections;
show tables;
```

find

```
db.collection.find();
db.collection.find({ <key>: { $exists: false }})
```

update

```
/* update one that meet the condition */
db.collection.update({ <key>: {$exists: false} }, {$set: { <key>: <value> }})

/* update all that meet the condition */
db.collection.updateMany({ <key>: { $exists: false }, { $set: { <key>: new ISODate("2020-02-02") } }})
```

distinct

```
db.colelction.distinct("<key>")
```