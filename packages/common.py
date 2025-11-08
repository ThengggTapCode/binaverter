from os import name, system
from colorama import Fore, Style

def print_error(msg):
    print(Fore.RED + "\n------------------------------------------\n")
    print(f"\t{msg}\n")
    print("------------------------------------------\n" + Fore.RESET)

def clear_terminal():
    if name == 'nt':
        system("cls")
    else:
        system("clear")