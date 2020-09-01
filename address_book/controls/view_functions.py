from address_book.controls.global_var import g_address_book


def is_empty(list_to_check):
    if len(list_to_check) == 0:
        print("There is no contacts in your address book.")
        return True
    return False


def view_all():
    list_of_all_contacts = ""
    print("CONTACTS SAVED: ")
    for i in range(0, len(g_address_book)):
        list_of_all_contacts += "{0}. {1} {2}\n".format(i, g_address_book[i].name, g_address_book[i].last_name)
    return list_of_all_contacts


def view_contact(index=0):
    print("Name: {}".format(g_address_book[index].name))
    if g_address_book[index].second_name:
        print("Second name: {}".format(g_address_book[index].second_name))
    print("Last Name: {}".format(g_address_book[index].last_name))
    for i in range(0, len(g_address_book[index].phone)):
        print("Phone: {}".format(g_address_book[index].phone[i]))
    if hasattr(g_address_book[index], "email") and len(g_address_book[index].email) > 0:
        for i in range(0, len(g_address_book[index].email)):
            print("Email: {}".format(g_address_book[index].email[i]))
    print("Social accounts:")
    for key, value in g_address_book[index].social_account.items():
        print("{0}: {1}".format(key, value))
    if hasattr(g_address_book[index], "address_street") and len(g_address_book[index].address_street) > 1:
        print("Address: {0}, {1}".format(g_address_book[index].address_street, g_address_book[index].city))
    else:
        print("Address: {}".format(g_address_book[index].city))

    return None