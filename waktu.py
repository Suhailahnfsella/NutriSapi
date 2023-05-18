import pandas as pd
import csv

def perhari() :
    data_sapi = []
    with open('datasapi.csv') as csv_sapi :
        csv_reader = csv.reader(csv_sapi, delimiter=",")
        for row in csv_reader:
            data_sapi.append({"id":row[0],"jenis":row[1],"bb":row[2]})

    df = pd.DataFrame(data_sapi)
    print(df)
    
    id = int(input("ID Sapi : "))

    berat = 0
    jenis = ""
    for i in data_sapi :
        if int(i['id']) == id :
            berat += int(i['bb'])
            jenis = i['jenis']
    
    if id < 10 :
        if jenis == "Pedaging" :
            if berat < 100 :
                print(" --------------------------------------- ")
                print(f"| ID Sapi      : {id}{' '*22}|")
                print(f"| Jenis Sapi   : {jenis}{' '*15}|")
                print(f"| Berat Sapi   : {berat} kg{' '*18}|")
                print(" --------------------------------------- ")
            elif berat >= 100 :
                print(" --------------------------------------- ")
                print(f"| ID Sapi      : {id}{' '*22}|")
                print(f"| Jenis Sapi   : {jenis}{' '*15}|")
                print(f"| Berat Sapi   : {berat} kg{' '*17}|")
                print(" --------------------------------------- ")
        elif jenis == "Perah" :
            if berat < 100 :
                print(" --------------------------------------- ")
                print(f"| ID Sapi      : {id}{' '*22}|")
                print(f"| Jenis Sapi   : {jenis}{' '*18}|")
                print(f"| Berat Sapi   : {berat} kg{' '*18}|")
                print(" --------------------------------------- ")
            elif berat >= 100 :
                print(" --------------------------------------- ")
                print(f"| ID Sapi      : {id}{' '*22}|")
                print(f"| Jenis Sapi   : {jenis}{' '*18}|")
                print(f"| Berat Sapi   : {berat} kg{' '*17}|")
                print(" --------------------------------------- ")
    elif id >= 10 :
        if jenis == "Pedaging" :
            if berat < 100 :
                print(" --------------------------------------- ")
                print(f"| ID Sapi      : {id}{' '*21}|")
                print(f"| Jenis Sapi   : {jenis}{' '*15}|")
                print(f"| Berat Sapi   : {berat} kg{' '*18}|")
                print(" --------------------------------------- ")
            elif berat >= 100 :
                print(" --------------------------------------- ")
                print(f"| ID Sapi      : {id}{' '*21}|")
                print(f"| Jenis Sapi   : {jenis}{' '*15}|")
                print(f"| Berat Sapi   : {berat} kg{' '*17}|")
                print(" --------------------------------------- ")
        elif jenis == "Perah" :
            if berat < 100 :
                print(" --------------------------------------- ")
                print(f"| ID Sapi      : {id}{' '*21}|")
                print(f"| Jenis Sapi   : {jenis}{' '*18}|")
                print(f"| Berat Sapi   : {berat} kg{' '*18}|")
                print(" --------------------------------------- ")
            elif berat >= 100 :
                print(" --------------------------------------- ")
                print(f"| ID Sapi      : {id}{' '*21}|")
                print(f"| Jenis Sapi   : {jenis}{' '*18}|")
                print(f"| Berat Sapi   : {berat} kg{' '*17}|")
                print(" --------------------------------------- ")

    kebutuhan = 10*berat/100
    hijauan = 60*kebutuhan/100
    konsentrat = 40*kebutuhan/100

    if jenis == "Pedaging" :
        print(f" Kebutuhan Pakan /Hari = {kebutuhan} kg")
        print(f"")
        print(f" Hijauan         = {hijauan} kg")
        print(f"")
        print(f" Konsentrat      = {konsentrat} kg")
        print(f" -> Bungkil Kelapa  = {10*konsentrat/100} kg")
        print(f" -> Bungkil Jagung  = {30*konsentrat/100} kg")
        print(f" -> Dedak           = {54.8*konsentrat/100} kg")
        print(f" -> Mineral Mix     = {0.2*konsentrat/100} kg")
        print(f" -> Tepung Ikan     = {0.2*konsentrat/100} kg")
        print(f" ")
        print(f" Vitamin & Mineral = {2*kebutuhan/100} kg")
        print(" --------------------------------------- ")
    elif jenis == "Perah" :
        print(f" Kebutuhan Pakan /Hari = {kebutuhan} kg")
        print(f" ")
        print(f" Hijauan         = {hijauan} kg")
        print(f" ")
        print(f" Konsentrat      = {konsentrat} kg")
        print(f" -> Bungkil Kelapa =  {25*konsentrat/100} kg")
        print(f" -> Bungkil Kacang =  {20*konsentrat/100} kg")
        print(f" -> Tepung Jagung  =  {25*konsentrat/100} kg")
        print(f" -> Dedak Padi     =  {25*konsentrat/100} kg")
        print(f" -> Ampas Tahu     =  {1*konsentrat/100} kg")
        print(f" -> Garam Dapur    =  {1*konsentrat/100} kg")
        print(f" -> Kapur          =  {1*konsentrat/100} kg")
        print(f" -> Tepung Tulang  =  {1*konsentrat/100} kg")
        print(f" ")
        print(f" Vitamin & Mineral = {2*kebutuhan/100} kg")
        print(" --------------------------------------- ")
    else :
        print("Error")
    

