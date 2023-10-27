reader = open("employee_dats.txt", "r")
separator = ","
employee_data = reader.readlines()
for i in employee_data:
    name, address, salary = i.split(",")
    try:
        salary = int(salary)
        if salary > 5000:
            new_salary = salary * 1.015
            first_name, last_name = name.split()
            print(first_name, "recived a 1.5% bounes")
            print("pervouis slary: ", salary)
            print("new slary: ", new_salary)
            print("bounes: ",salary*0.015)
    except ValueError:
        print("there seems to be a mistake in the file on line", i, "!")