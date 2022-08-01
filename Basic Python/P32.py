n=int(input("Enter the no of rows: "))
for i in range(65,65+n):
    for j in range(65,i+1):
        print("_"+chr(j),end="_")
    print()
