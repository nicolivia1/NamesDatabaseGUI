from Database import Database


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
