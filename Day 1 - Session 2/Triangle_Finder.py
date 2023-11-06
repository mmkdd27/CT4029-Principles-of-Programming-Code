side1 = int(input("Enter the length of one side : "))
side2 = int(input("Enter the length of another side : "))
side3 = int(input("Enter the length of the final side : "))

if side1 == side2:
    # we check if the first two sides are the same length
    if side2 == side3:
        # if all three is the same it is equilateral
        print("The triangle is equilateral and isosceles since all sides are of the same length ")
    else:
        # if 2 and 1 are the sma e length but 3 isn't its isosceles
        print("The triangle is is only isosceles since only two side are the same length ")
else:
    if side1 == side3:
        # we check if the first and third sides are the same length
        print("The triangle is is only isosceles since only two side are the same length ")
    elif side2 == side3:
        print("The triangle is is only isosceles since only two side are the same length ")
        # since we know 1 isn't the same length as 2 we check if the second and third sides are the same length
    else:
        print("The triangle is scalene since none of the sides are of matching lengths ")