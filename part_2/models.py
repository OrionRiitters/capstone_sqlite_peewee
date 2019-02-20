from peewee import *

class BaseModel(Model):
    class Meta:
        database = SqliteDatabase('juggling_records')

class Records(BaseModel):

    name = CharField()
    country = CharField()
    catches = IntegerField()
