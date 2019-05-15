#belajar set
hari_pertama = {"keju","tepung","garam","gula","coklat"}
hari_kedua = {"garam","gula","coklat","kecap"}
print("a. hari pertama = ",hari_pertama)
print("   hari kedua = ",hari_kedua)
b = hari_kedua.add("keju") #menambahkan elemen/kata keju ke dalam set
print("b. hari kedua tambah keju = ",hari_kedua)
c = hari_pertama and hari_kedua #mencari irisan diantara 2 set(himpunan)
print("c. barang yang sama = ",c)
d = hari_pertama - hari_kedua #mencari selisih A-B
print("d. brg yg dibeli hari pertama tdk dibeli hari kedua = ",d)
e = hari_pertama.discard("garam") #menghapus elemen didalam set
print("e. hari pertama hapus garam = ",hari_pertama) #
f = hari_kedua - hari_pertama #mencari selisih B -A
print("f. brg yg dibeli hari kedua tdk dibeli hari pertama = ",f)
g = hari_pertama ^ hari_kedua #mencari elemen yang berbeda
print("g. barang yang tidak sama = ",g)
h = print("h. hari pertama = ",hari_pertama)
i = print("i. hari kedua = ",hari_kedua)