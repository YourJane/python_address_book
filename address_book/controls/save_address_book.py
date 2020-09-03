import re


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
    for i in range(0, len(address_book)):
        with open(full_file_name, 'w') as f:
            print(address_book[i], file=f)
    return print("Address book is saved in {} file.".format(full_file_name))