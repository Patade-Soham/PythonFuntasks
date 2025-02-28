lis=[]
nums=input("Enter the numbers").split(' ')
n=0
a=0
for i in range(len(nums)):
    n=int(nums[i])
    lis.append(n)
    lis.sort()
    a=lis[0]

for i in range(lis.count(a)):
     lis.remove(a)
     
print(f'The second smallest integer is {lis[0]}')
