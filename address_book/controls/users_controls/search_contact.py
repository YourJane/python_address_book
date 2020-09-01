from address_book.controls.search_functions import *
from address_book.controls.validation_functions import validate_the_menu_action_loop
from address_book.controls.validation_functions import validate_required_fields_not_empty


def search_contact():
    menu = "1. SEARCH IN ALL FIELDS\n2. SEARCH BY NAME\n3. SEARCH BY LAST NAME"
    input_message = "Please choose the desired action by entering the number accordingly"
    action = validate_the_menu_action_loop(menu, input_message)
    search_key = validate_required_fields_not_empty("Please enter your search query.\n>>> ")
    if action == 1:
        found_contacts = search_contact_in_all_fields(search_key.capitalize().strip())
        return show_search_results(found_contacts, search_key)
    elif action == 2:
        found_contacts = search_contact_by_name(search_key.capitalize().strip())
        return show_search_results(found_contacts, search_key)
    elif action == 3:
        found_contacts = search_contact_by_last_name(search_key.capitalize().strip())
        return show_search_results(found_contacts, search_key)