from re import A


a = 0
b = 1
c = 0
print(0)
print(1)
while True:
    c = b
    b = a+b
    a = c
    if b > 34:
        break
    print(b)