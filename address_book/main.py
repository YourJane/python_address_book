from address_book.controls.users_controls.address_book_menu import address_book_menu
from address_book.controls.users_controls.address_book_quit import address_book_quit
from address_book.controls.users_controls.create_contact import create_contact
from address_book.controls.users_controls.delete_contact import delete_contact
from address_book.controls.users_controls.view_contact import view_contacts_info
from address_book.controls.view_functions import is_empty
from address_book.controls.view_functions import view_all
from address_book.controls.users_controls.update_contact import update_contact
from address_book.controls.save_address_book import save_address_book
from address_book.controls.import_contacts import import_address_book
from address_book.controls.export_contacts import export_address_book
from address_book.controls.users_controls.search_contact import search_contact
from address_book.controls.validation_functions import validate_the_menu_action

g_address_book = []

while True:
    get_menu_action, get_menu = address_book_menu()
    menu_action = validate_the_menu_action(get_menu_action, get_menu)

    if menu_action == 0:
        address_book_quit(g_address_book)
        break
    elif menu_action == 1:
        create_contact(g_address_book)
    elif menu_action == 2:
        if is_empty(g_address_book):
            continue
        update_contact(g_address_book)
    elif menu_action == 3:
        if is_empty(g_address_book):
            continue
        view_contacts_info(g_address_book)
    elif menu_action == 4:
        if is_empty(g_address_book):
            continue
        print(view_all(g_address_book))
    elif menu_action == 5:
        if is_empty(g_address_book):
            continue
        delete_contact(g_address_book)
    elif menu_action == 6:
        if len(g_address_book) > 0:
            save_address_book(g_address_book)
        else:
            print("There is nothing to save: your address book is empty.")
    elif menu_action == 7:
        search_contact(g_address_book)
    elif menu_action == 8:
        export_address_book(g_address_book)
    elif menu_action == 9:
        import_address_book(g_address_book)


