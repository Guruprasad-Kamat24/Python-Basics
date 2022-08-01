
lucky_numbers = [4, 8, 15, 16, 42, 23]
friends= ["Kelvin", "Karen", "Jim", "Tobby"]
friends.extend(lucky_numbers)
print(friends)

print(friends.index("Jim"))

friends.append("Creed")
print(friends)

friends.insert(1, "Guru")
print(friends)

friends.remove("Jim")
print(friends)

friends.pop()
print(friends)

friends.clear()
print(friends)

friends= ["Kelvin", "Karen", "Jim", "Jim", "Tobby"]
print(friends.count("Jim"))

friends.sort()
print(friends)

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2= friends.copy()
print(friends2)