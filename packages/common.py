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

# print final binary result
def print_binary(n, binary, mode):
    if mode == 'itb':
        print(Fore.GREEN + f'{n} = ', end='')
        for i in binary:
            print(i,end='')
        print(Fore.RESET + "\n")
    elif mode == 'bti':
        for i in binary:
            print(Fore.GREEN + i ,end='')
        print(f" = {n}\n" + Fore.RESET)