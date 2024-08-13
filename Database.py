class Database:
    _connection = None

    @classmethod
    def fetch_genders(cls):
        from ShowGenders import ShowGenders

        return [
            ShowGenders("Male"),
            ShowGenders("Female")
        ]
