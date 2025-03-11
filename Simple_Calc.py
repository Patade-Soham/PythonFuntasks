


def add():
    summ= a+b
    print(summ)
def sub():    
    subt= a-b
    print(subt)
def multi():   
    mult= a*b
    print(mult)
def div():    
    divv = a/b
    print(divv)
def modd():    
    mod= a%b
    print(mod)
        
    

print('''
     
1. ADD
2. SUB
3. MUL
4. DIV
5. MOD
6. end
      
      
      ''')
     
while(1):
    
    a=int(input("Enter first integer : "))
    b=int(input("Enter first integer : "))
    i = int(input("Enter opertor number: "))
    if i==1:
        add()
    elif i==2:
        sub()
    elif i==3:
        multi()
    elif i==4:
        div()
    elif i==5:
        modd()
    else:
        print('wrong Choice')
    
 




