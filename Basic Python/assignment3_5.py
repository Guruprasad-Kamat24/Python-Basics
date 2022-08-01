num=int(input())
sum=0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num==sum:
    print("The sum of Cubes is {}. It is the same as the number {}.".format(sum,num))
elif num!=sum:
    print("The sum of Cubes is {}. It is NOT the same as the number {}.".format(sum,num))