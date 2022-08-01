def drawpattern(n):
    for x in range(0,n):
        for y in range(0,n):
            if x>=y:
                print('*',end='')
        print('')
n=int(input("Enter the no of rows: "))
drawpattern(n)
