string = input("Enter a string: ")
str_rev = ''.join(reversed(string))
if string == str_rev:
    print("Yes")
else:
    print("No")