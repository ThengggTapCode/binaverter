from packages import *

if __name__ == '__main__':
    while True:
        # menu
        print(Fore.BLUE + Style.BRIGHT + "BINAVERTER ----- v2.0\n" + Style.RESET_ALL)
        print("Nhập kí tự tương ứng với lựa chọn:\n")
        print(Fore.GREEN + "1. Chuyển đổi số nguyên sang mã nhị phân")
        print("2. Chuyển đổi mã nhị phân sang số nguyên")
        print("3. Chuyển đổi văn bản sang mã nhị phân")
        print("4. Chuyển đổi mã nhị phân sang văn bản")
        print("T/t. Thoát\n" + Fore.RESET)
        
        try:
            # get user choice
            select = input("Vui lòng nhập lựa chọn để sử dụng: ").lower()
            clear_terminal()
            match select:
                # interger to binary
                case '1':
                    itb_menu()
                    
                # binary to interger
                case '2':
                    bti_menu()
                
                # text to binary
                case '3':
                    ttb_menu()

                # binary to text
                case '4':
                    pass
                
                # exit
                case 't':
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