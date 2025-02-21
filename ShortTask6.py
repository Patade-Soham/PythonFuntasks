# who pays the bill
import random

a=input("Give the name of the people seperated by ',' : ")
name= a.split(", ")
print(name[random.randint(0, (len(name)-1))],"is going to pay the bill.")
