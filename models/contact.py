class Contact:
    def __init__(self, name, phone, email, favorite=False) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.favorite = favorite
    
    def set_favorite(self):
        self.favorite = True
    
    def unset_favorite(self):
        self.favorite = False
    
    def to_string(self):
        return f"Name: {self.get_name()}\Phone: {self.get_phone()}\E-mail: {self.get_email()}\nFavorite: {self.get_favorite()}"


