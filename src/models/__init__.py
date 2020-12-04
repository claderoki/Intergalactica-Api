from .base import BaseModel
from .models import *

database = BaseModel._meta.database

with database:
    database.create_tables([Location])
