from address_book.controls.validation_functions import validate_email_value
from address_book.controls.validation_functions import validate_required_fields_not_empty


def update_contact_name(contact_index, address_book):
    new_value: str = validate_required_fields_not_empty("New Name: ").capitalize().strip()
    address_book[contact_index].name = new_value


def update_contact_last_name(contact_index, address_book):
    new_value: str = validate_required_fields_not_empty("New Last Name: ").capitalize().strip()
    address_book[contact_index].last_name = new_value


def update_contact_second_name(contact_index, address_book):
    new_value: str = input("New Second Name: ").capitalize().strip()
    address_book[contact_index].second_name = new_value


def update_contact_email_add_new(contact_index, address_book):
    new_value = validate_email_value("Add new email: ")
    address_book[contact_index].email.append(new_value)


def update_contact_email_edit(contact_index, email_index, address_book):
    new_value = validate_email_value("New email: ")
    address_book[contact_index].email[email_index] = new_value


def update_contact_email_delete(contact_index, email_index, address_book):
    del address_book[contact_index].email[email_index]


def update_contact_phone_add_new(contact_index, address_book):
    new_value = input("Add new phone: ").lower().strip()
    address_book[contact_index].phone.append(new_value)


def update_contact_phone_edit(contact_index, phone_index, address_book):
    if len(address_book[contact_index].phone) == 1:
        new_value = validate_required_fields_not_empty("New phone: ").lower().strip()
    else:
        new_value = input("New phone: ").lower().strip()
    address_book[contact_index].phone[phone_index] = new_value


def update_contact_phone_delete(contact_index, phone_index, address_book):
    address_book[contact_index].phone.pop(phone_index)


def update_contact_city(contact_index, address_book):
    new_value = input("New city: ").capitalize().strip()
    address_book[contact_index].city = new_value


def update_contact_street(contact_index, address_book):
    new_value = input("New street: ").capitalize().strip()
    address_book[contact_index].address_street = new_value


def update_contact_street_delete(contact_index, address_book):
    del address_book[contact_index].address_street


def update_social_account(contact_index, key, address_book):
    new_value = input("New account: ").lower().strip()
    address_book[contact_index].social_account[key] = new_value


def update_social_account_delete(contact_index, key, address_book):
    address_book[contact_index].social_account.pop(key)

