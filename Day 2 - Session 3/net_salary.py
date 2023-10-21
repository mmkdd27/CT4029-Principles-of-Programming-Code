gross_salary = int(input("Enter your Gross Salary: "))
if gross_salary > 150000:
    print("Your Net Salary After Deduction is:",gross_salary*0.54,)
    print("Your Tax Deduction is:",gross_salary*0.45)
elif 150000 >= gross_salary > 46350:
    print("Your Net Salary After Deduction is:",gross_salary*0.60)
    print("Your Tax Deduction is:",gross_salary*0.40)
elif 46350 >= gross_salary > 11850:
    print("Your Net Salary After Deduction is:",gross_salary * 0.80)
    print("Your Tax Deduction is:",gross_salary*0.20)
elif 11850 > gross_salary:
    print("Your Net Salary After Deduction is:",gross_salary)
    print("you are in the 0% tax bracket and there was no tax deducted" )
else:
    print("idk")
