from address_book.controls.view_functions import view_all
from address_book.controls.update_functions import *
from address_book.controls.validation_functions import validate_the_entered_index
from address_book.controls.validation_functions import validate_the_menu_action_loop
from address_book.controls.global_var import g_social_network_list
from address_book.controls.validation_functions import validate_social_network


def update_contact():
    list_of_contacts = view_all()
    contact_index_message = "Please enter the number of the contact you would like to edit.\n>>> "
    contact_index = validate_the_menu_action_loop(list_of_contacts, contact_index_message)

    edit_menu = "1. Name\n2. Second Name\n3. Last Name\n4. Phone\n5. Email\n6. Social account\n7. Address"
    entry_index_message = "What do you want to edit? Please choose from the list and enter the number.\n>>> "
    entry_index = validate_the_menu_action_loop(edit_menu, entry_index_message)

    menu_message_for_user = "Please choose the desired action by entering the number accordingly.\n>>> "

    if entry_index == 1:
        update_contact_name(contact_index)
    elif entry_index == 2:
        update_contact_second_name(contact_index)
    elif entry_index == 3:
        update_contact_last_name(contact_index)
    elif entry_index == 4:
        if len(g_address_book[contact_index].phone) == 1:
            menu = "1. ADD NEW PHONE\n2. UPDATE EXISTING"
        else:
            menu = "1. ADD NEW PHONE\n2. UPDATE EXISTING\n3. DELETE PHONE"
        action = validate_the_menu_action_loop(menu, menu_message_for_user)
        if action == 1:
            update_contact_phone_add_new(contact_index)
        elif action == 2:
            phone_index = validate_the_entered_index(contact_index, "phone", "Which phone you want to edit?\n>>> ")
            update_contact_phone_edit(contact_index, phone_index)
        elif action == 3:
            phone_index = validate_the_entered_index(contact_index, "phone", "Which phone you want to delete?\n>>> ")
            update_contact_phone_delete(contact_index, phone_index)
    elif entry_index == 5:
        if hasattr(g_address_book[contact_index], "email"):
            menu = "1. ADD NEW EMAIL\n2. UPDATE EXISTING\n3. DELETE EMAIL "
            action = validate_the_menu_action_loop(menu, menu_message_for_user)
        else:
            action = 1
        if action == 1:
            update_contact_email_add_new(contact_index)
        elif action == 2:
            if len(g_address_book[contact_index].email) > 0:
                input_message = "Which email you want to edit?\n>>> "
                email_index = validate_the_entered_index(contact_index, "email", input_message)
                update_contact_email_edit(contact_index, email_index)
            else:
                print("There is no email to edit for this contact")
        elif action == 3:
            if len(g_address_book[contact_index].email) > 0:
                input_message = "Which email you want to delete?\n>>> "
                email_index = validate_the_entered_index(contact_index, "email", input_message)
                update_contact_email_delete(contact_index, email_index)
            else:
                print("There is no email to delete for this contact")

    elif entry_index == 6:
        print("LEN", len(g_address_book[contact_index].social_account))
        if len(g_address_book[contact_index].social_account) == 1:
            menu = "1. ADD NEW SOCIAL ACCOUNT\n2. UPDATE EXISTING"
        else:
            menu = "1. ADD NEW SOCIAL ACCOUNT\n2. UPDATE EXISTING\n3. DELETE EXISTING"
        action = validate_the_menu_action_loop(menu, menu_message_for_user)
        if action == 1:
            social_network_list = ""
            for i in range(0, len(g_social_network_list)):
                social_network_list += "{0}. {1}\n".format(i, g_social_network_list[i])
            input_message = "Please enter the number of the social network you want to add.\n>>> "
            add_social_network_index = validate_the_menu_action_loop(social_network_list, input_message)
            update_social_account(contact_index, g_social_network_list[add_social_network_index])
        elif action == 2:
            input_message = "Please enter the social network name you would like to edit.\n>>> "
            key = validate_social_network(contact_index, input_message)
            update_social_account(contact_index, key)
        elif action == 3:
            input_message = "Please enter the social network name you would like to delete.\n>>> "
            key = validate_social_network(contact_index, input_message)
            update_social_account_delete(contact_index, key)
    elif entry_index == 7:
        if hasattr(g_address_book[contact_index], "address_street"):
            menu = "1. UPDATE CITY\n2. UPDATE STREET\n3. UPDATE ADDRESS\n4. DELETE STREET"
            action = validate_the_menu_action_loop(menu, menu_message_for_user)
        else:
            menu = "1. UPDATE CITY\n2. UPDATE STREET\n3. UPDATE ADDRESS"
            action = validate_the_menu_action_loop(menu, menu_message_for_user)
        if action == 1:
            update_contact_city(contact_index)
        elif action == 2:
            update_contact_street(contact_index)
        elif action == 3:
            update_contact_city(contact_index)
            update_contact_street(contact_index)
        elif action == 4:
            update_contact_street_delete(contact_index)