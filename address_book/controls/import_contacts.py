import json
import jsonpickle
import address_book
from address_book.controls.global_var import g_address_book


def import_address_book():
    with open('exported_address_book.json') as json_file:
        json_data = json.load(json_file)
        address_book.controls.global_var.g_address_book = jsonpickle.decode(json_data)
    return print("Address book was imported.")