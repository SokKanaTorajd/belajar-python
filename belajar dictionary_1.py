#belajar dictionary
#1
midterm1 = {"Mady":8, "Roger":5, "Paul":5, "Lucy":7}
print("1. score d-1 ",midterm1)
#2
midterm2 = {"Ken":8, "Andrea":7, "Smith":6}
print("2. score d-2 ",midterm2)
#3
midterm1.update(midterm2)
print("3. total score ",midterm1)
#4
midterm1["Roger"]=8
midterm1["Paul"]=8
midterm1["Smith"]=8
print("4. re-score",midterm1)
#5
for name,score in midterm1.items():
    if score >=8:
        print("score %s is %s"%(name,score))