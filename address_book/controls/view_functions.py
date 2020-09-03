def is_empty(list_to_check):
    if len(list_to_check) == 0:
        print("There is no contacts in your address book.")
        return True
    return False


def view_all(address_book):
    list_of_all_contacts = ""
    print("CONTACTS SAVED: ")
    for i in range(0, len(address_book)):
        list_of_all_contacts += "{0}. {1} {2}\n".format(i, address_book[i].name, address_book[i].last_name)
    return list_of_all_contacts


def view_contact(address_book, index=0):
    print("Name: {}".format(address_book[index].name))
    if address_book[index].second_name:
        print("Second name: {}".format(address_book[index].second_name))
    print("Last Name: {}".format(address_book[index].last_name))
    for i in range(0, len(address_book[index].phone)):
        print("Phone: {}".format(address_book[index].phone[i]))
    if hasattr(address_book[index], "email") and len(address_book[index].email) > 0:
        for i in range(0, len(address_book[index].email)):
            print("Email: {}".format(address_book[index].email[i]))
    print("Social accounts:")
    for key, value in address_book[index].social_account.items():
        print("{0}: {1}".format(key, value))
    if hasattr(address_book[index], "address_street") and len(address_book[index].address_street) > 1:
        print("Address: {0}, {1}".format(address_book[index].address_street, address_book[index].city))
    else:
        print("Address: {}".format(address_book[index].city))

    return None
