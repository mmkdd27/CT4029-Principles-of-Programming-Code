grade = int(input("enter your grade: %"))
if grade < 90:
    if grade < 80:
        if grade < 70:
            if grade < 60:
                print("F")
            else:
                print("D")
        else:
            print("C")
    else:
        print("B")
else:
    print("A")
