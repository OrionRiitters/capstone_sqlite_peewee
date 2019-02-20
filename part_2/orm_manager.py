from models import Records
from peewee import *

db = SqliteDatabase('juggling_records.db')

class ManageORM():
    """
    This class uses peewee to do basic CRUD operations on a table.
    Documentation for peewee can be found at:
    http://docs.peewee-orm.com/en/latest/peewee/api.html
    """

    def __init__(self):
        db.connect()
        if not db.table_exists('Records'):
            db.create_tables([Records])
        db.close()


    def add_row(self, row_name, row_country, row_catches):
        db.connect()
        new_record = Records(name=row_name, country = row_country, catches = row_catches)
        new_record.save()
        db.close()


    def update_row(self, row_name, row_catches):
        db.connect()
        row_changed = Records.update(catches=row_catches).where(Records.name == row_name).execute()
        db.close()

    def delete_row(self, row_name):
        db.connect()
        row_deleted = Records.delete().where(Records.name == row_name).execute()
        db.close()

    def get_row(self, row_name):
        db.connect()
        query = Records.select().where(Records.name == row_name)
        db.close()
        return query
