from peewee import *

"""
The records class defines a table and inherits from BaseModel. The Meta inner-class in BaseModel is a convention that defines the database to be used by any class inheriting from BaseModel.
"""

class BaseModel(Model):
    class Meta:
        database = SqliteDatabase('juggling_records')


class Records(BaseModel):

    name = CharField()
    country = CharField()
    catches = IntegerField()
