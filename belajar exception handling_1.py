#exception handling
try:
    print("Pembagian")
    a=float(input("masukkan angka ke-1 : "))
    b=float(input("masukkan angka ke-2 : "))
    c=a/b
    print("%f dibagi %f = %f"%(a,b,c))
except ZeroDivisionError:
    print("Tidak Terdefinisi. Masukkan angka selain 0. ")
except ValueError:
    print("inputan harus angka.")
