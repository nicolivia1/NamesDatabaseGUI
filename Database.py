# Imports
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
        from ShowGenders import Show

        sql = """
        SELECT TOP 50 Name, Gender, Year, NameCount
        FROM all_data
        WHERE Gender = ? AND Name = ?
        ORDER BY Year ASC
        """

        cls.connect()
        cursor = cls.__connection.cursor()
        cursor.execute(sql, gender, name_entry)
        shows = []
        show = cursor.fetchone()
        while show:
            shows.append(Show(show[0], show[1], show[2], show[3]))
            show = cursor.fetchone()
        return shows

