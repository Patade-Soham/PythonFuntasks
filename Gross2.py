def gross():
    bs= int(input("Enter basic Salary : "))
    da= bs*0.7
    ta= bs*0.30
    hra= bs*0.10
    add = bs+da+ta+hra
    return add
gross() 

size=10   
enp=[]
for i in range(size):
    gross_value=gross()
    enp.append(gross_value)

print(enp)
