import uuid
from datetime import datetime
from constants import date_format, datetime_format


class Event:
    id = 0
    visibility_dict = {
        'Y': 'Yes', 'N': 'No'
    }

    def __init__(self, title, description, start_date, end_date, time, location, visibility, image, sign_up_no):
        Event.id += 1
        self.__id = Event.id
        self.__title = title
        self.__description = description
        self.__start_date = start_date
        self.__end_date = end_date
        self.__time = time
        self.__location = location
        self.__visibility = visibility
        self.__image = image
        self.__sign_up_no = sign_up_no
        self.__datetime_created = datetime.now()
        self.__datetime_updated = datetime.now()
        self.__current_sign_up_no = 0

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

    def get_time(self):
        return self.__time

    def get_location(self):
        return self.__location

    def get_visibility(self):
        return self.__visibility

    def get_image(self):
        return self.__image

    def get_sign_up_no(self):
        return self.__sign_up_no

    def get_current_sign_up_no(self):
        return self.__current_sign_up_no

    def set_title(self, title):
        self.__title = title

    def set_description(self, description):
        self.__description = description

    def set_start_date(self, start_date):
        self.__start_date = start_date

    def set_end_date(self, end_date):
        self.__end_date = end_date

    def set_time(self, time):
        self.__time = time

    def set_location(self, location):
        self.__location = location
        print(self.__location)

    def set_visibility(self, visibility):
        self.__visibility = visibility

    def set_image(self, image):
        self.__image = image

    def set_sign_up_no(self, sign_up_no):
        self.__sign_up_no = sign_up_no

    def set_current_sign_up_no(self, current):
        self.__current_sign_up_no = current


event = Event("title", "description", "abc", "abc", "abc", "abc", "abc", "abc ", "abc")
print(event.get_description())
