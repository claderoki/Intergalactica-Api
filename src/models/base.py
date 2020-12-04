import os

import peewee

class BaseModel(peewee.Model):
    class Meta:
        database = peewee.MySQLDatabase(
            os.environ["mysql_db_name"],
            user     = os.environ["mysql_user"],
            password = os.environ["mysql_password"],
            host     = os.environ["mysql_host"],
            port     = int(os.environ["mysql_port"]),
        )
