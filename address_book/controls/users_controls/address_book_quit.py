from address_book.controls.global_var import answer_yes
from address_book.controls.global_var import answer_no
from address_book.controls.global_var import error_message_for_answer
from address_book.controls.save_address_book import save_address_book
from address_book.controls.global_var import value_for_yes_no_validation


def address_book_quit(address_book):
    if len(address_book) > 0:
        print("Do you want to save the address book before quiting the program?")
        while value_for_yes_no_validation not in answer_yes + answer_no:
            save_before_quit = input("Please enter Y/Д/Т for yes and N/Н for no.\n>>> ")
            if save_before_quit in answer_yes:
                save_address_book(address_book)
                break
            elif save_before_quit in answer_no:
                break
            else:
                print(error_message_for_answer)
                continue

    return print(">>> Program ended")
