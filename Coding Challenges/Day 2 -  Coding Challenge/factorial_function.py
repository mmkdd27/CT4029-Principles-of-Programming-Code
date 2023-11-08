number = int(input("enter a positive number "))


def factorial_finder(num):
    if num > 0:
        factorial = 1
        while num > 0:
            factorial = factorial * num
            num = num - 1
        print(factorial)
    else:
        print("please enter a positive integer ")


factorial_finder(number)
