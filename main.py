from packages import *

if __name__ == '__main__':
    while True:
        # menu
        print("\nBINAVERTER ----- v1.0\n")
        print("Nhập số tương ứng với lựa chọn: ")
        print("1. Chuyển đổi số nguyên sang mã nhị phân")
        print("2. Chuyển đổi mã nhị phân sang số nguyên (đang phát triển)")
        print("3. Thoát\n")
        
        select = input("Vui lòng nhập lựa chọn để sử dụng: ")
        print()
        match select:
            case '1':
                itb_menu()
            case '2':
                # under development!
                pass
            case '3':
                exit = input("Nhập bất kì phím nào để thoát\n")
                break