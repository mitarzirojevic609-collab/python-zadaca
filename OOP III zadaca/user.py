from db import DB


class User(DB):

    def __init__(self):
        super().__init__()


    def set_age(self, age):
        if age < 18:
            raise ValueError("Korisnik mora imati minimum 18 godina")

        self.__age = age

    def get_age(self, age):
        return self.__age


    def get_name(self):
        return self.__name



    def set_name(self, name):
        if len(name) < 3:
            raise ValueError("Ime mora imati minimum 3 karaktera")

        self.__name = name



mitar = User ()
mitar.set_name("Mitar")
mitar.set_age(19)
print(mitar._get_connection())



print(mitar.get_name())

