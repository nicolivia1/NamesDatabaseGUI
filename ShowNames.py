from Database import Database

class ShowNames:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self.get_name()

    @staticmethod
    def fetch_names():
        return Database.fetch_names()


class Gender:
    pass
