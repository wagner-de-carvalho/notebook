import notebook

while True:
    print("========== Notebook ==========")
    print("""---------- Menu ----------
1 - Add a new contact
2 - List all contacts
3 - List favorite contacts
4 - Edit contact
5 - Add to favorite
6 - Delete from favorite
7 - Delete contact
8 - Exit ->
===============================
         """)
    option = input("Choose one option: ")
    if option == "1":
        name = input("Insert a name: ")
        phone = input("Insert a phone: ")
        email = input("Insert an e-mail: ")
        notebook.add_contact(name, phone, email)

    elif option == "2":
        print("\n******** Contacts ********")
        notebook.list_contacts()
        print("****************************\n")

    elif option == "3":
        print("\n******** Favorites ********")
        notebook.list_favorites()
        print("****************************\n")

    elif option == "4":
         print("\n******** Contacts ********")
         contacts = notebook.list_contacts()

         if contacts > 0:
             index = input("Update this contact: ")
             name = input("Contact new name: ")
             phone = input("Contact new phone: ")
             email = input("Contact new e-mail: ")
             notebook.edit_contact(index, name, phone, email)

    elif option == "5":
        print("\n******** Contacts ********")
        not_favorites = notebook.list_not_favorites()

        if not_favorites > 0:
            index = input("Add this contact to favorite list: ")
            notebook.add_to_favorites(index)

    elif option == "6":
        print("\n******** Contacts ********")
        favorites = notebook.list_favorites()

        if favorites > 0:
            index = input("Remove this contact from favorites: ")
            notebook.remove_from_favorites(index)

    elif option == "7":
        print("\n******** Contacts ********")
        contacts = notebook.list_contacts()

        if contacts > 0:
            index = input("Delete this contact: ")
            notebook.delete_contact(index)

    elif option == "8":
        break

print("\nApplication closed!\n")