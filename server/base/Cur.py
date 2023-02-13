from peewee import *


class LoginModel(Model):
    us = TextField(unique=True)
    pw = TextField()
    aka = TextField()
    por = TextField()
    dt = DateTimeField()

    class Meta:
        table_name = "login"
