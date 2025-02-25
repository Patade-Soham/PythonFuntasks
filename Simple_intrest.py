def simple_intrest():
    P=int(input("Enter PRINCIPAL amt.: "))
    R=int(input("Enter Rate of intrest : "))
    T=int(input("Enter time in years : "))

    SI= (P*R*T)/100

    print(SI,"Rs/-")
    
simple_intrest()  
