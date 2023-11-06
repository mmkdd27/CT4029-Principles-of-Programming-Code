a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print((a + b + c + d + e) / 5)
# second way
numbers = 5
c = 0
for i in range(1, numbers + 1):
    a = int(input())
    c = a + c

print(c / numbers)
