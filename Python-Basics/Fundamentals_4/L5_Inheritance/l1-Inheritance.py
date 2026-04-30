class Employee:
    Start_time = "10am"
    End_time = "9pm"

    def changeTime(self, newTime):
        self.End_time = newTime

class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role

t1=Teacher("Maths")
A1 = AdminStaff("Clerk")
t1.changeTime("6pm")
print(t1.subject, t1.Start_time, t1.End_time)
print(A1.role, A1.Start_time, A1.End_time)