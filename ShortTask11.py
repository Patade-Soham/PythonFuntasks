#sum of evens
a=[]
for n in range(1,101):
    if n%2==0:
        a.append(n)
        
print(sum(a))

#sum of odds   
b=0
for n in range(1,101,2):
    b=n+b
print(b)  
