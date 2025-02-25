a=int(input("Enter your weight : "))
b=float(input("Enter your height : "))

c=a/(b/100)**2

print("Your BMI is : ",c)

if c<18.5:
    print("You are under weight")
elif 18.5<c<25:
    print("You have normal weight")
elif 25<c<30:
    print("Your are over weight")
else :
    print("You come under obesse category")
