import math as math

side1 = int(input("Enter the length of one side : "))
side2 = int(input("Enter the length of another side : "))
side3 = int(input("Enter the length of the final side : "))
s = (side1 + side2 + side3) // 2
print("The area of the triangle is : ", math.sqrt((side1 + side2 + side3) // 2))

if side1 == side2:
    if side2 == side3:
        print("The triangle is equilateral and isosceles since all sides are of the same length ")
    else:
        print("The triangle is is only isosceles since only two side are the same length ")
else:
    if side1 == side3:
        print("The triangle is is only isosceles since only two side are the same length ")

    elif side2 == side3:
        print("The triangle is is only isosceles since only two side are the same length ")
    else:
        print("The triangle is scalene since none of the sides are of matching lengths ")
