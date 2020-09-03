import json
import jsonpickle


def export_address_book(address_book):
    with open("exported_address_book.json", "w") as outfile:
        address_book_in_json = jsonpickle.encode(address_book, unpicklable=True)
        json.dump(address_book_in_json, outfile)
        print(address_book_in_json)
    return print("Address book was exported.")