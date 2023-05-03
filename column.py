import db_connect as db
import mysql.connector
from colorama import init as initColor, Fore, Back
from function import printTable
from createRecord import createSQLrecord

import commonSettings as cs
initColor(autoreset=True)

class Column():

    @staticmethod
    def showColumns(tab1):
        try:
            print(cs.userColor + f"W tabeli {tab1} dostępne kolumny:")
            mydb = mysql.connector.connect(**db.dbconnect)
            mycursor = mydb.cursor()
            mycursor.execute(f"SHOW COLUMNS FROM {tab1}")
            tmpList = mycursor.fetchall()
            mydb.close()
            list1 = []
            for lis in tmpList:
                list1.append(lis[0])
            print(cs.userColor + f"{list1}")
        except:
            print(cs.errorColor + "Nie udało się połączyć z bazą danych")
            pass

    @staticmethod   
    def showTable(tab1):
        try:
            print(cs.userColor + f"W tabeli {tab1} dostępne kolumny:")
            mydb = mysql.connector.connect(**db.dbconnect)
            mycursor = mydb.cursor()
            mycursor.execute(f"SELECT * FROM {tab1}")
            tmpList = mycursor.fetchall()
            mycursor.execute(f"SHOW COLUMNS FROM {tab1}")
            colNames = mycursor.fetchall()
            mydb.close()
            cName = []
            for lis in colNames:   
                cName.append(lis[0])
            printTable(cName, tmpList, cs.userColor)
        except:
            print(cs.errorColor + "Nie udało się połączyć z bazą danych")
            pass

    @staticmethod
    def showSpecifyColumn(tab1):
        print(cs.userColor + "Wpisz kolumnę którą chcesz wyświetlić: format col1,col2,...")
        in1 = input()
        if in1[-1] != ",":
            try:
                mydb = mysql.connector.connect(**db.dbconnect)
                mycursor = mydb.cursor()
                mycursor.execute(f"Select {in1} FROM {tab1}")
                tmpList = mycursor.fetchall()

                cName = []
                list1 = in1.split(",")
                for lis in list1:   
                    cName.append(lis)
                printTable(cName, tmpList, cs.userColor)

                print(cs.okColor + "Pomślnie wyświetlono kolumny")
                mydb.close()
            except mysql.connector.Error as err:
                print(cs.errorColor + f"Podano nazwę kolumny która nie występuje w tabeli")
        else:
            print(cs.errorColor + "Wyrażenie nie może kończyć się przecinkiem")

    @staticmethod
    def showSpecifyRecord(tab1):
        print(cs.userColor + "Wpisz rekord który chcesz wyświetlić wg tabela,war_w_tabeli np. id=5 : ")
        in1 = input()
        list1 = in1.split("=")
        
        if (len(list1) == 2):
            sql = f"SELECT * FROM {tab1} WHERE {list1[0]}='{list1[1]}'"
            try:
                mydb = mysql.connector.connect(**db.dbconnect)
                mycursor = mydb.cursor()
                mycursor.execute(sql)
                print(cs.okColor + sql)
                tmpList = mycursor.fetchall()

                mycursor.execute(f"SHOW COLUMNS FROM {tab1}")
                colNames = mycursor.fetchall()
                mydb.close()
                cName = []
                for lis in colNames:   
                    cName.append(lis[0])

                printTable(cName, tmpList, cs.userColor)
                print(cs.okColor + "Pomślnie wyświetlono rekord")
            except mysql.connector.Error as err:
                print(cs.errorColor + sql)
                print(cs.errorColor + "Błędnie podana nazwa kolumny lub szukanego pola")
        else:
            print(cs.errorColor + "Nie poprawny zapis, za dużo / za mało podanych elementów")

    @staticmethod
    def addRecord(tab1):
        try:
            mydb = mysql.connector.connect(**db.dbconnect)
            mycursor = mydb.cursor()
            # Wyślij zapytanie SQL do systemowej tabeli information_schema.columns
            mycursor.execute(f"SELECT COLUMN_NAME, DATA_TYPE FROM information_schema.columns WHERE table_name = '{tab1}'")

            # Pobierz wyniki i wyświetl typy danych kolumn
            list1 = mycursor.fetchall()
            print(cs.userColor + f"Wpisz rekord w formacie", end="")
            for lis in list1:
                 print(cs.userColor + f" kolumna_{lis[0]}_{lis[1]},", end="")
            print(cs.userColor + " np. 5,aaa,bbb: ")

            in1 = input()
            list2 = in1.split(",")
            if len(list1) == len(list2):
                for lis in range(len(list1)):
                    lname, ltype = list1[lis]
                    if ltype == "int":
                        try:
                            list2[lis] = int(list2[lis])
                        except:
                            pass
                    if list2[lis] != "":
                        if not ((ltype == "int" and type(list2[lis]) == int) or (ltype == "varchar" and type(list2[lis]) == str)):
                            raise ValueError(cs.errorColor + "Niepoprawny typ danych wpisany do rekordu") 
            else:
                raise ValueError(cs.errorColor + "Ilość wpisanych zmiennych zbyt mała lub duża") 

            sql = createSQLrecord(tab1, list2)
            mycursor.execute(sql)
            mydb.commit()
            print(cs.okColor + "Pomślnie dodano nowy rekord")
            print(cs.okColor + sql)
            mydb.close()
        except mysql.connector.Error as err:
            print(cs.errorColor + f"Nie udało się dodać rekordu: {err}")
            pass
        except ValueError as ve:
            print(cs.errorColor + f"Nie udało się wpisać rekordu: {ve}")
            pass

    @staticmethod
    def deleteRecord(tab1):
        print(cs.userColor + "Wpisz rekordy do usunięcia wg. wartości pola w kolumnie: np. id=5 : ")
        in1 = input()
        list1 = in1.split("=")

        if (len(list1) == 2):
            sql = f"DELETE FROM {tab1} WHERE {list1[0]}='{list1[1]}';"
            try:
                mydb = mysql.connector.connect(**db.dbconnect)
                mycursor = mydb.cursor()
                mycursor.execute(sql)
                print(cs.okColor + sql)
                mydb.commit()
                print(cs.okColor + "Pomślnie usunięto rekord")
                mydb.close()
            except:
                print(cs.errorColor + sql)
                print(cs.errorColor + "Błędnie podana nazwa kolumny lub szukanego pola")
        else:
            print(cs.errorColor + "Nie poprawny zapis, za dużo / za mało podanych elementów")