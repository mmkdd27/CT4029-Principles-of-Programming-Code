def reverser(s):
    str = ""#I create a new empty string
    for i in s: #i add every letter of the original string to the new one but from the left
        str = i + str
    return str


sring = input("enter your string: ")
print(reverser(sring))


num1, num2, num3 = (input("enter your values sepertaed by a ','").split(","))
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
    maximum = num1#I assume num1 one to be minimum and maximum then I challenge it with comparing with other values
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
