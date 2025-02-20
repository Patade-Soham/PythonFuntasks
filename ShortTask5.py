print("\n\n\n>>>>welcome to python pizza<<<< \n\n\n")
  
print(" small pizza(s)  : $4 \n medium pizza(m) : $5 \n large pizza(l)  : $6 \n\n\n add peperoni for small : +$1 \n add peperoni for med and large : $2 \n\n add cheese : +$1")
g=input("would you like to order pizza? (y/n) : ")

bill=0
if g=="y":
   a=input("\nEnter size of pizza (s\m\l): ")
   if a=="s":
       bill=bill+4
   elif a=="m":    
       bill=bill+4
   else:
       bill=bill+6
       
   b=input("\nWould you like to add peperoni (y/n) : ")    
   c=input("\nwould you like to cheese (y/n) :  ")
   if b=="y":
       if a=="s":
          bill=bill+1
       else:
         bill=bill+2 
   if c=="y":
       bill=bill+1  
   print("\nYour final bill is :",bill,"Rs/-\n")    
   print("THANKYOU !!!!!")
else :
   print("Thank you")     
