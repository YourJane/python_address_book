import json
import jsonpickle


def import_address_book(g_address_book):
    with open('exported_address_book.json') as json_file:
        json_data = json.load(json_file)
        address_book = jsonpickle.decode(json_data)

        for contact in address_book:
            g_address_book.append(contact)

    print("Address book was imported.")
