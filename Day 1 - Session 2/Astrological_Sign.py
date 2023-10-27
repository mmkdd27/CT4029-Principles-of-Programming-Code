# here I ask for the month and then the day to check each one in as separate if statement
# a better solution could have been possible using more complex functions

# **********************************************************************************************
# here is a guide I found:
# Aries ♈️: March 21 - April 19
# Taurus ♉️: April 20 - May 20
# Gemini ♊️: May 21 - June 20
# Cancer ♋️: June 21 - July 22
# Leo ♌️: July 23 - August 22
# Virgo ♍️: August 23 - September 22
# Libra ♎️: September 23 - October 22
# Scorpio ♏️: October 23 - November 21
# Sagittarius ♐️: November 22 - December 21
# Capricorn ♑️: December 22 - January 19
# Aquarius ♒️: January 20 - February 18
# Pisces ♓️: February 19 - March 20
# *************************************************************************************************
month = int(input("what month where you born ? (enter it as an number, for instance january as 1 : "))
day = int(input("what day were you born ? : "))
if month == 1 and day <= 19:
    print("Capricorn ♑️")
elif month == 1 and day > 19:
    print("Aquarius ♒️")
elif month == 2 and day <= 18:
    print("Aquarius ♒️")
elif month == 2 and day > 18:
    print("Pisces ♓️️")
elif month == 3 and day <= 19:
    print("Pisces ♓️")
elif month == 4 and day > 20:
    print("Pisces ♓️")
elif month == 3 and day <= 20:
    print("Aries ♈️")
elif month == 4 and day <= 19:
    print("Aries ♈️")
elif month == 4 and day > 19:
    print("Taurus ♉️")
elif month == 5 and day <= 20:
    print("Taurus ♉️")
elif month == 5 and day > 20:
    print("Gemini ♊️")
elif month == 6 and day <= 20:
    print("Gemini ♊️")
elif month == 6 and day > 20:
    print("Cancer ♋️")
elif month == 7 and day <= 22:
    print("Cancer ♋️")
elif month == 7 and day > 22:
    print("Leo ♌️")
elif month == 8 and day <= 22:
    print("Leo ♌️")
elif month == 8 and day > 22:
    print("Virgo ♍️")
elif month == 9 and day <= 22:
    print("Virgo ♍️")
elif month == 9 and day > 22:
    print("Libra ♎️")
elif month == 10 and day <= 22:
    print("Libra ♎️")
elif month == 10 and day > 22:
    print("Scorpio ♏️")
elif month == 11 and day <= 21:
    print("Scorpio ♏️")
elif month == 11 and day > 21:
    print("Sagittarius ♐️")
elif month == 12 and day <= 21:
    print("Sagittarius ♐️")
elif month == 12 and day > 21:
    print("Capricorn ♑️")
else:
    print("idk")
