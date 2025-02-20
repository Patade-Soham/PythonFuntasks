print("Welcome to tip calculator")
bill=float(input("What was your tolal bill? : "))
tip=int(input("How much percent tip you would like to give : "))
s=int(input("Number of people you want to split :"))

e= (bill+(tip/100)*bill)/s

print(f"Each person should pay {e}Rs/-")
