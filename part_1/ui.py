from db_manager import ManageDB

class UI():

    manageDB = ManageDB.getInstance()


    def search_by_name(self):
        """
        This method takes user input and calls manageDB.read with the input as
        an argument
        """

        user_input = input('What is the name of the record holder you seek?\n')
        print('\n')
        rows_returned = self.manageDB.read(user_input)

        if rows_returned:
            print('\n%-20s%-20s%-20s' % ('Name', 'Country', 'Number of Catches'))
            [print('%-20s%-20s%-20i' % row) for row in rows_returned]
        else:
            print('\nNo rows match your search criteria!\n')


    def add_row(self):
        """
        This method takes user input and calls manageDB.add_row with the input
        as the method's arguments
        """
        row_name = input('Please enter the name for the record you are entering:\n')
        row_country = input('Please enter the country for the record you are entering:\n')
        row_catches = 0
        try:
            row_catches += int(input('Please enter the number of catches for the record you are entering:\n'))

        except ValueError:
            print('Error: Please be sure to enter an integer for the number of catches. Row not updated.\n')
            return


        if not self.manageDB.read(row_name):
            print('\n')
            self.manageDB.add_row(row_name, row_country, row_catches)
            print('Successfully inserted row!\n')
        else:
            print('\nOops! That name is already in the database. Try removing it or updating the number of catches.\n')


    def update_catches(self):
        """
        This method takes user input and calls manageDB.read, manageDB.add_row
        and manageDB.delete with the input as the method's arguments.
        """

        name_input = input('Enter record holder name:\n')
        try:
            catches_input = int(input('Enter number of catches:\n'))
        except ValueError:
            print('Error: Please be sure to enter an integer for the number of catches. Row not updated.\n')
            return

        row_returned = self.manageDB.read(name_input)
        print('\n')
        if row_returned:
            self.manageDB.add_row(row_returned[0][0], row_returned[0][1], catches_input)
            self.manageDB.delete(name_input)
            print('Successfully updated row!\n')
        else:
            print('\nNo rows match your search criteria!')


    def delete_by_name(self):
        """
        This method takes user input and calls manageDB.read and manageDB.delete
        with the input as the method's arguments.
        """

        name_input = input('Enter the name of the record holder you would like to delete:\n')

        if self.manageDB.read(name_input):
            self.manageDB.delete(name_input)
            print('Successfully deleted row!')
        else:
            print('\nNo rows match your search criteria!')

    def exit_prog(self):
        exit()

    def incorrect_input(self):
        print('Please type a correct input option!\n')


    def menu(self):
        """
        This method simply displays the user's menu command options.
        """
        print('\nTake a look at these nice options!')
        print('1 - Search database by record holder name')
        print('2 - Add row to database')
        print('3 - Update number of catches for existing record')
        print('4 - Delete record by record holder name')
        print('0 - Exit program\n\n')

        user_input = input('')
        print('\n')

        return user_input

