import notebook

"""
- Deve ser possível adicionar um contato x
- Deve ser possível visualizar a lista de contatos cadastrados x
- Deve ser possível editar um contato x
- Deve ser possível marcar/desmarcar um contato como favorito x
- Deve ser possível ver uma lista de contatos favoritos x
- Deve ser possível apagar um contato
"""

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
        print("OPTION", option)

    elif option == "5":
        print("OPTION", option)

    elif option == "6":
        print("OPTION", option)

    elif option == "7":
        print("OPTION", option)

    elif option == "8":
        break

print("\nApplication closed!\n")