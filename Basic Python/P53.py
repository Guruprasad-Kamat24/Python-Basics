test_str =input("Enter the string: ")
all_freq = {}
for i in test_str:
	if i in all_freq:
		all_freq[i] += 1
	else:
		all_freq[i] = 1
print (" \n"+ str(all_freq))
