import pandas as pd
import csv

def perhari2() :
    data_sapi = []
    with open('datasapi.csv') as csv_sapi :
        csv_reader = csv.reader(csv_sapi, delimiter=",")
        for row in csv_reader:
            data_sapi.append({"id":row[0],"jenis":row[1],"bb":row[2]})

    df = pd.DataFrame(data_sapi)
    print(df)

    berat_pedaging = 0
    jumlah_pedaging = 0

    berat_perah = 0
    jumlah_perah = 0

    for i in data_sapi :
        if i['jenis'] == "Pedaging" :
            berat_pedaging += int(i['bb'])
            jumlah_pedaging += 1
        elif i['jenis'] == "Perah" :
            berat_perah += int(i['bb'])
            jumlah_perah += 1
    
    kali = ''
    if jumlah_pedaging < 10 :
        kali = ' '*18
    elif jumlah_pedaging >= 10 and jumlah_pedaging < 100 :
        kali = ' '*17
    elif jumlah_pedaging >= 100 :
        kali = ' '*16
    
    kali2 = ''
    if jumlah_perah < 10 :
        kali2 = ' '*18
    elif jumlah_perah >= 10 and jumlah_perah < 100 :
        kali2 = ' '*17
    elif jumlah_perah >= 100 :
        kali2 = ' '*16

    kali3 = ''
    if berat_pedaging < 100 :
        kali3 = ' '*14
    elif 1000 > berat_pedaging >= 100 :
        kali3 = ' '*13
    elif berat_pedaging >= 1000 :
        kali3 = ' '*12

    kali4 = ''
    if berat_perah < 100 :
        kali4 = ' '*14
    elif 1000 > berat_perah >= 100 :
        kali4 = ' '*13
    elif berat_perah >= 1000 :
        kali4 = ' '*12

    kebutuhan_pedaging = 10*berat_pedaging/100
    hijauan_pedaging = 60*kebutuhan_pedaging/100
    konsentrat_pedaging = 40*kebutuhan_pedaging/100

    kebutuhan_perah = 10*berat_perah/100
    hijauan_perah = 60*kebutuhan_perah/100
    konsentrat_perah = 40*kebutuhan_perah/100
    
    print(" --------------------------------------- ")
    print(f"| Jumlah Sapi      : {jumlah_pedaging}{kali}|")
    print(f"| Jenis Sapi       : Pedaging {' '*10}|")
    print(f"| Total Berat Sapi : {berat_pedaging} kg{kali3}|")
    print(" --------------------------------------- ")
    print(f" Kebutuhan Pakan /Hari = {kebutuhan_pedaging} kg")
    print(f"")
    print(f" Hijauan               = {hijauan_pedaging} kg")
    print(f"")
    print(f" Konsentrat            = {konsentrat_pedaging} kg")
    print(f" -> Bungkil Kelapa     = {10*konsentrat_pedaging/100} kg")
    print(f" -> Bungkil Jagung     = {30*konsentrat_pedaging/100} kg")
    print(f" -> Dedak              = {54.8*konsentrat_pedaging/100} kg")
    print(f" -> Mineral Mix        = {0.2*konsentrat_pedaging/100} kg")
    print(f" -> Tepung Ikan        = {0.2*konsentrat_pedaging/100} kg")
    print(f" ")
    print(f" Vitamin & Mineral     = {2*kebutuhan_pedaging/100} kg")
    print(" --------------------------------------- ")

    print("")
    
    print(" --------------------------------------- ")
    print(f"| Jumlah Sapi      : {jumlah_perah}{kali2}|")
    print(f"| Jenis Sapi       : Perah {' '*13}|")
    print(f"| Total Berat Sapi : {berat_perah} kg{kali4}|")
    print(" --------------------------------------- ")
    print(f" Kebutuhan Pakan /Hari = {kebutuhan_perah} kg")
    print(f"")
    print(f" Hijauan               = {hijauan_perah} kg")
    print(f"")
    print(f" Konsentrat            = {konsentrat_perah} kg")
    print(f" -> Bungkil Kelapa =  {25*konsentrat_perah/100} kg")
    print(f" -> Bungkil Kacang =  {20*konsentrat_perah/100} kg")
    print(f" -> Tepung Jagung  =  {25*konsentrat_perah/100} kg")
    print(f" -> Dedak Padi     =  {25*konsentrat_perah/100} kg")
    print(f" -> Ampas Tahu     =  {1*konsentrat_perah/100} kg")
    print(f" -> Garam Dapur    =  {1*konsentrat_perah/100} kg")
    print(f" -> Kapur          =  {1*konsentrat_perah/100} kg")
    print(f" -> Tepung Tulang  =  {1*konsentrat_perah/100} kg")
    print(f" ")
    print(f" Vitamin & Mineral     = {2*kebutuhan_perah/100} kg")
    print(" --------------------------------------- ")

