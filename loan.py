import uuid
from datetime import datetime
from constants import date_format, datetime_format


class Loan:
    visibility_dict = {
        'Y': 'Yes', 'N': 'No'
    }
    choice_dict = {
        '': 'Select', 'K': 'Kayak', 'P': 'Paddle', 'L': 'Lifejacket'
    }

    def __init__(self, email, number, date, choice):
        self.id = str(uuid.uuid4())
        self.__email = email
        self.__number = number
        self.__date = date
        self.__choice = choice


    def get_id(self):
        return self.id

    def get_email(self):
        return self.__email

    def get_number(self):
        return self.__number

    def get_date(self):
        return self.__date

    def get_choice(self):
        return self.__choice

    def set_email(self, email):
        self.__email = email

    def set_number(self, number):
        self.__number = number

    def set_date(self, date):
        self.__date = date

    def set_choice(self, choice):
        self.__choice = choice


loan = Loan("email", "number", "date", "choice")
