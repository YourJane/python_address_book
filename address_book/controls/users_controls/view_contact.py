from address_book.controls.view_functions import view_all
from address_book.controls.view_functions import view_contact
from address_book.controls.validation_functions import validate_the_menu_action_loop


def view_contacts_info(address_book):
    list_of_contacts = view_all(address_book)
    input_message = "Please enter the number of the contact you would like to view.\n>>> "
    contact_index = validate_the_menu_action_loop(list_of_contacts, input_message)
    return view_contact(address_book, contact_index)
