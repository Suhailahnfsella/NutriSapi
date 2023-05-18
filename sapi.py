from func1 import fitursatu1
from func1 import fitursatu2
from func2 import fiturdua
from func2 import fiturtiga
import csv
from csv import writer
import pandas as pd
import os

os.system("cls")

data_sapi = []
with open('datasapi.csv') as csv_sapi :
    csv_reader = csv.reader(csv_sapi, delimiter=",")
    for row in csv_reader:
      data_sapi.append({"id":row[0],"jenis":row[1],"bb":row[2]})

angka = [1,2,3,4,5]
fitur = 0
while fitur not in angka :
    print(" ======================================= ")
    print("| Pemrograman Menghitung Kebutuhan Sapi |")
    print('|             "NUTRISAPI"               |')
    print(" ======================================= ")
    print("|                FITUR                  |")
    print(" --------------------------------------- ")
    print("|         1. Cek Jenis Pakan            |")
    print("|         2. Masukkan Data Sapi         |")
    print("|         3. Lihat Data Sapi            |")
    print("|         4. Cek Kebutuhan Tiap Sapi    |")
    print("|         5. Cek Kebutuhan Seluruh Sapi |")
    print(" --------------------------------------- ")
    fitur += int(input("FITUR (1/2/3/4/5) : "))
    if fitur == 1:
        print(" --------------------------------------- ")
        print("|        PILIH JENIS PAKAN SAPI         |")
        print(" --------------------------------------- ")
        print("|        PAKAN SAPI PEDAGING   (1)      |")
        print("|        PAKAN SAPI PERAH      (2)      |")
        print("|        END_MENU              (3)      |")
        print(" --------------------------------------- ")

        angka2 = [1,2,3]

        pilih = 0
        while pilih not in angka2 :
            pilih = int(input("Pilih Jenis Pakan (1/2/3) : "))
            if pilih == 1:
                fitursatu1()
            elif pilih == 2:
                fitursatu2()
            elif pilih == 3:
                break
            else :
                print("Tidak ada menu yang tersedia")
                pilih = 0
        
    elif fitur == 2:
        print("Pilih jenis Sapi")
        print("Pedaging (1)")
        print("Perah    (2)")
        jenis = int(input("Jenis (1/2) : "))
        bb = int(input("Berat Badan Sapi : "))
        id = int(data_sapi[-1]['id'])
        idfiks = id + 1

        if jenis == 1 :
          Dict = {"id":idfiks,"jenis":"Pedaging","bb":bb}
          data_sapi.append(Dict)
          datajenis = data_sapi[-1]['jenis']
          databb = data_sapi[-1]['bb']
          datafiks = [idfiks,datajenis,databb]
          with open('datasapi.csv', 'a', newline='') as datanya:
              writer_object = writer(datanya)
              writer_object.writerow(datafiks)
              datanya.close()
              print("Data Sapi Berhasil ditambahkan")

        elif jenis == 2 :
          Dict = {"id":idfiks,"jenis":"Perah","bb":bb}
          data_sapi.append(Dict)
          datajenis = data_sapi[-1]['jenis']
          databb = data_sapi[-1]['bb']
          datafiks = [idfiks,datajenis,databb]
          with open('datasapi.csv', 'a',newline='') as datanya:
              writer_object = writer(datanya)
              writer_object.writerow(datafiks)
              datanya.close()
              print("Data Sapi Berhasil ditambahkan")

        else :
          "Tidak ada jenis sapi yang dipilih"
          fitur = 0
                
    elif fitur == 3:
        df = pd.DataFrame(data_sapi)
        print(df)
        
    elif fitur == 4:
        print(" --------------------------------------- ")
        print("|      PILIH MENU CEK KEBUTUHAN SAPI    |")
        print(" --------------------------------------- ")
        print("|             PERHARI   (1)             |")
        print("|             PERMINGGU (2)             |")
        print("|             PERBULAN  (3)             |")
        print("|             END_MENU  (4)             |")
        print(" --------------------------------------- ")
        fiturdua()

    elif fitur == 5:
        print(" --------------------------------------- ")
        print("|      PILIH MENU CEK KEBUTUHAN SAPI    |")
        print(" --------------------------------------- ")
        print("|             PERHARI   (1)             |")
        print("|             PERMINGGU (2)             |")
        print("|             PERBULAN  (3)             |")
        print("|             END_MENU  (4)             |")
        print(" --------------------------------------- ")
        fiturtiga()
        
    else :
        print("Angka yang dimasukkan salah")
        fitur = 0