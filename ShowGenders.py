from Database import Database

class Show:

    #Name, Gender, Year, NameCount
    def __init__(self, Name, Gender, Year, NameCount, Total):
        self.__name = Name
        self.__gender = Gender
        self.__year = Year
        self.__name_count = NameCount
        self.__total = Total

    def get_name(self):
        return self.__name
    def get_gender(self):
        return self.__gender
    def get_year(self):
        return self.__year
    def get_count(self):
        return self.__name_count
    def get_total(self):
        return self.__total

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
