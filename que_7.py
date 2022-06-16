from re import L


list = []

while True:
    n = input("Enter the no.: ")
    if n == "done":
        break
    try:
        n = int(n)
    except:
        print("Enter a valid integer")
    list.append(n)

print("Largest no. is", max(list))
print("Smallest no. is",  min(list) )