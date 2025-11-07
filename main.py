from packages import *

if __name__ == '__main__':
    while True:
        # menu
        print(Fore.BLUE + Style.BRIGHT + "\nBINAVERTER ----- v1.0\n" + Style.RESET_ALL)
        print("Nhập số tương ứng với lựa chọn:\n")
        print(Fore.GREEN + "1. Chuyển đổi số nguyên sang mã nhị phân")
        print("2. Chuyển đổi mã nhị phân sang số nguyên (đang phát triển)")
        print("3. Thoát\n" + Fore.RESET)
        
        select = input("Vui lòng nhập lựa chọn để sử dụng: ")
        print()
        match select:
            case '1':
                itb_menu()
            case '2':
                # under development!
                pass
            case '3':
                exit = input(Fore.YELLOW + Style.BRIGHT + "Nhập bất kì phím nào để thoát\n" + Style.RESET_ALL)
                break
            case _:
                print_error("Lựa chọn đã nhập không hợp lệ!")