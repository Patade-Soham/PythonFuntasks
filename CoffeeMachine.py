
logo='''
 >>>>>>>WELCOME TO COFFEE MACHINE<<<<<<<
'''

latte_e='''
  .====.
,|`===='|
||      |
`|      |  
  `-__-'

'''

cap='''
   ( (
    ) )
  ........
  |      |]
  \      /    
   `----'
'''

esp='''
         {
      {   }
       }_{ __{
    .-{   }   }-.
   (   }     {   )
   |`-.._____..-'|
   |             ;--.
   |            (__  \\
   |             | )  )
   |             |/  /
   |             /  /    
   |            (  /
   \             y'
    `-.._____..-'
'''

menu={
    'espresso' : {
        'ingredient': {
            'water': 50,
            'coffee' : 18,
            'milk' : 0 
        },
        'cost': 150

    },
    'latte' : {
        'ingredient': {
            'water': 200,
            'coffee' : 24,
            'milk' : 150
        },
        'cost': 250
        
    },
    'cappuccino' :{
        'ingredient': {
            'water': 250,
            'coffee' : 24,
            'milk' : 100
        },
        'cost': 300
    }

}

coffee=100
water=500
milk=300
money=0
loop=True




def order(item):
     global coffee, water, milk, money 
     coffee =coffee - menu[item]['ingredient']['coffee']
     milk = milk - menu[item]['ingredient']['milk']
     water = water - menu[item]['ingredient']['water']
     
     
     if coffee < menu[item]['ingredient']['coffee']:
          print('Not enough coffee in the machine ')
     elif milk <  menu[item]['ingredient']['milk']:
         print('Not  enough milk')
     elif water < menu[item]['ingredient']['water']:
          print('Not enough water ')
     else:
          bill = menu[item]['cost']
          
          print(f'Anount to pay : {bill}Rs')
          print('You can pay in 10, 20 and 50 only.')
          a=int(input('pay in 10rs :')) * 10
          b=int(input('pay in 20rs :')) * 20
          c=int(input('pay in 50rs :')) * 50
          d = a+b+c
          if d < bill:
               print('Amount required ', bill, 'Invalid')
               
          else:
               money = money + menu[item]['cost']
               print(f'Here is your {item}')
               if bill < d :
                    return_amt=d-bill
                    print(f'Here is your change. {return_amt}Rs.')
             
            
def check_machine():
      print(f'coffee : {coffee}')
      print(f'milk : {milk}')
      print(f'water : {water}')
      print(f'money : {money}')

def reset():
    global coffee, water, milk, money 
    coffee=100
    water=500
    milk=300
    money=0
             

def machine():
              
    print('''
    1. Espresso
    2. Latte
    3. Cappuccino  
    4. Report    
            ''')
    choice=int(input('What would you like to have ? : '))
    if choice == 1:       
            order('espresso')
            print(esp)
    elif choice == 2 :
            order('latte')
            print(latte_e)
    elif choice == 3:
            order('cappuccino')
            print(cap)
    elif choice==4:
        check_machine()
    else:
        reset()
    
   
   
while True:
     print(logo)
     start=int(input('1.Order\n2.exit..\nEnter your choice : '))

     if start == 1:
          machine()
     elif start==2:
          print('Thankyou!')
          break   
     else:
          print('Invalid Choice')  
    

     
