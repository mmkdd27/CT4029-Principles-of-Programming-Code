# function to check weather the number is prime or not
def prime_check(n):
    for factor in range(2, n):
        if n % factor == 0:
            return False
    return True


for number in range(1, 1000):
    # loop to go through every number form 1 to 1000
    if number < 500 or number > 600:
        # check to remove numbers that aren't between 500 and 600
        if prime_check(number):
            # we check if It's prime or not and print it, if it is
            print(number)
        if number == 23:
            # I assumed this is what you meant by stops at 23 ?
            break