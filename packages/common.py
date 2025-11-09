from os import name, system
from colorama import Fore, Style

def print_error(msg):
    print(Fore.RED + "\n------------------------------------------\n")
    print(f"\t{msg}\n")
    print("------------------------------------------\n" + Fore.RESET)

def clear_terminal():
    # windows system
    if name == 'nt':
        system("cls")
    # unix/other system
    else:
        system("clear")