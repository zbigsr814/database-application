import mysql.connector
from prettytable import PrettyTable
from colorama import init as initColor, Fore, Back

import db_connect as db, commonSettings as cs

initColor(autoreset=True)

class Login():
    @classmethod
    def changeHost(cls):
        in1 = ""
        while in1=="":
            in1 = input(cs.userColor + "Podaj nowego hosta: ")
        db.dbconnect["host"] = in1

    @classmethod
    def changeUser(cls):
        in1 = ""
        while in1=="":
            in1 = input(cs.userColor + "Podaj nowego usera: ")
        db.dbconnect["user"] = in1

    @classmethod
    def changePasswd(cls):
        in1 = ""
        while in1=="":
            in1 = input(cs.userColor + "Podaj nowego hasła: ")
        db.dbconnect["password"] = in1

    @classmethod
    def changeDb(cls):
        in1 = ""
        while in1=="":
            in1 = input(cs.userColor + "Podaj nowego DB: ")
        db.dbconnect["database"] = in1

    @classmethod
    def openDb(cls):
            try:
                mydb = mysql.connector.connect(**db.dbconnect)
                print(cs.okColor + f"Połączono z bazą danych {db.dbconnect['database']}")
                mydb.close()
                return True
            except:
                print(cs.errorColor + "Nie udało sie połączyć z bazą danych")
                return False