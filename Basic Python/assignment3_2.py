a=float(input("Enter the number: "))
b=float(input("Enter the number: "))
c=float(input("Enter the number: "))
if a>=b and a>=c:
    x=a
elif b>=a and b>=c:
    x=b
elif c>=a and c>=b:
    x=c
print(x)