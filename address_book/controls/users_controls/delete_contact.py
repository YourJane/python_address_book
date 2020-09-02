from address_book.controls.view_functions import view_all
from address_book.controls.validation_functions import validate_the_menu_action_loop


def delete_contact(address_book):
    list_of_contacts = view_all(address_book)
    input_message = "Which contact you want to delete? Please enter the number of that contact."
    contact_index = validate_the_menu_action_loop(list_of_contacts, input_message)
    del address_book[contact_index]
    return print("Contact deleted")