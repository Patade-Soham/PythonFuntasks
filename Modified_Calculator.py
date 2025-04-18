
def add(a,b):
    return a+b
   
def sub(a,b):    
   return a-b
    
def multi(a,b):   
    return a*b
def div(a,b):    
    return a/b
 
def modd(a,b):    
   return a%b

operations={'+': add,
            '-': sub,
            '*':multi,
            '/':div,
            '%':modd
    }


def calc():
    a=int(input("Enter first integer : "))
    for key in operations:
        print(key)
    operator=input('Enter the operator :')    

    b=int(input("Enter second integer : "))
    calc_func=operations[operator]  
    answer=calc_func(a,b)
    print(f'{a} {operator} {b} = {answer}')
    return answer



def calc_more(answer):
    operation_symbol=input('enter the operator : ')
    num3=int(input('Enter integer : '))
    calc_func=operations[operation_symbol]
    answer=calc_func(answer,num3)
    print(f'{answer} {operation_symbol} {num3} = {answer}')
    return answer
    
print('''
  _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

      ''')
prev_ans=calc()
while True:
    
    

    choice=input('press "y" to calculate with same value or press "n" for new calculation and "e" for exit : ')
    if choice=='y':
        prev_ans=calc_more(prev_ans)
        
    elif choice == 'n':
        prev_ans=calc()
    else:
        break
    
print('exited.....')    
    
