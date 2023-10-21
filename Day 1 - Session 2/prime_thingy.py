# function to check weather the number is prime or not
def prime_check(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for i in range(1, 1000):
    if i < 500 or i > 600:
        if prime_check(i):
            print(i)
        else:
            continue
        if i == 23:
            # I assumed this is what you meant by stops at 23 ?
            break
