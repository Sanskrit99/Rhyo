from peewee import *

from root.config.PsqlConfig import psqlcf


class BaseModel(Model):
    class Meta:
        database = PostgresqlDatabase(
            'fap',
            host=psqlcf.host,
            port=psqlcf.port,
            user=psqlcf.user,
            password=psqlcf.password
        )

class LoginModel(BaseModel):
    us = TextField(unique=True)
    pw = TextField()
    aka = TextField()
    por = TextField()
    dt = DateTimeField()

    class Meta:
        table_name = "login"

