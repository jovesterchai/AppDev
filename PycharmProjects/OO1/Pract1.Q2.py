class Customer:
    def __init__(self, customer_id, name):
        self.__customer_id = ""
        self.__customer_id = customer_id
        self.__name = name

    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def set_customer_id(self, customer_id):
        if len(customer_id) == 5:
            if customer_id[-1].isalpha():
                self.__customer_id = customer_id

    def display_details(self):
        print("===== Customer Details =====")
        print("Customer ID: ", self.__customer_id)
        print("Customer Name: ", self.__name)


c1 = Customer("1234A", "Andrea Tan")
c1.display_details()

c2 = Customer("7895", "Lee Chit Boon")
c2.display_details()

c3 = Customer("7895B", "Lee Chit Boon")
c3.display_details()
