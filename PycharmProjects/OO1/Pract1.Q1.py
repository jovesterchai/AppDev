class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age


name = input("Enter pet name: ")
type = input("Enter pet type: ")
age = int(input("Enter age of pet: "))

pet = Pet(name, type, age)

print("Pet %s is a %s, and it is %i years old." % (pet.get_name(), pet.get_animal_type(), pet.get_age()))
