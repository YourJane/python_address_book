import re
import jsonpickle


def save_address_book(address_book):
    while True:
        file_name = input("How do you what to name the file?\n>>> ")
        if re.fullmatch(r"^[^*&%\s]+$", file_name):
            break
        else:
            print("The filename you have provided is invalid. Please make sure your file doesn't contains /"
                      "'*','&', '&' and spaces.")
            continue
    full_file_name = file_name+".txt"
    address_book_in_json = jsonpickle.encode(address_book, unpicklable=True)
    for i in range(0, len(address_book_in_json)):
        with open(full_file_name, 'w') as f:
            print(address_book_in_json, file=f)
    return print("Address book is saved in {} file.".format(full_file_name))