def perminggu2() :
    data_sapi = []
    with open('datasapi.csv') as csv_sapi :
        csv_reader = csv.reader(csv_sapi, delimiter=",")
        for row in csv_reader:
            data_sapi.append({"id":row[0],"jenis":row[1],"bb":row[2]})

    df = pd.DataFrame(data_sapi)
    print(df)

    berat_pedaging = 0
    jumlah_pedaging = 0

    berat_perah = 0
    jumlah_perah = 0

    for i in data_sapi :
        if i['jenis'] == "Pedaging" :
            berat_pedaging += int(i['bb'])
            jumlah_pedaging += 1
        elif i['jenis'] == "Perah" :
            berat_perah += int(i['bb'])
            jumlah_perah += 1
    
    kali = ''
    if jumlah_pedaging < 10 :
        kali = ' '*18
    elif jumlah_pedaging >= 10 and jumlah_pedaging < 100 :
        kali = ' '*17
    elif jumlah_pedaging >= 100 :
        kali = ' '*16
    
    kali2 = ''
    if jumlah_perah < 10 :
        kali2 = ' '*18
    elif jumlah_perah >= 10 and jumlah_perah < 100 :
        kali2 = ' '*17
    elif jumlah_perah >= 100 :
        kali2 = ' '*16

    kali3 = ''
    if berat_pedaging < 100 :
        kali3 = ' '*14
    elif 1000 > berat_pedaging >= 100 :
        kali3 = ' '*13
    elif berat_pedaging >= 1000 :
        kali3 = ' '*12

    kali4 = ''
    if berat_perah < 100 :
        kali4 = ' '*14
    elif 1000 > berat_perah >= 100 :
        kali4 = ' '*13
    elif berat_perah >= 1000 :
        kali4 = ' '*12

    kebutuhan_pedaging = (10*berat_pedaging/100)*7
    hijauan_pedaging = 60*kebutuhan_pedaging/100
    konsentrat_pedaging = 40*kebutuhan_pedaging/100

    kebutuhan_perah = (10*berat_perah/100)*7
    hijauan_perah = 60*kebutuhan_perah/100
    konsentrat_perah = 40*kebutuhan_perah/100
    
    print(" --------------------------------------- ")
    print(f"| Jumlah Sapi      : {jumlah_pedaging}{kali}|")
    print(f"| Jenis Sapi       : Pedaging {' '*10}|")
    print(f"| Total Berat Sapi : {berat_pedaging} kg{kali3}|")
    print(" --------------------------------------- ")
    print(f" Kebutuhan Pakan /Minggu = {kebutuhan_pedaging} kg")
    print(f"")
    print(f" Hijauan                 = {hijauan_pedaging} kg")
    print(f"")
    print(f" Konsentrat              = {konsentrat_pedaging} kg")
    print(f" -> Bungkil Kelapa       = {10*konsentrat_pedaging/100} kg")
    print(f" -> Bungkil Jagung       = {30*konsentrat_pedaging/100} kg")
    print(f" -> Dedak                = {54.8*konsentrat_pedaging/100} kg")
    print(f" -> Mineral Mix          = {0.2*konsentrat_pedaging/100} kg")
    print(f" -> Tepung Ikan          = {0.2*konsentrat_pedaging/100} kg")
    print(f" ")
    print(f" Vitamin & Mineral       = {2*kebutuhan_pedaging/100} kg")
    print(" --------------------------------------- ")

    print("")
    
    print(" --------------------------------------- ")
    print(f"| Jumlah Sapi      : {jumlah_perah}{kali2}|")
    print(f"| Jenis Sapi       : Perah {' '*13}|")
    print(f"| Total Berat Sapi : {berat_perah} kg{kali4}|")
    print(" --------------------------------------- ")
    print(f" Kebutuhan Pakan /Minggu = {kebutuhan_perah} kg")
    print(f"")
    print(f" Hijauan                 = {hijauan_perah} kg")
    print(f"")
    print(f" Konsentrat              = {konsentrat_perah} kg")
    print(f" -> Bungkil Kelapa =  {25*konsentrat_perah/100} kg")
    print(f" -> Bungkil Kacang =  {20*konsentrat_perah/100} kg")
    print(f" -> Tepung Jagung  =  {25*konsentrat_perah/100} kg")
    print(f" -> Dedak Padi     =  {25*konsentrat_perah/100} kg")
    print(f" -> Ampas Tahu     =  {1*konsentrat_perah/100} kg")
    print(f" -> Garam Dapur    =  {1*konsentrat_perah/100} kg")
    print(f" -> Kapur          =  {1*konsentrat_perah/100} kg")
    print(f" -> Tepung Tulang  =  {1*konsentrat_perah/100} kg")
    print(f" ")
    print(f" Vitamin & Mineral       = {2*kebutuhan_perah/100} kg")
    print(" --------------------------------------- ")

