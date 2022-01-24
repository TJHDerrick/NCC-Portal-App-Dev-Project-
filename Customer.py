import Person


class Customer(Person.Person):
    count_id = 0

    def __init__(self, first_name, last_name, gender, email, membership, password, confirm_password):
        super().__init__(first_name, last_name, gender, email, membership) # Did not fill up membership
        Customer.count_id += 1
        self.__customer_id = Customer.count_id
        self.__password = password
        self.__confirm_password = confirm_password

    def get_customer_id(self):
        return self.__customer_id

    def get_password(self):
        return self.__password

    def get_confirm_password(self):
        return self.__confirm_password

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_password(self, password):
        self.__password = password

    def set_confirm_password(self, confirm_password):
        self.__confirm_password = confirm_password






