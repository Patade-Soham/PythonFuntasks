import random

print("********Welcome to Rock, Papers and scissors********")

a=int(input("0.rock\n1.paper\n2.scissors\n\n Enter your choice : "))

rock=0
paper=1
scissors=2

ur_choice=[rock, paper, scissors]

print(ur_choice[a])

comp_choice=random.randint(0, 2)

print(ur_choice[comp_choice])

if a>=3 or a<0:
    print("INVALID CHOICE YOU LOSE !")
elif a==comp_choice:
    print("ITS A DRAW")
elif a==0 and comp_choice==2:
     print("YOU WIN!")
elif a==2 and comp_choice==0:
     print("YOU LOSE")
elif a>comp_choice:
    print("YOU WIN!")
elif a<comp_choice: 
    print("YOU LOSE!")
else :
    print('INVALID CHOICE')
    
print("Thankyou!")    

