class Contact:
    def __init__(self, name, phone, email, favorite=False) -> None:
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__favorite = favorite
    
    def get_name(self):
        return self.__name
    
    def get_phone(self):
        return self.__phone
    
    def get_email(self):
        return self.__email
    
    def get_favorite(self):
        return self.__favorite
    
    def set_favorite(self):
        self.__favorite = True
    
    def unset_favorite(self):
        self.__favorite = False
    
    def to_string(self):
        return f"Name: {self.get_name()}\Phone: {self.get_phone()}\E-mail: {self.get_email()}\nFavorite: {self.get_favorite()}"


