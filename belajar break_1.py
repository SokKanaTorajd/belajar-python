#break pada perulangan for
for i in range (0,5): #(start,stop, step).utk program ini start dari 0 kemudaian berhenti pada indeks ke -5
	if i==3:
		print("this line is a break")
		break #berhenti pada kondisi yang telah ditentukan. apabila kondisi terpenuhi, maka program berhenti
	print(i)