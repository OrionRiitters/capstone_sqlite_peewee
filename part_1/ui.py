from db_manager import ManageDB

class UI():

    manageDB = ManageDB.getInstance()

    def add_row(self):
        

        row_name = input('Please enter the name for the record you are entering:\n')
        row_country = input('Please enter the country for the record you are entering:\n')
        row_catches = 0
        try:
            row_catches += int(input('Please enter the number of catches for the record you are entering:\n'))
        except ValueError:
            print('Error: Please be sure to enter an integer for the number of catches. Row not updated.')
            return

        self.manageDB.add_row(row_name, row_country, row_catches)
    


    def search_by_name():
        pass


    def update_catches():
        pass


    def delete_by_name():
        pass
