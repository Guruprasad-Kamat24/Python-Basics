
def is_leap_year(y):
    a=y%4
    b=y%100
    c=y%400
    if(bool(a==0 and b!=0)):
        print(bool(a==0))
    elif(bool(a!=0 and c!=0)):
        print(bool(a==0))



y=int(input("Enter the year: "))
is_leap_year(y)

