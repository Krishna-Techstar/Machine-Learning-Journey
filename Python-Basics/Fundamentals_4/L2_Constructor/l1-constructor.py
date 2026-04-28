class Student:
    def __init__(self): # deflaut constructor 
        print("Constructor was Called")

stu1 = Student()
print("this is form calling part")

# to define property 

class student:
    def __init__(self, name, cgpa): # parameterise constructor
        self.name = name  # self.name is to store value in memory
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa   

stut1 =student("Krishnakant", 9.85)
stut2 =student("Krishna", 8.95)
stut3 =student("Yash", 9.85)
stut4 =student("Nishit", 8.85)
stut5 =student("Raj", 7.85)

print(stut1.name, stut1.cgpa)
print(stut2.name, stut2.cgpa)
print(stut3.name, stut3.cgpa)
print(stut4.name, stut4.cgpa)
print(stut5.name, stut5.cgpa)

print(stut1.get_cgpa())
print(stut2.get_cgpa())