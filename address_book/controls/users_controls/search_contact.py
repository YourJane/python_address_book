from address_book.controls.search_functions import *
from address_book.controls.validation_functions import validate_the_menu_action_loop
from address_book.controls.validation_functions import validate_required_fields_not_empty
from address_book.controls.global_var import answer_yes
from address_book.controls.global_var import answer_no
from address_book.controls.global_var import error_message_for_answer
from address_book.controls.global_var import value_for_yes_no_validation


def search_contact(address_book):
    menu = "1. SEARCH IN ALL FIELDS\n2. SEARCH BY NAME\n3. SEARCH BY LAST NAME"
    input_message = "Please choose the desired action by entering the number accordingly.\n>>> "
    action = validate_the_menu_action_loop(menu, input_message)
    search_key = validate_required_fields_not_empty("Please enter your search query.\n>>> ")
    print("Do you what to search for a full match with entered query?")
    while value_for_yes_no_validation not in answer_yes + answer_no:
        is_full_search = input("Please enter Y/Д/Т to search for a full match, and N/Н to use partial search.\n>>> ")
        if is_full_search in answer_yes:
            found_contacts = search_contact_by_attr_values(search_key, address_book, action, True)
            break
        elif is_full_search in answer_no:
            found_contacts = search_contact_by_attr_values(search_key, address_book, action, False)
            break
        else:
            print(error_message_for_answer)
            continue

    return show_search_results(found_contacts, search_key)
