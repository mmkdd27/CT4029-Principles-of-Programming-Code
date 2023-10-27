###########reader1 = open("employee_data1.txt", "r")
reader2 = open("employee_data2.txt", "r")
employee_data1 = reader1.readlines()
employee_data2 = reader2.readlines()
separator = ","
# do not set separator to "/" to avoid problems when it comes to date of birth
for i in employee_data1:
    full_name, contact_info, address, DoB, role1 = i.split(",")
    print(role1)
    for b in employee_data2:
        responsibility, role2 = b.split(",")
        print(role2)
