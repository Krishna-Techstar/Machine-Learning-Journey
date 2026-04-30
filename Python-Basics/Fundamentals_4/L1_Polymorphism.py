class Employee:
    def get_desgination(self):
        print("Desgination = Empolyee")

class Teacher(Employee):
    def get_desgination(self):
        print("Desgination = Teacher")

l1 = Teacher()
l1.get_desgination()