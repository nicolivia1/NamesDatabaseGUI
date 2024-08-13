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
        print(genders)
        return genders
