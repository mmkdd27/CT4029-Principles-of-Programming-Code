reader = open("employee_data.txt", "r")
separator = ","
employee_data = reader.readlines()
for i in employee_data:
    name, address, salary = i.split(",")
    try:
        salary = int(salary)
        if salary > 5000:
            new_salary = salary * 1.015
            first_name, last_name = name.split()
            print(first_name, "Received a 1.5% bonus")
            print("Previous salary: ", salary)
            print("New salary: ", new_salary)
            print("Bonus: ", salary * 0.015)
    except ValueError:
        print("there seems to be a mistake in the file on line", i, "!")
