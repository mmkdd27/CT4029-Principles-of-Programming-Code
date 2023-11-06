human_age = int(input("Please enter the age in human years : "))
if human_age >= 2:
    dog_age = ((human_age - 2) * 4) + 21
    # if the age is above 2 I just remove the first two yeas ,calculate the rest of the age then add the two years as 21
else:
    dog_age = human_age * 10.5
    # if the age is below 2 I just calculate the age
print(dog_age)