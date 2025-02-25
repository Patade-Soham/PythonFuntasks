print ("//Welcome to profit calculator//")
cp=input("Enter cost price : ")
a=int (cp)
sp=input("selling Price :")
b=int(sp)
c= b-a
            
profit= c/a*100
            
if(a<b):
    print("Congo! you made a profit of :",profit,"%")
            
if(a>=b):
      print("You made a loss of",profit*-1,"%")
                    
print("Thank you!")
