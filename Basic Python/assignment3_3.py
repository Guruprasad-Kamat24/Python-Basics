a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=int(input("Enter the number: "))
n=int(input("Enter the value of n: "))
if n>2:
    print("{},{},{} do not satisfy Fermat equation as n is greater than 2.".format(a,b,c))
elif n==0:
    print("{},{},{} satisfy Fermat equation trivially.".format(a, b, c))
elif n==1 or n==2:
    print("{},{},{} satisfy Fermat equation for n ={}".format(a, b, c, n))
elif n<0:
    print("ERROR: n must be a non-negative integer.")