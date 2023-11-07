a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = int(input("Enter the third number"))
d = int(input("Enter the fourth number"))
e = int(input("Enter the fifth number"))
print((a + b + c + d + e) / 5)
# second way
numbers = 5
c = 0
for i in range(1, numbers + 1):
    a = int(input())
    c = a + c

print(c / numbers)
