human_age = int(input("please enter the age in human years : "))
if human_age >= 2:
    dog_age = ((human_age - 2) * 4) + 21
else:
    dog_age = human_age * 10.5
print(dog_age)
