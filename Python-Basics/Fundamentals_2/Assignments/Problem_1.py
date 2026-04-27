salary = int(input("Enter Your Salary"))

if(salary<30000):
    finalSalary = salary - (salary*0.05)
    print("Your Salary after tax Dedcuation is ",finalSalary)
elif(salary> 30000 | salary <= 70000):
    finalSalary = salary - (salary*0.15)
    print("Your Salary after tax Dedcuation is ",finalSalary)
else:
    finalSalary = salary - (salary*0.25)
    print("Your Salary after tax Dedcuation is ",finalSalary)