def perbulan2() :
    data_sapi = []
    with open('datasapi.csv') as csv_sapi :
        csv_reader = csv.reader(csv_sapi, delimiter=",")
        for row in csv_reader:
            data_sapi.append({"id":row[0],"jenis":row[1],"bb":row[2]})

    df = pd.DataFrame(data_sapi)
    print(df)

    berat_pedaging = 0
    jumlah_pedaging = 0

    berat_perah = 0
    jumlah_perah = 0

    for i in data_sapi :
        if i['jenis'] == "Pedaging" :
            berat_pedaging += int(i['bb'])
            jumlah_pedaging += 1
        elif i['jenis'] == "Perah" :
            berat_perah += int(i['bb'])
            jumlah_perah += 1
    
    kali = ''
    if jumlah_pedaging < 10 :
        kali = ' '*18
    elif jumlah_pedaging >= 10 and jumlah_pedaging < 100 :
        kali = ' '*17
    elif jumlah_pedaging >= 100 :
        kali = ' '*16
    
    kali2 = ''
    if jumlah_perah < 10 :
        kali2 = ' '*18
    elif jumlah_perah >= 10 and jumlah_perah < 100 :
        kali2 = ' '*17
    elif jumlah_perah >= 100 :
        kali2 = ' '*16

    kali3 = ''
    if berat_pedaging < 100 :
        kali3 = ' '*14
    elif 1000 > berat_pedaging >= 100 :
        kali3 = ' '*13
    elif berat_pedaging >= 1000 :
        kali3 = ' '*12

    kali4 = ''
    if berat_perah < 100 :
        kali4 = ' '*14
    elif 1000 > berat_perah >= 100 :
        kali4 = ' '*13
    elif berat_perah >= 1000 :
        kali4 = ' '*12

    kebutuhan_pedaging = (10*berat_pedaging/100)*30
    hijauan_pedaging = 60*kebutuhan_pedaging/100
    konsentrat_pedaging = 40*kebutuhan_pedaging/100

    kebutuhan_perah = (10*berat_perah/100)*30
    hijauan_perah = 60*kebutuhan_perah/100
    konsentrat_perah = 40*kebutuhan_perah/100
    
    print(" --------------------------------------- ")
    print(f"| Jumlah Sapi      : {jumlah_pedaging}{kali}|")
    print(f"| Jenis Sapi       : Pedaging {' '*10}|")
    print(f"| Total Berat Sapi : {berat_pedaging} kg{kali3}|")
    print(" --------------------------------------- ")
    print(f" Kebutuhan Pakan /Bulan = {kebutuhan_pedaging} kg")
    print(f"")
    print(f" Hijauan                = {hijauan_pedaging} kg")
    print(f"")
    print(f" Konsentrat             = {konsentrat_pedaging} kg")
    print(f" -> Bungkil Kelapa      = {10*konsentrat_pedaging/100} kg")
    print(f" -> Bungkil Jagung      = {30*konsentrat_pedaging/100} kg")
    print(f" -> Dedak               = {54.8*konsentrat_pedaging/100} kg")
    print(f" -> Mineral Mix         = {0.2*konsentrat_pedaging/100} kg")
    print(f" -> Tepung Ikan         = {0.2*konsentrat_pedaging/100} kg")
    print(f" ")
    print(f" Vitamin & Mineral      = {2*kebutuhan_pedaging/100} kg")
    print(" --------------------------------------- ")

    print("")
    
    print(" --------------------------------------- ")
    print(f"| Jumlah Sapi      : {jumlah_perah}{kali2}|")
    print(f"| Jenis Sapi       : Perah {' '*13}|")
    print(f"| Total Berat Sapi : {berat_perah} kg{kali4}|")
    print(" --------------------------------------- ")
    print(f" Kebutuhan Pakan /Bulan = {kebutuhan_perah} kg")
    print(f"")
    print(f" Hijauan                = {hijauan_perah} kg")
    print(f"")
    print(f" Konsentrat             = {konsentrat_perah} kg")
    print(f" -> Bungkil Kelapa =  {25*konsentrat_perah/100} kg")
    print(f" -> Bungkil Kacang =  {20*konsentrat_perah/100} kg")
    print(f" -> Tepung Jagung  =  {25*konsentrat_perah/100} kg")
    print(f" -> Dedak Padi     =  {25*konsentrat_perah/100} kg")
    print(f" -> Ampas Tahu     =  {1*konsentrat_perah/100} kg")
    print(f" -> Garam Dapur    =  {1*konsentrat_perah/100} kg")
    print(f" -> Kapur          =  {1*konsentrat_perah/100} kg")
    print(f" -> Tepung Tulang  =  {1*konsentrat_perah/100} kg")
    print(f" ")
    print(f" Vitamin & Mineral      = {2*kebutuhan_perah/100} kg")
    print(" --------------------------------------- ")