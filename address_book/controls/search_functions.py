
def _value_matches(value, search_key, is_full_match):
    if is_full_match:
        return value == search_key

    return search_key in value


def _find_match(contact, search_key, is_full_match):
    for attribute in dir(contact):
        if callable(attribute) or attribute.startswith('__'):
            continue

        value = getattr(contact, attribute)

        # if it's a dictionary, let's extract the values and check them
        if isinstance(value, dict):
            for key in value:
                if _value_matches(value[key], search_key, is_full_match):
                    return True
        # if it's a list, let's loop through the values and check them
        elif isinstance(value, list):
            for sub_value in value:
                if _value_matches(sub_value, search_key, is_full_match):
                    return True
        # otherwise just check the value
        else:
            if _value_matches(value, search_key, is_full_match):
                return True

    return False


def search_contact_by_attr_values(search_key, address_book, search_type, is_full_match=True):
    found_contacts = []

    if search_type == 1:
        for contact in address_book:
            if _find_match(contact, search_key.casefold().strip(), is_full_match):
                found_contacts.append(contact)
        return found_contacts
    elif search_type == 2:
        for i in range(0, len(address_book)):
            if _value_matches(address_book[i].name, search_key.capitalize().strip(), is_full_match):
                found_contacts.append(address_book[i])
        return found_contacts
    elif search_type == 3:
        for i in range(0, len(address_book)):
            if _value_matches(address_book[i].last_name, search_key.capitalize().strip(), is_full_match):
                found_contacts.append(address_book[i])
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
