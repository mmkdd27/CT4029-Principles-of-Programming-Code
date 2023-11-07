def reverser(s):
    str = ""
    for i in s:
        str = i + str
    return str


sring = input("enter your string: ")
print(reverser(sring))


#num1, num2, num3 = (input("enter your values sepertaed by a ','").split(","))
def maximizer(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        if num1 == num2 == num3:
            return num1, num2, num3
        elif num1 == num2:
            return num1, num2
        elif num1 == num3:
            return num1, num3
        else:
            return num1
    elif num2 >= num1 and num2 >= num3:
        if num2 == num3:
            return num2, num3
        else:
            return num2
    elif num3 >= num1 and num3 >= num2:
        return num3


def find_max_and_min(num1, num2, num3):
    maximum = num1
    minimum = num1

    if num2 > maximum:
        maximum = num2
    elif num2 < minimum:
        minimum = num2

    if num3 > maximum:
        maximum = num3
    elif num3 < minimum:
        minimum = num3

    return maximum, minimum


print(maximizer(4,13,9))
print(find_max_and_min(2,77,1)
