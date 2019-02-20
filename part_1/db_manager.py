import sqlite3

class ManageDB():
    """
    This class accesses and modifies an sqlite database. Implements the singleton class pattern
    from https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
    This singleton pattern is  unnecessary but it works and I don't have time to un-implement it.
    These methods are all pretty self-explanatory so I will not be writing comments for each of
    them.
    """

    __instance = None

    @staticmethod
    def getInstance():

        if ManageDB.__instance == None:
            ManageDB()
        return ManageDB.__instance


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
                    cur.execute('CREATE TABLE IF NOT EXISTS records (name text, country text, catches int)')
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
                cur.execute('INSERT INTO records VALUES (?, ?, ?)', (row_name, row_country, row_catches))
        except sqlite3.Error as e:
            print('Error inserting row (it was not updated).')
        finally:
            db.close()


    def read(self, input):

        upper_input = input.upper()
        row_list = []

        try:
            db = sqlite3.connect('juggling_records')
            cur = db.cursor()
            with db:
                for row in cur.execute('SELECT * FROM records WHERE UPPER(name) like ?', [upper_input]):
                    row_list.append(row)

            return row_list

        except sqlite3.Error as e:
            print('Error: Could not read rows.')
            print(e)

        finally:
            db.close()


    def delete(self, input):

        upper_input = input.upper()

        try:
            db = sqlite3.connect('juggling_records')
            cur = db.cursor()
            with db:
                cur.execute('DELETE FROM records WHERE UPPER(name) like ?', [upper_input])


        except sqlite3.Error as e:
            print('Error: Could not delete row.')
            print(e)

        finally:
            db.close()

