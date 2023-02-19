"""
2023 © MySQL Class , Sikrox Memer
Created To Provide A Much Beginner 
Starting Pack To Interact With MySQL
Connector . As Long As The User Know
How To Use Structered Querry Language
It Will Make It Easier To Use This Class
"""

import mysql.connector

class MySQL(object):
    """
    MySQL Class Object Maker To Establish Good \n
    Connection Between Python And MySQL Server \n
    To Execute SQL Inside Python Functions Or More..\n
    Syntax:\n
    Object = MySQL(
        host : String,
        password : Integer,
        user : String,
        database: String
    );
    """

    def __init__(self, host: str, password: str, user: str, database:str=None):
        try:
            self.__host = host
            self.__password = password
            self.__user = user
            self.__database = database
            self.db = mysql.connector.connect(
                host=self.__host,
                password=self.__password,
                user=self.__user,
                database=self.__database,
            )
        except mysql.connector.Error as err:
            print(
                f"You Have An Error In Your mySQL Connection Information\n ERROR : {err}")
            exit(1)

    def __Connect(self):
        """
        Connect Or Test If There Is A Connection Between \n
        Python And MySQL \n
        Syntax :
        Object.Connect() -> Connection Adress
        """
        try:
            print(self.db)
        except mysql.connector.Error as err:
            return f"CONNECTION ERROR : {err}"

    @property
    def __MySQLQuickValues(self):
        """
        Retrun MySQL Connection Informations
        (Privet)
        """
        database = {
            'host': self.__database,
            'user': self.__user,
            'password': self.__password,
            'database': self.__database
        }
        for values in database:
            print(values)
        pass
    pass

    def Execute(self, SQL: str):
        """
        Function : Run A Querry Statement Inside Your Python Code \n
        Syntax : \n
        Object.Execute(strict : default = False , SQL) \n
        strict Mode Turns Your SQL Statement To Upper \n
        SQL.upper()
        """
        try:
            Cursor = self.db.cursor()
            Cursor.execute(f'{SQL}')
            for Info in Cursor:
                print(Info)
        except mysql.connector.Error as err:
            print(f"SQL ERROR : {err}")

    def __str__(self):
        from datetime import datetime
        return f"<MySQL Class Object  At {hex(id(MySQL()))}>\n<Created At {datetime.now()}>"
    """
    def __del__(self):
        from os import getcwd
        return f"<MySQL Class Object Deleted From {getcwd()}>"
    """
    pass


pass

"""
Object = MySQL(host='localhost' , password='789456123Simo11' , user='root')
Object.Execute(SQL='CREATE DATABASE IF NOT EXISTS MOHAMED;')
"""
