height=(input("Enter height of students")).split(" ")

for n in range(0,len(height)):
  
    height[n]=int(height[n])
add=0
for  val in height:
    add=add+val
    
print('average height is ',add/len(height))  

#alternate method
# height=(input("Enter height of students")).split(" ")

# for n in range(0,len(height)):
#     height[n]=int(height[n])

# a=sum(height)/len(height)

# print(a)
