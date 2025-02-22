score=(input("Enter score of students")).split(" ")

for n in range(0,len(score)):
    score[n]=int(score[n])

heighest=score[0]

for a in score :
    if a>heighest:
        heighest=a        
print(a)
