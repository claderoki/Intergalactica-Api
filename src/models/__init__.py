from .base import BaseModel
from .poll import Poll, Vote, Option
database = Poll._meta.database

with database:
    # database.create_tables([Translation, NamedEmbed])
    # database.create_tables([Human, GlobalHuman, RankRole, Settings, EmojiUsage])
    
    database.create_tables([Poll, Option, Vote])
