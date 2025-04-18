
def leap_year(year):
    b=year/4
    c=year/100
    d=year/400


    if b==int(b):
        if c==int(c):
            if d==int(d):
                return True
              
            else:
                return False
        else:
          return True
    else:
      return False
  
def Day_in_month(month):
    months_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if leap_year(year)==False:
        days=months_days[month - 1]
        return days
    elif leap_year(year)==True:
        if month==2:
            days=months_days[month-1]+1
            return days
        else:
            days=months_days[month-1]
            return days
            
year=int(input("Enter Year : "))
month=int(input('Enter number of month : ')) 

number_of_days=Day_in_month(month)      
print(number_of_days) 
  
