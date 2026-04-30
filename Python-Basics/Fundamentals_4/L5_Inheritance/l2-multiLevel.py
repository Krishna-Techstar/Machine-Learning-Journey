class Employee:
    Start_time = "10am"
    End_time = "9pm"

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role

class accountsDept(AdminStaff):
    def __init__(self, Name , EMPID, Salary, role):
        super().__init__(role)
        self.Name =Name
        self.EMPID = EMPID
        self.Salary = Salary
        self.role = role

a1 = AdminStaff("Accountant")
acc1 = accountsDept("Ram",101, 23500, "Accountant")

print(acc1.Name, acc1.EMPID, acc1.role, acc1.Salary, acc1.Start_time, acc1.End_time)