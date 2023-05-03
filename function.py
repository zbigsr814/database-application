from prettytable import PrettyTable
from colorama import init as initColor, Fore, Back

def printTable(idx, lists, color=Fore.RESET):   # wyświetla tabelkę w kolorze
    initColor(autoreset=True)
    tab2 = PrettyTable()
    tab2.field_names = idx
    for i in range(len(lists)):
        tab2.add_row(lists[i])
    print(f"{color}{tab2}")