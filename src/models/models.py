import datetime

import peewee

from .base import BaseModel

class Location(BaseModel):
    latitude   = peewee.DecimalField  (null = False)
    longitude  = peewee.DecimalField  (null = False)
    created_on = peewee.DateTimeField (null = True, default = lambda : datetime.datetime.utcnow())
    name       = peewee.TextField     (null = False)
