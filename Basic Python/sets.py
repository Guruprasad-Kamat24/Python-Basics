a={1,4,2.4,'aaa','abc',9,2}
b=set([1,4,3,'abc',87])
print(a)
print(b)

#lenght of set
print(len(a))

#acces set elements
for x in a:
    print(x)

#adding elements to a set
a.add(3)
print(a)
a.update([3,'aa'])
print(a)

#remove element
a.remove('aaa')
print(a)
a.discard(3)
print(a)
a.pop()
print(a)