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



# above enhanced code  --Nitesh

# def findSmallest(lst):
#     lst.sort()
#     for i in range(len(lst)+1):
#         if lst[i] == lst[i+1]:
#             continue
#         else:
#             return lst[i+1]
    
# nums = input("enter number by single space: ").split()
# num_list = [int(i) for i in nums]
# print(f"The second smallest number in the list is {findSmallest(num_list)}")


# with lambda  --Nitesh
# just added lambda function 😅


# l = lambda a,b : a == b
# def findSmallest(lst):
#     lst.sort()
#     for i in range(len(lst)+1):
#         if l(lst[i],lst[i+1]):
#             continue
#         else:
#             return lst[i+1]
    
# nums = input("enter number by single space: ").split()
# num_list = [int(i) for i in nums]
# print(f"The second smallest number in the list is {findSmallest(num_list)}")




