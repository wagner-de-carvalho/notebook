from models.contact import Contact

contacts = []

def add_contact(name, phone, email, favorite=False):
    contact =  Contact(name, phone, email, favorite)
    contacts.append(contact)
    print(f"{contact.name} added as a new contact!")
    return

def list_contacts():
    for contact in contacts:
        print(contact.to_string() + "\n")

def list_favorites():
    for contact in contacts:
        if contact.get_favorite():
            print(contact.to_string() + "\n")

def edit_contact(index, name, phone, email, favorite=False):
    relative_index  = int(index) - 1
    if relative_index >= 0 and relative_index < len(contacts):
        contacts[relative_index].name = name if name else contacts[relative_index].name
        contacts[relative_index].phone = phone if phone else contacts[relative_index].phone
        contacts[relative_index].email = email if email else contacts[relative_index].email
        contacts[relative_index].favorite = favorite if favorite else contacts[relative_index].favorite

    print(f"{contacts[relative_index].name} updated!")

def delete_contact(index):
    relative_index  = int(index) - 1
    name = ""
    if relative_index >= 0 and relative_index < len(contacts):
        contact = contacts[relative_index]
        name = contact.name
        contacts.remove(contact)

    print(f"Contact {name} deleted!")

def set_as_favorite(index):
    relative_index  = int(index) - 1
    if relative_index >= 0 and relative_index < len(contacts):
        contacts[relative_index].set_favorite()

def unset_as_favorite(index):
    relative_index  = int(index) - 1
    if relative_index >= 0 and relative_index < len(contacts):
        contacts[relative_index].unset_favorite()

    
