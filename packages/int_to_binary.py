from .common import *
from .algorithms import *

def itb_menu():
    while True:
        try:
            # get interger n
            n = input("Nhập số nguyên (nhập T để thoát lựa chọn): ")
            clear_terminal()
            n = int(n)
        
        # ValueError exception
        except ValueError:
            if n.lower() == 't':
                print(Fore.YELLOW + Style.BRIGHT + "Đã thoát lựa chọn!\n", Style.RESET_ALL)
                return
            print_error("VUI LÒNG CHỈ NHẬP SỐ NGUYÊN")
            continue
        
        # convert |n| interger to binary
        binary = interger_to_binary(abs(n))
        
        # format binary for better visual
        binary = format_binary(n, binary)
        clear_terminal()
        
        # print the final binary result
        print_binary(n, binary, 'itb')