from address_book.controls.global_var import g_address_book
from address_book.controls.validation_functions import validate_email_value
from address_book.controls.validation_functions import validate_required_fields_not_empty


def update_contact_name(contact_index):
    new_value: str = validate_required_fields_not_empty("New Name: ").capitalize().strip()
    g_address_book[contact_index].name = new_value


def update_contact_last_name(contact_index):
    new_value: str = validate_required_fields_not_empty("New Last Name: ").capitalize().strip()
    g_address_book[contact_index].last_name = new_value


def update_contact_second_name(contact_index):
    new_value: str = input("New Second Name: ").capitalize().strip()
    g_address_book[contact_index].second_name = new_value


def update_contact_email_add_new(contact_index):
    new_value = validate_email_value("Add new email: ")
    g_address_book[contact_index].email.append(new_value)


def update_contact_email_edit(contact_index, email_index):
    new_value = validate_email_value("New email: ")
    g_address_book[contact_index].email[email_index] = new_value


def update_contact_email_delete(contact_index, email_index):
    del g_address_book[contact_index].email[email_index]


def update_contact_phone_add_new(contact_index):
    new_value = input("Add new phone: ").lower().strip()
    g_address_book[contact_index].phone.append(new_value)


def update_contact_phone_edit(contact_index, phone_index):
    if len(g_address_book[contact_index].phone) == 1:
        new_value = validate_required_fields_not_empty("New phone: ").lower().strip()
    else:
        new_value = input("New phone: ").lower().strip()
    g_address_book[contact_index].phone[phone_index] = new_value


def update_contact_phone_delete(contact_index, phone_index):
    g_address_book[contact_index].phone.pop(phone_index)


def update_contact_city(contact_index):
    new_value = input("New city: ").capitalize().strip()
    g_address_book[contact_index].city = new_value


def update_contact_street(contact_index):
    new_value = input("New street: ").capitalize().strip()
    g_address_book[contact_index].address_street = new_value


def update_contact_street_delete(contact_index):
    del g_address_book[contact_index].address_street


def update_social_account(contact_index, key):
    new_value = input("New account: ").lower().strip()
    g_address_book[contact_index].social_account[key] = new_value


def update_social_account_delete(contact_index, key):
    g_address_book[contact_index].social_account.pop(key)

