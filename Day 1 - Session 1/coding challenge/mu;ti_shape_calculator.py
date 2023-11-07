import math

while True:  # this is so the prgram doesnt close after the calculation is done
    print("Choose a shape to calculate its area:")
    print("1. Rectangle")
    print("2. Square")
    print("3. Circle")
    print("4. Triangle")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        print("The area of the rectangle is:", area)

    elif choice == '2':
        side = float(input("Enter the length of one side of the square: "))
        area = side * side
        print("The area of the square is:", area)

    elif choice == '3':
        radius = float(input("Enter the radius of the circle: "))
        area = math.pi * (radius ** 2)
        print("The area of the circle is:", area)

    elif choice == '4':
        base = float(input("Enter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        print("The area of the triangle is:", area)

    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
