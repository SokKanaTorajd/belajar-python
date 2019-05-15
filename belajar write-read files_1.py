#menulis dan membaca file di python menggunakan perintah write dan read
# a artinya append menimbun data yang baru sehingga data yang lama masih ada. 
#jika w artinya write, data yang baru dimasukkan akan menggantikan data yang lama.

def tulis():
	file=open("biodata.txt","a") 
	nama=str(input("nama anda : "))
	tgl =str(input("tanggal lahir anda : "))
	ori = str(input("asal anda : "))
	file.write("nama : {} \n".format(nama))
	file.write("tgl:{}\n".format(tgl))
	file.write("asal : {} \n".format(ori))
	file.close()

def baca():
	file=open("biodata.txt","r")
	print(file.read())

tulis()
print("\n \t\tDaftar Biodata\n")
baca()