#membuat piramida bintang * menggunakan for dan while
for i in range (0,5):
	for j in range(0,i+1):
		print("*",end="")
	print()

i=0
while i<5:
    j=0
    while j<=i:
        print("*",end="")
        j+=1
    print()
    i+=1