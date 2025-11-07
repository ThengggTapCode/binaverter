from colorama import Fore, Style

def print_error(msg):
    print(Fore.RED + "\n------------------------------------------\n")
    print(f"\t{msg}\n")
    print("------------------------------------------\n" + Fore.RESET)
    