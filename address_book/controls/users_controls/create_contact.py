from address_book.controls.contact import Contact
from address_book.controls.global_var import g_social_network_list
from address_book.controls.validation_functions import validate_email_value
from address_book.controls.validation_functions import validate_required_fields_not_empty
from address_book.controls.validation_functions import validate_the_menu_action_loop


def create_contact(address_book):
    name = validate_required_fields_not_empty("*Name: ").capitalize().strip()
    last_name = validate_required_fields_not_empty("*Last Name: ").capitalize().strip()
    second_name = input("Second Name: ").capitalize().strip()
    phone = validate_required_fields_not_empty("*Phone: ").strip()
    email = validate_email_value("Email: ")
    city = validate_required_fields_not_empty("*City: ").capitalize().strip()
    address_street = input("Street: ").capitalize().strip()

    social_network_list = ""
    print("Pick social network to add:\n")
    for i in range(0, len(g_social_network_list)):
        social_network_list += ("{0}. {1}\n".format(i, g_social_network_list[i]))
    input_message = 'Please enter the number of the social network you want to add: '
    social_network_choice = validate_the_menu_action_loop(social_network_list, input_message)
    social_network = g_social_network_list[social_network_choice]
    social_network_account = validate_required_fields_not_empty("*Account in named social network: ").strip().lower()
    social_account = {social_network: social_network_account}

    address_book.append(Contact(
        name,
        last_name,
        [phone],
        social_account,
        city,
        **{"second_name": second_name, "address_street": address_street, "email": [email]}
    ))
    return print("Contact saved")