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
            # get user choice
            select = input("Vui lòng nhập lựa chọn để sử dụng: ")
            clear_terminal()
            match select:
                # interger to binary
                case '1':
                    itb_menu()
                    
                # binary to interger
                case '2':
                    # under development!
                    pass
                
                # exit
                case '3':
                    exit = input(Fore.YELLOW + Style.BRIGHT + "Nhập bất kì phím nào để thoát\n" + Style.RESET_ALL)
                    clear_terminal()
                    break
                
                # invalid choice
                case _:
                    print_error("LỰA CHỌN ĐÃ NHẬP KHÔNG HỢP LỆ!")
                    
        # KeyboardInterrupt exception
        except KeyboardInterrupt:
            clear_terminal()
            exit = input("Đã phát hiện Ctrl-C. Nhập bất kì phim nào để thoát. Nhập phím 'T' để tiếp tục chương trình\n").lower()
            clear_terminal()
            if exit != 't':
                break