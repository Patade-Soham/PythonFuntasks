#add remove update sort
lis=[]


def adding():
    a=input("what you want to add in list : ")
    lis.append(a)
    print(lis)

def dump():
    b=int(input("Enter index of element you want to remove : "))
    lis.remove(lis[b])
    print(lis)
    
def new():
    c=int(input("index : "))
    d=input("new element : ")
    lis[c]=d
    print(lis)
    
def arr():
    lis.sort()
    print(lis)
    
    

while(True):
    print("wlecome to list manager\n\n")
    print('''1-add
          2-remove
          3-update
          4-arr
          5-exit... ''')
    
    
    
    f=int(input("Enter your choice : "))
    
    if f==1:
        adding()
    elif f==2:
        dump()
    elif f==3:
        new()
    elif f==4:
        arr()
    elif f==5:
        break
    else:
        print ("wrong choice")
        
      
