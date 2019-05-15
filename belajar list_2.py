#belajar list
#1
jakarta = ["","Wiliam","Kate","Anderson","Jame","Mady"]
print("a.",jakarta)
#2
jakarta.append("Jones")
print("b.",jakarta)
#3
jakarta[3]="Grace"
print("c.",jakarta)
#4
member = "Thompson" in jakarta
print("d. Thompson ada di dalam kereta : ",member)
#5
print("e.",sorted(jakarta))
#6
for p in jakarta:
    print(p)
#7
jakarta.clear()
print("g. ",jakarta)