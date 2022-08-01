r=int(input("Enter the no. of rows: "))
c=int(input("Enter the no. of columns: "))
matrix=[]
print("Enter the entries row wise: ")
for i in range (r):
    a=[]
    for j in range (c):
        a.append(int(input()))
        matrix.append(a)

for i in range (r):
    for j in range (c):
        print(matrix[i][j],end=" ")
    print()

k=int(input("Enter the key no to be found: "))
for i in range (r):
    for j in range (c):
        