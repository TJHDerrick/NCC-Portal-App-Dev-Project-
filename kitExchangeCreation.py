from datetime import datetime


class Creation:
    sizes_dict = {
     'S': 'Small', 'M': 'Medium', 'L': 'Large'
    }
    id = 0

    def __init__(self, name, description, sizes, location):
        Creation.id += 1
        self.__id = Creation
        self.__name = name
        self.__description = description
        self.__sizes = sizes
        self.__location = location
        self.__datetime_created = datetime.now()
        self.__datetime_updated = datetime.now()

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_sizes(self):
        return self.__sizes

    def get_location(self):
        return self.__location

    def set_name(self, name):
        self.__name = name

    def set_description(self, description):
        self.__description = description

    def set_sizes(self, sizes):
        self.__sizes = sizes

    def set_sizes(self, location):
        self.__location = location


creation = Creation("name", "description", "sizes", "location")
print(creation.get_description())
