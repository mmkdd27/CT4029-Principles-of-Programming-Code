# Read employee personal information from file 1
file1 = open('employee_data1.txt', "r")
employee_info = file1.readlines()

file2 = open("employee_data2.txt", "r")
job_responsibilities = file2.readlines()

roles_responsibilities = {}
for line in job_responsibilities:
    role, responsibility = line.strip().split("#")
    roles_responsibilities[role] = responsibility

# Match roles and print combined information in a separate text file
output_file = open('combined_info.txt', 'w')
for line in employee_info:
    data = line.strip().split('&')
    first_name, last_name, contact_info, address, dob, role = data
    responsibility = roles_responsibilities.get(role, "Not specified")
    combined_info = f"Name: {first_name} {last_name}\nContact Info: {contact_info}\nAddress: {address}\nDOB: {dob}\nRole: {role}\nResponsibility: {responsibility}\n"
    output_file.write(combined_info)


file1.close()
file2.close()
