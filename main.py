from packages import *

if __name__ == '__main__':
    while True:
        # menu
        print(Fore.BLUE + Style.BRIGHT + "BINAVERTER ----- v1.0\n" + Style.RESET_ALL)
        print("Nhập số tương ứng với lựa chọn:\n")
        print(Fore.GREEN + "1. Chuyển đổi số nguyên sang mã nhị phân")
        print("2. Chuyển đổi mã nhị phân sang số nguyên (đang phát triển)")
        print("3. Thoát\n" + Fore.RESET)
        
        try:
            select = input("Vui lòng nhập lựa chọn để sử dụng: ")
            clear_terminal()
            match select:
                case '1':
                    itb_menu()
                case '2':
                    # under development!
                    pass
                case '3':
                    exit = input(Fore.YELLOW + Style.BRIGHT + "Nhập bất kì phím nào để thoát\n" + Style.RESET_ALL)
                    clear_terminal()
                    break
                case _:
                    print_error("Lựa chọn đã nhập không hợp lệ!")
        except KeyboardInterrupt:
            clear_terminal()
            exit = input("Đã phát hiện Ctrl-C. Nhập bất kì phim nào để thoát. Nhập phím 'T' để tiếp tục chương trình\n").lower()
            clear_terminal()
            if exit != 't':
                break