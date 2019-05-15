#program ini menggabungkan perkondisian dan fungsi untuk melakukan write dan read file
def option():
	print("BIODATA")
	print("1. Tulis biodata")
	print("2. Tampilkan biodata")
	pilih = int(input("pilihan anda : "))
	return pilih
def write():
	f = open("biodata.txt","w")
	f.write(a = input("masukkan nama anda :"))
	f.write(b =input("masukkan tanggal lahir  anda :"))
	f.write(c = input("masukkan asal anda :"))
	f.close()
def read():
	f = open("biodata.txt","r")
	print(f.read())
	
pilihan = option()
if pilihan == 1:
	write()
else:
	read()