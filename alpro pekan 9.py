#start program
print ("Selamat Datang di Python Pizza")
#pelanggan memilih topping pizza
print("Disini kami memiliki beberapa varian toping yakni:")
print("1. Frankfurter")
print("2. Meat monsta")
print("3. Super supreme")
print("4. Super supreme chicken")
ToppingPizza = input ("Pilih topping kesukaan anda? ")
HargaPizza = 0 ;
#setelah memilih menu maka
if (ToppingPizza == "frankfurter"):
    print ("harga pizza dengan topping ini = Rp. 43.636")
    HargaPizza += 43636
elif (ToppingPizza == "meat monsta"):
    print ("harga pizza dengan topping ini adalah = Rp. 43.636")
    HargaPizza += 43636
elif (ToppingPizza == "super supreme"):
    print ("harga pizza dengan topping ini adalah = Rp. 43.636")
    HargaPizza += 43636
elif (ToppingPizza == "super supreme chicken"):
    print ("harga pizza dengan topping ini adalah = Rp. 43.636")
    HargaPizza += 43636
else :
    print ("tidak ada pilihan")
#pemilihan crust dan ukuran pizza    
print ("silahkan pilih crust")
print ("1.pan")
print ("2.stuffedcrust cheese")
print ("3.stuffedcrust sausage")
print ("4.cheesy bites")
print ("5.crown crust")
crustPizza = input("pilih crust pizza: ")
crustPizza = crustPizza.lower()
if (crustPizza == "pan"):
    print ("harga pizza dengan crust ini adalah rp 43.636")
    hargaCrust = HargaPizza + 0
    print ("pilih ukuran pizza yang anda inginkan : ")
    print ("1.personal")
    print ("2.reguler")
    print ("3.large")
    ukuranPizza = input("pilih ukuran pizza: ")
    hargaUkuran = 0 ;
    ukuranPizza = ukuranPizza.lower()
    if (ukuranPizza == "personal"):
        hargaUkuran += hargaCrust + 0
    elif (ukuranPizza == "reguler"):
        hargaUkuran += hargaCrust + 57273
    elif (ukuranPizza == "large"):
        hargaUkuran += hargaCrust + 89091
    else:
        print ("tidak ada pilihan")

elif (crustPizza == "stuffedcrust cheese"):
    print ("harga pizza dengan crust ini adalah rp 55.455")
    hargaCrust = HargaPizza + 11818
    print ("silahkan pilih ukuran")
    print ("1.personal")
    print ("2.reguler")
    print ("3.large")
    ukuranPizza = input("pilih ukuran pizza: ")
    hargaUkuran = 0 ;
    ukuranPizza = ukuranPizza.lower()
    if (ukuranPizza == "personal"):
        hargaUkuran += hargaCrust + 0
    elif (ukuranPizza == "reguler"):
        hargaUkuran += hargaCrust + 65455
    elif (ukuranPizza == "large"):
        hargaUkuran += hargaCrust + 104545
    else:
        print ("tidak ada pilihan")

elif (crustPizza == "stuffedcrust sausage"):
    print ("harga pizza dengan crust ini adalah rp 52.727")
    hargaCrust = HargaPizza + 9091
    print ("silahkan pilih ukuran")
    print ("1.personal")
    print ("2.reguler")
    print ("3.large")
    ukuranPizza = input("pilih ukuran pizza: ")
    hargaUkuran = 0 ;
    ukuranPizza = ukuranPizza.lower()
    if (ukuranPizza == "personal"):
        hargaUkuran += hargaCrust + 0
    elif (ukuranPizza == "reguler"):
        hargaUkuran += hargaCrust + 64545
    elif (ukuranPizza == "large"):
        hargaUkuran += hargaCrust + 102727
    else:
        print ("tidak ada pilihan")

elif (crustPizza == "cheesy bites"):
    print ("harga pizza dengan crust ini adalah rp 57.272")
    hargaCrust = HargaPizza + 13636
    print ("silahkan pilih ukuran")
    print ("1.personal")
    print ("2.reguler")
    print ("3.large")
    ukuranPizza = input("pilih ukuran pizza: ")
    hargaUkuran = 0 ;
    ukuranPizza = ukuranPizza.lower()
    if (ukuranPizza == "personal"):
        hargaUkuran += hargaCrust + 0
    elif (ukuranPizza == "reguler"):
        hargaUkuran += hargaCrust + 66364
    elif (ukuranPizza == "large"):
        hargaUkuran += hargaCrust + 107273
    else:
        print ("tidak ada pilihan")

elif (crustPizza == "crown crust"):
    print ("harga pizza dengan crust ini adalah rp 55.454")
    hargaCrust = HargaPizza + 11818
    print ("silahkan pilih ukuran")
    print ("1.personal")
    print ("2.reguler")
    print ("3.large")
    ukuranPizza = input("pilih ukuran pizza: ")
    hargaUkuran = 0 ;
    ukuranPizza = ukuranPizza.lower()
    if (ukuranPizza == "personal"):
        hargaUkuran += hargaCrust + 0
    elif (ukuranPizza == "reguler"):
        hargaUkuran += hargaCrust + 65455
    elif (ukuranPizza == "large"):
        hargaUkuran += hargaCrust + 104545
    else:
        print ("tidak ada pilihan")
else:
    print ("tidak ada pilihan")

if (ukuranPizza == "personal"):
    extraCheese = 13636
elif (ukuranPizza == "reguler"):
    extraCheese = 16364
elif (ukuranPizza == "large"):
    extraCheese =  19091
else:
    print("tidak ada dipilih")

extra = input(f"extracheese? +Rp. {extraCheese} y/n: ")
if extra == "y":
    hargatotal = hargaUkuran + extraCheese
elif extra == "n":
    hargatotal = hargaUkuran
else:
    print ("tidak ada yang dipilih")
print (f"total pesanan anda adalah :Rp. {str(hargatotal)}")