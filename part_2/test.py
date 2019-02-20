from orm_manager import ManageORM

manager = ManageORM()

[print(row.catches) for row in manager.get_row('adsf')]
