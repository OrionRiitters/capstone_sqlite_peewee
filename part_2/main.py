from db_manager import ManageDB
from ui import UI



def main():
    """
    Run a loop that takes user input and calls the appropriate methods of UI.
    """
    manageDB = ManageDB.getInstance()
    ui = UI()

    while True:
        user_input = ui.menu()
        switch(ui, user_input)


def switch(ui, user_input):
    """
    This function acts like a switch statement that you would find in java or another
    similar language.
    """
    dict = {
        '1': 'search_by_name',
        '2': 'add_row',
        '3': 'update_catches',
        '4': 'delete_by_name',
        '0': 'exit_prog'
    }

    if user_input in dict.keys():
        method = getattr(ui, dict.get(user_input))
        method()
    else:
        ui.incorrect_input()

main()
