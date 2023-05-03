from colorama import init as initColor, Fore, Back
import db_connect as db
import login as lg, table as tb, commonSettings as cs
import io, re

closeLoop = True

def validFnc(in1):      # Funkcja wykorzystująca regular expression, wstępna walidacja
    global closeLoop
    if in1 == "exit":
        closeLoop = False
        return ""
    elif re.match("^.*,$", in1): 
        print(cs.errorColor + "Podane wyrażenie nie może kończyć się przecinkiem")
        return ""
    elif not re.match("^[a-zA-Z0-9,]+$", in1): 
        print(cs.errorColor + "Podane wyrażenie musi zawierać tylko symbole: a-z, A-Z, 1-9 / lub wpisz 'exit' aby wyjść")
        return ""
    else: 
        return in1

def tableMaker(in1, cnt):    # funkcja tworząca zapytanie SQL tworzenia tabeli
    in1 = str(in1)
    list1 = in1.split(",")

    tmp = io.StringIO()   # String builder

    if cnt >= 2:
        tmp.write(", ")

    if(len(list1) >= 2 and len(list1) <= 3):
        tmp.write(list1[0]+ " ")
        if(list1[1]=="str"):
            tmp.write("VARCHAR(50) ")
        elif(list1[1]=="int"):
            tmp.write("INT ")
        else:
            print(cs.errorColor + "BŁĄD - nie podano typu zmiennych")
            return ""
        
        if(len(list1) == 3):
            if(list1[2]=="key"):
                tmp.write("PRIMARY KEY")
            elif(list1[2]=="autoinckey"):
                tmp.write("AUTO_INCREMENT PRIMARY KEY")
            else:
                print(cs.errorColor + "BŁĄD - Niepoprawny zapis klucza")
        
        strr = tmp.getvalue()
        print(cs.okColor + "Dodano kolumne")
        return strr
    else:
        print(cs.errorColor + "BŁĄD - Niepoprawny zapis")
        return ""

s = io.StringIO()   # String builder


def getSQLcreate():
    while closeLoop:        # Tworzene nazwy tabeli zgodnej z formatem
        in1 = input(cs.userColor + "Podaj nazwą tabeli do utworzenia: ")
        if validFnc(in1) == in1:
            s.write(f"CREATE TABLE {in1} (")
            print(cs.okColor + "Nadano nazwę tabeli")
            break

    cnt = 0
    while closeLoop:    # Tworzenie kolumn i ich typów
        cnt += 1 
        print(cs.userColor + "Wpisz 'exit' w celu wyjścia")
        in2 = input(cs.userColor + f"Podaj kolumny w formacie: nazwa,typ(int/str),opcje(opcjonalne/key/autoinckey) : np. id,int,key lub col2,str: ")

        if validFnc(in2) == "":
            continue
        tmp = tableMaker(in2, cnt)
        if tmp == "":
            continue
        else:
            s.write(tmp)

        
    s.write(");")
    print(cs.okColor + s.getvalue())
    return s.getvalue()

