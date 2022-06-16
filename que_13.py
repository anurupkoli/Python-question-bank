list = []

for i in range(3):
    n = int(input("Enter the number: "))
    list.append(n)

largest = None
for i in list:
    if largest == None or i>largest:
        largest = i

print(f"Largest b/w {list} is {largest}")