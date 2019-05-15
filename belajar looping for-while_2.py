#membuat matriks menggunakan for dan while
for i in range (0,2):
	for j in range(0,+3):
		print("*",end="")
	print()

i=0
while i<2:
	j=0
	while j<3:
		print("*",end="")
		j+=1
	print()
	i+=1