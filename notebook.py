from models.contact import Contact

contacts = []

def add_contact(name, phone, email, favorite=False):
    contact =  Contact(name, phone, email, favorite)
    contacts.append(contact)
    return

def list_contacts():
    for contact in contacts:
        print(contact.to_string())

def list_favorites():
    for contact in contacts:
        if contact.get_favorite():
            contact.to_string()

def edit_contact(index, name, phone, email, favorite=False):
    relative_index  = int(index) - 1
    contact = contacts[relative_index]
    contact.name = name if name else contact.name
    contact.phone = phone if phone else contact.phone
    contact.email = email if email else contact.email
    contact.favorite = favorite if favorite else contact.favorite

    
