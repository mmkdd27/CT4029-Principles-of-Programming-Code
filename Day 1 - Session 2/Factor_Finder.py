number = int(input("enter your number here and press enter : "))
# receives input

for i in range(1, number + 1):
    # we check every number from 1 to the number itself
    if number % i == 0:
        # swe check if the number is divisible by our number and out put it if it is
        print(i)