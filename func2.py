from waktu import perhari
from waktu import perminggu
from waktu import perbulan
from waktu2 import perhari2
from waktu2 import perminggu2
from waktu2 import perbulan2

def fiturdua() :
    angka2 = [1,2,3,4]

    menu = 0
    while menu not in angka2 :
        menu += int(input("Jangka Waktu : "))
        if menu == 1:
            perhari()
        elif menu == 2:
            perminggu()
        elif menu == 3:
            perbulan()
        elif menu == 4:
            break
        else :
            print("Tidak ada menu yang tersedia")
            menu = 0

def fiturtiga() :
    angka2 = [1,2,3,4]

    menu = 0
    while menu not in angka2 :
        menu += int(input("Jangka Waktu : "))
        if menu == 1:
            perhari2()
        elif menu == 2:
            perminggu2()
        elif menu == 3:
            perbulan2()
        elif menu == 4:
            break
        else :
            print("Tidak ada menu yang tersedia")
            menu = 0