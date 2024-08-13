class Database:
    _connection = None

    @classmethod
    def fetch_names(cls):
        from ShowNames import ShowNames

        return [
            ShowNames("Marc")
        ]