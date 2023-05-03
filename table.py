import db_connect as db
import mysql.connector
from colorama import init as initColor, Fore, Back
from createTable import getSQLcreate

import function, commonSettings as cs
initColor(autoreset=True)

class Tabele():

    @classmethod
    def showTables(cls):
        try:
            mydb = mysql.connector.connect(**db.dbconnect)
            mycursor = mydb.cursor()
            mycursor.execute("SHOW TABLES")
            tmpList = mycursor.fetchall()
            mydb.close()
            list1 = []
            for lis in tmpList:
                list1.append(lis[0])
            print(cs.userColor + "Dostępne tabele:")
            print(f"{cs.userColor}{list1}")
        except:
            print(cs.userColor + "Nie udało się połączyć z bazą danych")
            pass

    @classmethod
    def openTable(cls):
        print(cs.userColor + "Podaj nazwe tabeli do otwarcia:")
        in1 = input()
        try:
            mydb = mysql.connector.connect(**db.dbconnect)
            mycursor = mydb.cursor()
            mycursor.execute("SHOW TABLES")
            tmpList = mycursor.fetchall()
            mydb.close()
            list1 = []
            for lis in tmpList:
                list1.append(lis[0])
            if in1 in list1: return in1
            else: 
                print(cs.errorColor + "Nie ma takiej tabeli w bazie danych!")
                print(cs.errorColor + f"Dostępne tabele: {list1}")
                return ""
        except:
            print(cs.errorColor + "Nie udało otworzyć tabeli lub problem z baza danych")
            return ""
                                                        
    @classmethod
    def addTable(cls):
        sql = getSQLcreate()
        try: 
            mydb = mysql.connector.connect(**db.dbconnect)
            mycursor = mydb.cursor()
            mycursor.execute(sql)
            mydb.commit()
            mydb.close()
            print(cs.okColor + "Pomyślnie dodano tabelę")
        except:
            print(cs.errorColor + "Nieprawidłowy format wprowadzonych danych - Tabela nie została utworzona")
            pass 

    @classmethod
    def deleteTabele(cls):
        print(cs.userColor + "Podaj nazwe tabeli do usunięcia")
        in1 = input(cs.userColor)
        print(Fore.RESET, end="")
        try:
            mydb = mysql.connector.connect(**db.dbconnect)
            mycursor = mydb.cursor()
            mycursor.execute(f"DROP TABLE {in1};")
            mydb.close()
            print(cs.okColor + "Pomyślnie usunięto tabelę")
        except mysql.connector.errors.ProgrammingError:
            print(cs.errorColor + "Nie ma takiej tabeli w bazie danych")

        except:
            print(cs.errorColor + "Nie udało się połączyć z bazą danych")
