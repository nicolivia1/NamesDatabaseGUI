from Database import Database

class Show:

    #Name, Gender, Year, NameCount
    def __init__(self, Name, Gender, Year, NameCount):
        self.__name = Name
        self.__gender = Gender
        self.__year = Year
        self.__name_count = NameCount

    @staticmethod
    def fetch_names(gender, name_entry):
        return Database.fetch_names(gender, name_entry)

class ShowGenders:
    ALL_GENDERS = '--Select Gender --'

    def __init__(self, gender):
        self._gender = gender

    def get_gender(self):
        return self._gender

    @staticmethod
    def fetch_genders():
        return Database.fetch_genders()


class ShowNames:
    pass
