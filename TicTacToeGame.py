#fun game to under stand list
r1=["__", "__", "__"]
r2=["__", "__", "__"]
r3=["__", "__", "__"]

lis=[]
maps=[r1, r2, r3]
print(f'{r1}\n{r2}\n{r3}')


def check(p):   
    
    for i in range(3):
            
        if r1[i]==r2[i]==r3[i]==p:
            print(f'player {p} wins:')
            exit()

    for i in maps:               
        if i[0]==i[1]==i[2]==p:
            print(f'player {p} wins')
            exit()  
    if r1[0]==r2[1]==r3[2]==p:
       print(f'Player {p} wins')        
       exit()
    elif r3[0]==r2[1]==r1[2]==p:
          print(f'Player {p} wins')        
          exit()  
    


def cross():
    a=int(input("enter no row  :"))
    if a=='':
        print('Thanks for playing')
    b=int(input("enter no coloumn : "))
    if (a,b) in lis:
        print('Place already Taken!')
        cross()
    else:
        lis.append((a,b))
        maps[a-1][b-1]="X"
        print(f'{r1}\n{r2}\n{r3}')



def circles():
    a=int(input("enter no row  :"))
    if a=='':
        print('Thanks for playing')
    b=int(input("enter no coloumn : "))
    if (a,b) in lis:
        print('Place already Taken!')
        circles()
    else:
        lis.append((a,b))
        maps[a-1][b-1]="O"
        print(f'{r1}\n{r2}\n{r3}')



while (True):
      
    cross()
    check("X")
    circles()
    check("O")
    
    
    
    
    
    
    
    
    
    
    
    
    
