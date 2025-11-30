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
def print_binary(n, binary, mode, text):
    
    binary = ''.join(binary)
    if mode == 'itb':
        print(Fore.GREEN + f'{n} = {binary}\n' + Fore.RESET)
    elif mode == 'bti':
        print(Fore.GREEN + f'{binary} = {n}\n' + Fore.RESET)
    elif mode == 'ttb':
        print(Fore.GREEN + f'{text} = ')
        print(f'{binary}\n' + Fore.RESET)