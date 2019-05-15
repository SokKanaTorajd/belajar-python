#menggunakan perulangan for
#mencetak bilangan ganjil <15 menggunakan perulangan for dan continue
for i in range (15):
	if i%2==0 :
		continue #jika kondisi tersebut benar, maka angka yang habis dibagi 2 tidak akan ditampilkan
	print(i)