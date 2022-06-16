def cal_n_no(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

def area_sq(s):
    area = s*s
    return area

no = int(input("Enter a number: "))
side = float(input("Enter the side of square: "))

sum = cal_n_no(no)
area = area_sq(side)

print(f"Sum of first {no} numbers is {sum}")
print(f"Area of square is {area}")