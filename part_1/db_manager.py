import sqlite3

class ManageDB():
    """
    This class accesses and modifies an sqlite database. Implements the singleton class pattern from https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
    """

    __instance = None

    @staticmethod
    def getInstance():

        if ManageDB.__instance == None:
            ManageDB()
        return manageDB.__instance


    def __init__(self):
        """Creates singleton instance and creates table in the db if one isn't present."""
        if ManageDB.__instance != None:
            raise Exception("You can't do that! This is a singleton.")
        else:
            ManageDB.__instance = self
            try:
                db = sqlite3.connect('juggling_records')
                cur = db.cursor()
                with db:
                    cur.execute('Create table if not exists records (name text, country text, catches int)')
            except sqlite3.Error as e:
                print('Error creating database..')
                print(e)
            finally:
                db.close()

    def add_row(self, row_name, row_country, row_catches):
        try:
            db = sqlite3.connect('juggling_records')
            cur = db.cursor()
            with db:
                cur.execute('Create table if not exists records (name text, country text, catches int)')
        except sqlite3.Error as e:
            print('Error creating database..')
            print(e)
        finally:
            db.close()

    def read():
        pass


    def update():
        pass


    def delete():
        pass

