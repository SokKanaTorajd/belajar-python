#membuat program menghitung luas dan keliling persegi panjang menggunakan fungsi
def option ():
    print("pilih salah satu program : ")
    print("1. luas persegi panjang")
    print("2. keliling persegi panjang")
    print("3. keluar program")
    pilihan = int(input("pilihan anda : "))
    return pilihan

def luas_pp():
    panjang = int(input("masukkan panjang : "))
    lebar = int(input("masukkan lebar : "))
    luas = panjang*lebar
    print("Luas = ",luas)
    return luas

def keliling_pp():
    panjang = int(input("masukkan panjang : "))
    lebar = int(input("masukkan lebar : "))
    keliling = 2*(panjang+lebar)
    print("Keliling =", keliling)
    return keliling
opt = option()

while True:
    if opt == 1:
        luas_pp()
        print("kembali? y/n")
        a = input()
        if a == "y" or "Y":
            opt
        else:
            break
    elif opt == 2:
        keliling_pp()
        print("kembali? y/n") 
        a = input()
        if a == "y" or "Y":
            opt
        else:
            break
    else:
        print("Terima Kasih :)")
        break