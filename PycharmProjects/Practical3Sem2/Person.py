class Person:
    def __init__(self, name, nric):
        self.__name = name
        self.__nric = nric

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_nric(self):
        return self.__nric

    def __str__(self):
        return self.__name
