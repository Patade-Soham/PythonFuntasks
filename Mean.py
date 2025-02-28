def avg():
    nums=input("Enter the numbers").split(' ')

    n=0
    for i in range(0,len(nums)):
        n=int(nums[i])+n

    mean=n//len(nums)

    print(f'The mean of the numbers is {mean}')   
avg()

    
