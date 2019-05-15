#penggunaan contiunue pada for
for i in range (0,6):
	if i == 3:
		continue #melompati kondisi yg ditentukan, kemudian melanjutkan kondisi selanjutnya
		#operasi/kondisi yang ada setelah continue akan diabaikan
		print("ini continue")
	print("sekarang angka: ",i)