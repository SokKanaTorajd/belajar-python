#break pada perulangan while
i=0
while i<7:
	if i==5:
		print("this line is a break") #program akan berhenti jika i == 5
		break
	print(i)
	i+=1