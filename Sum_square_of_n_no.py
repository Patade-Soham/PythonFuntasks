nums=int(input("Enter the no : "))

n=0
for i in range(0,nums+1):
    n=n+i**2
    
print(f'The sum of square of natural numbers from 1 to {nums} is {n}')
