from address_book.controls.global_var import g_address_book


def search_contact_in_all_fields(search_key):
    found_contacts = []
    for index in range(0, len(g_address_book)):
        for key in g_address_book[index]:
            if g_address_book[index][key] == search_key:
                found_contacts.append(g_address_book[index])
    return found_contacts


def search_contact_by_name(search_key):
    found_contacts = []
    for i in range(0, len(g_address_book)):
        if g_address_book[i].name == search_key:
            found_contacts.append(g_address_book[i])
    return found_contacts


def search_contact_by_last_name(search_key):
    found_contacts = []
    for i in range(0, len(g_address_book)):
        if g_address_book[i].last_name == search_key:
            found_contacts.append(g_address_book[i])
    return found_contacts


def show_search_results(found_contacts, search_key):
    results = ""
    if len(found_contacts) == 0:
        return print("No contacts were found on '{}'".format(search_key))
    else:
        print("Search results on '{}'".format(search_key))
        for i in range(0, len(found_contacts)):
            results += ("{0}. {1} {2}\n".format(i, found_contacts[i].name, found_contacts[i].last_name))
    return print(results)
