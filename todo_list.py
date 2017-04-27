"""This is a Terminal-based program that allows a user to create and edit a to-do list.

The stub of each function has been provided. Read the docstrings for what each 
function should do and complete the body of the functions below.

You can run the script in your Terminal at any time using the command:

    >>> python todo_list.py

"""

def add_to_list(my_list):
    """Takes user input and adds it as a new item to the end of the list."""

    list_item = raw_input("What would you like to add to the list? ")
    my_list.append(list_item)

#    print my_list
#    return my_list


def view_list(my_list):
    """Print each item in the list."""

    for item in my_list:
        print str(my_list.index(item)+1) + ". " + item

def delete_first_item(my_list):
    print "You are deleting " + my_list[0]
    del my_list[0]


def display_main_menu(my_list1):
    """Displays main options, takes in user input, and calls view or add function."""

    user_options = """
    \nWould you like to:
    A. Add a new item
    B. View list
    C. Delete first item in list
    D. Quit the program
     """

    while True:
        # Collect input and include your if/elif/else statements here.
        print user_options
        user_input = raw_input(">>> ").upper()

        if user_input == "A":
            add_to_list(my_list1)
        elif user_input == "B":
            view_list(my_list1)
        elif user_input == "C":
            delete_first_item(my_list1)
        elif user_input == "D":
            break
        else:
            print "Sorry, I don't know what you mean.  Please try again."

    

#-------------------------------------------------

my_list = []
display_main_menu(my_list)

