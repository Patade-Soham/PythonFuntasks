
print(">>>>WELCOME TO PRIME NUMBER CALCULATOR<<<<\n\n\n")

num=int(input("Enter a Number : "))
lis=[]
for i in range(1,num+1):
    a=num/i
    if a==int(a):
        lis.append(a)
if len(lis)==2:
    print(f"{num} is a prime number ")
elif len(lis)>2:
    print(f"{num} is not a prime number" )
            
        
