import pyodbc


class Database:
    __connection = None

    @classmethod
    def connect(cls):
        if cls.__connection is None:
                server = "cisdbss.pcc.edu"
                username = "275student"
                password = "275student"
                database = "NAMES"
                cls.__connection = pyodbc.connect(
                    "DRIVER={ODBC Driver 18 for SQL Server};SERVER=" + server +
                    ";DATABASE=" + database + ";UID=" + username + ";PWD=" + password +
                    ";TrustServerCertificate=yes"
                )

    @classmethod
    def fetch_genders(cls):
        from ShowGenders import ShowGenders

        sql = '''
        SELECT DISTINCT Gender
        from all_data
        '''

        cls.connect()
        cursor = cls.__connection.cursor()
        cursor.execute(sql)
        genders = []
        gender = cursor.fetchone()
        while gender:
            genders.append(ShowGenders(gender[0]))
            gender = cursor.fetchone()
        return genders

    @classmethod
    def fetch_names(cls, gender, name_entry):
        from ShowGenders import NameInfo, ShowGenders

        sql = """
        SELECT TOP 50 Name, Gender, Year, NameCount, Total
        FROM all_data
        WHERE Name = ?
        """

        if gender != ShowGenders.ALL_GENDERS:
            sql = sql + """
            AND Gender = ?
            """

        sql = sql + """
        ORDER BY Year DESC;
            """

        cls.connect()
        cursor = cls.__connection.cursor()

        if gender != ShowGenders.ALL_GENDERS:
            cursor.execute(sql, name_entry, gender)
        else:
            cursor.execute(sql, name_entry)
        shows = []
        show = cursor.fetchone()
        while show:
            shows.append(NameInfo(show[0], show[1], show[2], show[3], show[4]))
            show = cursor.fetchone()
        return shows
