import random        

letter= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

symbol=['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

nums=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


print('>>>>>>WELCOME TO PASSWORD GENERATOR<<<<<<<\n\n')

a=int(input("How many characters do you want : "))
b=int(input("How many symbols do you want : "))
c=int(input("How many numbers do you want : "))

password=""


for char in range(a):
    d=str(random.choice(letter)) 
    password=password+d

    
for char in range(b):
    e=str(random.choice(symbol))
    password=password+e

    
for char in range(c):
    f=str(random.choice(nums)) 
    password=password+f


print("your password is : ",password)
