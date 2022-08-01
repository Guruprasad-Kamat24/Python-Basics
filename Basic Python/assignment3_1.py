num=float(input("Enter the number: "))
if (num%2)==0:
    print("The number is even")
    y=num%4
    if y==0:
        print("This is the number we are looking for.It is divisible by 4")
    elif y!=0:
        print("Sorry the given number is not divisible by 4.The reminder after dividing by 4 is {0}".format(y))
elif (num%2)!=0:
    print("The number is odd")
    z = num % 3
    if z == 0:
        print("This is the number we are looking for.It is divisible by 3")
    elif z != 0:
        print("Sorry the given number is not divisible by 3.The reminder after dividing by 3 is {0}".format(z))