def perminggu() :
    data_sapi = []
    with open('datasapi.csv') as csv_sapi :
        csv_reader = csv.reader(csv_sapi, delimiter=",")
        for row in csv_reader:
            data_sapi.append({"id":row[0],"jenis":row[1],"bb":row[2]})

    df = pd.DataFrame(data_sapi)
    print(df)
    
    id = int(input("ID Sapi : "))

    berat = 0
    jenis = ""
    for i in data_sapi :
        if int(i['id']) == id :
            berat += int(i['bb'])
            jenis = i['jenis']
    
    if id < 10 :
        if jenis == "Pedaging" :
            if berat < 100 :
                print(" --------------------------------------- ")
                print(f"| ID Sapi      : {id}{' '*22}|")
                print(f"| Jenis Sapi   : {jenis}{' '*15}|")
                print(f"| Berat Sapi   : {berat} kg{' '*18}|")
                print(" --------------------------------------- ")
            elif berat >= 100 :
                print(" --------------------------------------- ")
                print(f"| ID Sapi      : {id}{' '*22}|")
                print(f"| Jenis Sapi   : {jenis}{' '*15}|")
                print(f"| Berat Sapi   : {berat} kg{' '*17}|")
                print(" --------------------------------------- ")
        elif jenis == "Perah" :
            if berat < 100 :
                print(" --------------------------------------- ")
                print(f"| ID Sapi      : {id}{' '*22}|")
                print(f"| Jenis Sapi   : {jenis}{' '*18}|")
                print(f"| Berat Sapi   : {berat} kg{' '*18}|")
                print(" --------------------------------------- ")
            elif berat >= 100 :
                print(" --------------------------------------- ")
                print(f"| ID Sapi      : {id}{' '*22}|")
                print(f"| Jenis Sapi   : {jenis}{' '*18}|")
                print(f"| Berat Sapi   : {berat} kg{' '*17}|")
                print(" --------------------------------------- ")
    elif id >= 10 :
        if jenis == "Pedaging" :
            if berat < 100 :
                print(" --------------------------------------- ")
                print(f"| ID Sapi      : {id}{' '*21}|")
                print(f"| Jenis Sapi   : {jenis}{' '*15}|")
                print(f"| Berat Sapi   : {berat} kg{' '*18}|")
                print(" --------------------------------------- ")
            elif berat >= 100 :
                print(" --------------------------------------- ")
                print(f"| ID Sapi      : {id}{' '*21}|")
                print(f"| Jenis Sapi   : {jenis}{' '*15}|")
                print(f"| Berat Sapi   : {berat} kg{' '*17}|")
                print(" --------------------------------------- ")
        elif jenis == "Perah" :
            if berat < 100 :
                print(" --------------------------------------- ")
                print(f"| ID Sapi      : {id}{' '*21}|")
                print(f"| Jenis Sapi   : {jenis}{' '*18}|")
                print(f"| Berat Sapi   : {berat} kg{' '*18}|")
                print(" --------------------------------------- ")
            elif berat >= 100 :
                print(" --------------------------------------- ")
                print(f"| ID Sapi      : {id}{' '*21}|")
                print(f"| Jenis Sapi   : {jenis}{' '*18}|")
                print(f"| Berat Sapi   : {berat} kg{' '*17}|")
                print(" --------------------------------------- ")

    kebutuhan = (10*berat/100)*7
    hijauan = 60*kebutuhan/100
    konsentrat = 40*kebutuhan/100

    if jenis == "Pedaging" :
        print(f" Kebutuhan Pakan /Minggu = {kebutuhan} kg")
        print(f"")
        print(f" Hijauan         = {hijauan} kg")
        print(f"")
        print(f" Konsentrat      = {konsentrat} kg")
        print(f" -> Bungkil Kelapa  = {10*konsentrat/100} kg")
        print(f" -> Bungkil Jagung  = {30*konsentrat/100} kg")
        print(f" -> Dedak           = {54.8*konsentrat/100} kg")
        print(f" -> Mineral Mix     = {0.2*konsentrat/100} kg")
        print(f" -> Tepung Ikan     = {0.2*konsentrat/100} kg")
        print(f" ")
        print(f" Vitamin & Mineral = {2*kebutuhan/100} kg")
        print(" --------------------------------------- ")
    elif jenis == "Perah" :
        print(f" Kebutuhan Pakan /Minggu = {kebutuhan} kg")
        print(f" ")
        print(f" Hijauan         = {hijauan} kg")
        print(f" ")
        print(f" Konsentrat      = {konsentrat} kg")
        print(f" -> Bungkil Kelapa =  {25*konsentrat/100} kg")
        print(f" -> Bungkil Kacang =  {20*konsentrat/100} kg")
        print(f" -> Tepung Jagung  =  {25*konsentrat/100} kg")
        print(f" -> Dedak Padi     =  {25*konsentrat/100} kg")
        print(f" -> Ampas Tahu     =  {1*konsentrat/100} kg")
        print(f" -> Garam Dapur    =  {1*konsentrat/100} kg")
        print(f" -> Kapur          =  {1*konsentrat/100} kg")
        print(f" -> Tepung Tulang  =  {1*konsentrat/100} kg")
        print(f" ")
        print(f" Vitamin & Mineral = {2*kebutuhan/100} kg")
        print(" --------------------------------------- ")
    else :
        print("Error")

