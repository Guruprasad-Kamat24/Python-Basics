lucky_no=[4,8,15,16,23,42]
friends = ["Kevin", 2, "Jim","Jim", False]

friends.extend(lucky_no)
print(friends)

friends.append("Creed")
print(friends)

friends.insert(1,"Kelly")
print(friends)

friends.remove("Jim")
print(friends)

friends.pop()
print(friends)

print(friends.index("Kevin"))

friends = ["Kevin", 2, "Jim","Jim", False]

print(friends.count("Jim"))

lucky_no.sort()
print(lucky_no)

lucky_no.reverse()
print(lucky_no)

friends2=friends.copy()
print(friends2)

friends.clear()
print(friends)