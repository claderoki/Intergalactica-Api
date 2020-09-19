import datetime
from enum import Enum

import peewee
import discord
import playhouse.pool
from emoji import emojize

import src.config as config
from .fields import EmojiField
from .base import BaseModel

# db = playhouse.pool.PooledMySQLDatabase("polls_db", max_connections=32, stale_timeout=300, **config.mysql)

class Poll(BaseModel):
    anonymous = True

    question        = peewee.TextField       ()
    due_date        = peewee.DateTimeField   (default = lambda : datetime.datetime.now() + datetime.timedelta(days = 2))
    guild_id        = peewee.BigIntegerField ()
    author_id       = peewee.BigIntegerField ()
    type            = peewee.TextField       (default = "single")
    message_id      = peewee.BigIntegerField (null = True)
    channel_id      = peewee.BigIntegerField (null = True)
    ended           = peewee.BooleanField    (default = False)

    @property
    def due_date_passed(self) -> bool:
        current_date = datetime.datetime.now()
        return current_date >= self.due_date


class Option(BaseModel):
    poll     = peewee.ForeignKeyField (Poll, backref = "options")
    value    = peewee.TextField       ()
    reaction = EmojiField             ()

class Vote(BaseModel):
    user_id  = peewee.BigIntegerField ()
    option   = peewee.ForeignKeyField (Option, backref = "votes")