def perbulan() :
    data_sapi = []
    with open('datasapi.csv') as csv_sapi :
        csv_reader = csv.reader(csv_sapi, delimiter=",")
        for row in csv_reader:
            data_sapi.append({"id":row[0],"jenis":row[1],"bb":row[2]})

    df = pd.DataFrame(data_sapi)
    print(df)
    
    id = int(input("ID Sapi : "))

    berat = 0
    jenis = ""
    for i in data_sapi :
        if int(i['id']) == id :
            berat += int(i['bb'])
            jenis = i['jenis']
    
    if id < 10 :
        if jenis == "Pedaging" :
            if berat < 100 :
                print(" --------------------------------------- ")
                print(f"| ID Sapi      : {id}{' '*22}|")
                print(f"| Jenis Sapi   : {jenis}{' '*15}|")
                print(f"| Berat Sapi   : {berat} kg{' '*18}|")
                print(" --------------------------------------- ")
            elif berat >= 100 :
                print(" --------------------------------------- ")
                print(f"| ID Sapi      : {id}{' '*22}|")
                print(f"| Jenis Sapi   : {jenis}{' '*15}|")
                print(f"| Berat Sapi   : {berat} kg{' '*17}|")
                print(" --------------------------------------- ")
        elif jenis == "Perah" :
            if berat < 100 :
                print(" --------------------------------------- ")
                print(f"| ID Sapi      : {id}{' '*22}|")
                print(f"| Jenis Sapi   : {jenis}{' '*18}|")
                print(f"| Berat Sapi   : {berat} kg{' '*18}|")
                print(" --------------------------------------- ")
            elif berat >= 100 :
                print(" --------------------------------------- ")
                print(f"| ID Sapi      : {id}{' '*22}|")
                print(f"| Jenis Sapi   : {jenis}{' '*18}|")
                print(f"| Berat Sapi   : {berat} kg{' '*17}|")
                print(" --------------------------------------- ")
    elif id >= 10 :
        if jenis == "Pedaging" :
            if berat < 100 :
                print(" --------------------------------------- ")
                print(f"| ID Sapi      : {id}{' '*21}|")
                print(f"| Jenis Sapi   : {jenis}{' '*15}|")
                print(f"| Berat Sapi   : {berat} kg{' '*18}|")
                print(" --------------------------------------- ")
            elif berat >= 100 :
                print(" --------------------------------------- ")
                print(f"| ID Sapi      : {id}{' '*21}|")
                print(f"| Jenis Sapi   : {jenis}{' '*15}|")
                print(f"| Berat Sapi   : {berat} kg{' '*17}|")
                print(" --------------------------------------- ")
        elif jenis == "Perah" :
            if berat < 100 :
                print(" --------------------------------------- ")
                print(f"| ID Sapi      : {id}{' '*21}|")
                print(f"| Jenis Sapi   : {jenis}{' '*18}|")
                print(f"| Berat Sapi   : {berat} kg{' '*18}|")
                print(" --------------------------------------- ")
            elif berat >= 100 :
                print(" --------------------------------------- ")
                print(f"| ID Sapi      : {id}{' '*21}|")
                print(f"| Jenis Sapi   : {jenis}{' '*18}|")
                print(f"| Berat Sapi   : {berat} kg{' '*17}|")
                print(" --------------------------------------- ")

    kebutuhan = (10*berat/100)*30
    hijauan = 60*kebutuhan/100
    konsentrat = 40*kebutuhan/100

    if jenis == "Pedaging" :
        print(f" Kebutuhan Pakan /Bulan = {kebutuhan} kg")
        print(f"")
        print(f" Hijauan         = {hijauan} kg")
        print(f"")
        print(f" Konsentrat      = {konsentrat} kg")
        print(f" -> Bungkil Kelapa  = {10*konsentrat/100} kg")
        print(f" -> Bungkil Jagung  = {30*konsentrat/100} kg")
        print(f" -> Dedak           = {54.8*konsentrat/100} kg")
        print(f" -> Mineral Mix     = {0.2*konsentrat/100} kg")
        print(f" -> Tepung Ikan     = {0.2*konsentrat/100} kg")
        print(f" ")
        print(f" Vitamin & Mineral = {2*kebutuhan/100} kg")
        print(" --------------------------------------- ")
    elif jenis == "Perah" :
        print(f" Kebutuhan Pakan /Bulan = {kebutuhan} kg")
        print(f" ")
        print(f" Hijauan         = {hijauan} kg")
        print(f" ")
        print(f" Konsentrat      = {konsentrat} kg")
        print(f" -> Bungkil Kelapa =  {25*konsentrat/100} kg")
        print(f" -> Bungkil Kacang =  {20*konsentrat/100} kg")
        print(f" -> Tepung Jagung  =  {25*konsentrat/100} kg")
        print(f" -> Dedak Padi     =  {25*konsentrat/100} kg")
        print(f" -> Ampas Tahu     =  {1*konsentrat/100} kg")
        print(f" -> Garam Dapur    =  {1*konsentrat/100} kg")
        print(f" -> Kapur          =  {1*konsentrat/100} kg")
        print(f" -> Tepung Tulang  =  {1*konsentrat/100} kg")
        print(f" ")
        print(f" Vitamin & Mineral = {2*kebutuhan/100} kg")
        print(" --------------------------------------- ")
    else :
        print("Error")