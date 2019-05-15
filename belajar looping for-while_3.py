#piramida terbalik
i = 5
while i>0:
	j=1
	while j<=i:
		print("*",end="")
		j+=1
	print()
	i-=1

for i in range (5,0,-1):
	for j in range (1,-1):
		print("*",end="")
	print()