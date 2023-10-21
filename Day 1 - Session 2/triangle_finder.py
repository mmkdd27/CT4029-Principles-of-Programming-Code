side1 = int(input("enter the length of one side : "))
side2 = int(input("enter the length of another side : "))
side3 = int(input("enter the length of the final side : "))

if side1 == side2:
    if side2 == side3:
        print("the triangle is equilateral and isosceles since all sides are of the same length ")
    else:
        print("the triangle is is only isosceles since only two side are the same length ")
else:
    if side1 == side3:
        print("the triangle is is only isosceles since only two side are the same length ")

    elif side2 == side3:
        print("the triangle is is only isosceles since only two side are the same length ")
    else:
        print("the triangle is scalene since none of the sides are of matching lengths ")
