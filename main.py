from colorama import init as initColor, Fore, Back
import db_connect as db
import login as lg, table as tb, column as cl, commonSettings as cs

initColor(autoreset=True)

def menuLogin():
    while True:
        print(cs.userColor + "----------------------------------------")
        cnt = 0
        # wyświetl meny 1...6
        print("Wpisz dane logowania do połączenia z bazą danych")
        for key, value in db.dbconnect.items():
            cnt = cnt + 1
            print(str(cnt), ".", key, ":", value)
        print("5 . Połącz z bazą danych")
        print("6 . Wyjście")
        in1 = input("1...6: ")
        if(in1.isdigit() and int(in1)>=1 and int(in1)<=6):
            match in1:
                case "1": lg.Login.changeHost()
                case "2": lg.Login.changeUser()
                case "3": lg.Login.changePasswd()
                case "4": lg.Login.changeDb()
                case "5": 
                    if lg.Login.openDb() == True: menuDb()
                case "6": break

def menuDb():
    while True:    
        print("1 . Pokaż dostępne tabele")
        print("2 . Otwórz tabelę")
        print("3 . Dodaj tabelę")
        print("4 . Usuń tabelę")
        print("6 . Powrót do wyboru bazy danych")
        in1 = input("1...6: ")
        if(in1.isdigit() and int(in1)>=1 and int(in1)<=6):
            match in1:
                case "1": tb.Tabele.showTables()
                case "2": 
                    tab1 = tb.Tabele.openTable()
                    if tab1 != "": menuColumns(tab1)
                case "3": tb.Tabele.addTable()
                case "4": tb.Tabele.deleteTabele()
                case "5": tb.Tabele.changeDb()
                case "6": break

def menuColumns(tab1):
    while True:
        print("1 . Pokaż dostępne kolumny")
        print("2 . Wyświetl zawartość całej tabeli")
        print("3 . Wyświetl zawartość określonych kolumn")
        print("4 . Wyświetl rekord o id")
        print("5 . Dodaj rekord")
        print("6 . Usuń rekord o nazwie pola w kolumnie")
        print("7 . Powrót")
        in1 = input("1...6: ")
        if(in1.isdigit() and int(in1)>=1 and int(in1)<=7):
            match in1:
                case "1": cl.Column.showColumns(tab1)
                case "2": cl.Column.showTable(tab1)
                case "3": cl.Column.showSpecifyColumn(tab1)
                case "4": cl.Column.showSpecifyRecord(tab1)
                case "5": cl.Column.addRecord(tab1)
                case "6": cl.Column.deleteRecord(tab1)
                case "7": break

menuLogin()