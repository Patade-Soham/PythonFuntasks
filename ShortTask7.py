#fun game to under stand list
r1=["😃", "😃", "😃"]
r2=["😃", "😃", "😃"]
r3=["😃", "😃", "😃"]

map=[r1, r2, r3]
print(f'{r1}\n{r2}\n{r3}')

a=int(input("enter no row  :"))
b=int(input("enter no coloumn : "))

map[a-1][b-1]="x"
print(f'{r1}\n{r2}\n{r3}')
