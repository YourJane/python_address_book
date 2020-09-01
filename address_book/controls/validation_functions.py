import re
from address_book.controls.global_var import error_message_out_of_range
from address_book.controls.global_var import error_message_on_alpha
from address_book.controls.global_var import g_address_book
from address_book.controls.global_var import g_social_network_list


def validate_the_menu_action(menu_action, menu):
    only_digits_menu = re.sub('\D', '', menu)
    if not menu_action.isnumeric():
        print(error_message_on_alpha)
    elif menu_action not in only_digits_menu:
        print(error_message_out_of_range)
    else:
        menu_action = int(menu_action)
    return menu_action


def validate_the_entered_index(contact_index, contact_attribute, input_message):
    values_list = ""
    for v in getattr(g_address_book[contact_index], contact_attribute):
        values_list += "{0}. {1}\n".format(getattr(g_address_book[contact_index], contact_attribute).index(v), v)
    while True:
        print(values_list)
        value_index = validate_the_menu_action(input(input_message), values_list)
        if type(value_index) == int:
            break
        else:
            continue
    return value_index


def validate_the_menu_action_loop(menu, input_message):
    while True:
        print(menu)
        menu_action = validate_the_menu_action(input(input_message), menu)
        if type(menu_action) == int:
            break
        else:
            continue
    return menu_action


def validate_social_network(contact_index, input_message):
    social_key_value_list = ""
    social_key_list = ""
    for key, value in g_address_book[contact_index].social_account.items():
        social_key_value_list += "{0}: {1}\n".format(key, value)
        social_key_list += "{}, ".format(key)

    while True:
        print(social_key_value_list)
        social_network_to_update = input(input_message)

        if social_network_to_update not in social_key_list and social_network_to_update not in g_social_network_list:
            print("The social network you have entered is not supported in our program.")
            continue
        elif social_network_to_update not in social_key_list and social_network_to_update in g_social_network_list:
            print("You have entered social network that contact doesn't have")
            continue
        else:
            return social_network_to_update


def validate_email_value(input_message):
    while True:
        email = input(input_message).strip().lower()
        if len(email) < 1:
            break
        elif not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            print("Email validation failed: make sure you have entered 1 symbol '@', there is at least 1 '.' after it ")
            continue
        else:
            break

    return email


def validate_required_fields_not_empty(input_message):
    while True:
        required_value = input(input_message)
        if required_value.isspace() or required_value == "":
            print("This field is required, please enter the value.")
        else:
            break

    return required_value
