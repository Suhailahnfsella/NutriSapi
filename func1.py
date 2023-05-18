from menu import menu1
from menu import menu2
from menu import menu3

def fitursatu1() :
    print(" --------------------------------------- ")
    print("|       JENIS PAKAN SAPI PEDAGING       |")
    print(" --------------------------------------- ")
    print("|       HIJAUAN                 (1)     |")
    print("|       KONSENTRAT              (2)     |")
    print("|       VITAMIN & MINERAL       (3)     |")
    print("|       END_MENU                (4)     |")
    print(" --------------------------------------- ")
    angka2 = [1,2,3,4]

    menu = 0
    while menu not in angka2 :
        menu += int(input("Pilih Jenis : "))
        if menu == 1:
            menu1(0)
        elif menu == 2:
            menu2(0)
        elif menu == 3:
            menu3()
        elif menu == 4:
            break
        else :
            print("Tidak ada menu yang tersedia")
            menu = 0

def fitursatu2() :
    print(" --------------------------------------- ")
    print("|       JENIS PAKAN SAPI PERAH          |")
    print(" --------------------------------------- ")
    print("|       HIJAUAN                 (1)     |")
    print("|       KONSENTRAT              (2)     |")
    print("|       VITAMIN & MINERAL       (3)     |")
    print("|       END_MENU                (4)     |")
    print(" --------------------------------------- ")
    angka2 = [1,2,3,4]

    menu = 0
    while menu not in angka2 :
        menu += int(input("Pilih Jenis : "))
        if menu == 1:
            menu1(1)
        elif menu == 2:
            menu2(1)
        elif menu == 3:
            menu3()
        elif menu == 4:
            break
        else :
            print("Tidak ada menu yang tersedia")
            menu = 0