countE = 0
countO = 0
sumE = 0
sumO = 0

while True:
    x = input("Enter a number: ")
    if x == "done":
        break
    x = int(x)
    if x%2 == 0:
        countE += 1
        sumE += x
    else:
        countO += 1
        sumO += x

print(f"Total numbers of even no. is {countE} and sum is {sumE}")
print(f"Total numbers of odd no. is {countO} and sum is {sumO}")