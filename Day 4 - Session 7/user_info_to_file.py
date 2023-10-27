def middle_name_check():
    while True:
        check = input("do you have a middle name ? [y]/[n] : ")
        check.lower()
        if check == "n" or check == "y":
            if check == "y":
                middle_name = input("what is it ? :  ")
                return middle_name
            elif check == "n":
                return None

        else:
            print("please enter a valid option")


def age_func():
    try:
        age = int(input("how old are you ?"))
        if age == 18:
            print("oh cool,we are the same age !")
        elif age > 18:
            print("""wow! :o 
    you are""", age - 18, "years older then me !")
        elif age < 18:
            print("""wow! :o 
    you are""", 18 - age, "years younger then me !")
        return age
    except ValueError:
        print("in number form !")
        age_func()



def gender_func():
    while True:
        check = input("do you wish to share your gender ? [y]/[n] : ")
        check.lower()
        if check == "n" or check == "y":
            if check == "y":
                middle_name = input("what do you identify as ? : ")
                return middle_name
            elif check == "n":
                print("okay dokey!")
                return None
            else:
                print("please enter a valid option")

def stro_finder():
    try:
        month = int(input("what month where you born ? (enter it as an number, for instance january as 1 : "))
        day = int(input("what day were you born ? : "))
        if month == 1 and day <= 19:
            return ("Capricorn")
        elif month == 1 and day > 19:
            return ("Aquarius️")
        elif month == 2 and day <= 18:
            return("Aquarius️")
        elif month == 2 and day > 18:
            return("Pisces️️")
        elif month == 3 and day <= 19:
            return("Pisces️")
        elif month == 4 and day > 20:
            return("Pisces️")
        elif month == 3 and day <= 20:
            return("Aries️")
        elif month == 4 and day <= 19:
            return("Aries️")
        elif month == 4 and day > 19:
            return("Taurus️")
        elif month == 5 and day <= 20:
            return("Taurus️")
        elif month == 5 and day > 20:
            return("Gemini️")
        elif month == 6 and day <= 20:
            return("Gemini️")
        elif month == 6 and day > 20:
            return("Cancer️")
        elif month == 7 and day <= 22:
            return("Cancer️")
        elif month == 7 and day > 22:
            return("Leo️")
        elif month == 8 and day <= 22:
            return("Leo️")
        elif month == 8 and day > 22:
            return("Virgo️")
        elif month == 9 and day <= 22:
            return("Virgo")
        elif month == 9 and day > 22:
            return("Libra️")
        elif month == 10 and day <= 22:
            return("Libra️")
        elif month == 10 and day > 22:
            return("Scorpio️")
        elif month == 11 and day <= 21:
            return("Scorpio")
        elif month == 11 and day > 21:
            return("Sagittarius️")
        elif month == 12 and day <= 21:
            return("Sagittarius️")
        elif month == 12 and day > 21:
            return("Capricorn")
    except ValueError:
     print("in number form !")



def sign_checker(sign):
    sign = sign.strip().lower()

    if sign == "aries":
        return True
    elif sign == "taurus":
        return True
    elif sign == "gemini":
        return True
    elif sign == "cancer":
        return True
    elif sign == "leo":
        return True
    elif sign == "virgo":
        return True
    elif sign == "libra":
        return True
    elif sign == "scorpio":
        return True
    elif sign == "sagittarius":
        return True
    elif sign == "capricorn":
        return True
    elif sign == "aquarius":
        return True
    elif sign == "pisces":
        return True
    else:
        return False

def sign_func():
    while True:
        check = input("do you know your astronomical sign ? [y]/[n] : ")
        check.lower()
        if check == "n" or check == "y":
            if check == "y":
                sign = input("what is it ? : ")
                return sign.lower()
            elif check == "n":
                sign = stro_finder().lower()
                return sign
            elif sign_checker(sign) is False:
                print("sorry i cant seem to recognize this sign")
            else:
                print("please enter a valid option")



def save_data():
    writer = open("user_data.txt", "w", encoding="utf-8")
    first_name = input("hello,whats your first name ? : ")
    last_name = input("whats your last name ? : ")
    middle_name = str(middle_name_check())
    age = str(age_func())
    gender = str(gender_func())
    sign = sign_func()
    user_data = [first_name,last_name,middle_name,age,gender,sign ]
    writer.writelines(user_data)

save_data()