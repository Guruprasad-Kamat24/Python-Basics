# Python3 program to
# Check if the string is pangram
import string


def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False

    return True


# Driver code
x=string(input(""))
if (ispangram(x) == True):
    print("Yes, the string is a pangram")
else:
    print("No, no the string is not a pangram.")
