def address_book_menu():
    input('PRESS "ENTER" KEY TO ENTER CONTACTS MENU')
    print("<<<<<<<<<<<<<< CONTACTS MENU >>>>>>>>>>>>>>")
    print("Please enter the number of the action you want to do.")
    menu = "1. ADD NEW CONTACT\n2. UPDATE CONTACT\n3. VIEW CONTACT\n4. VIEW ALL CONTACTS\n5. DELETE CONTACT\
    \n6. SAVE ADDRESS BOOK\n7. SEARCH CONTACT\n8. EXPORT ADDRESS BOOK\n9. IMPORT ADDRESS BOOK\n0. QUIT"
    print(menu)

    menu_action = input('>>> ')
    return menu_action, menu
