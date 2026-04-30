
class teacher:
    def __init__(self, name, salary, subject):
        self.name = name
        self.salary = salary
        self.subject = subject

class student:
    def __init__(self, studing_year, fees, CGPA):
        self.studing_year = studing_year
        self.fees = fees
        self.CGPA = CGPA

class TeacherAssistent(teacher, student):
    def __init__(self, name,salary,subject,studing_year , fees, CGPA):
        super().__init__( name, salary, subject)
        student.__init__(self, studing_year,fees, CGPA)
        self.name = name
        self.studing_year = studing_year
        self.fees = fees
        self.CGPA = CGPA
        self.name = name
        self.salary = salary
        self.subjet = subject


ta1 = TeacherAssistent("Krishnakant Sharma", 95000, "Maths", "2nd", 225750, 9.85)

print(f"{ta1.name} of CSE {ta1.studing_year} year is working as a Teacher Assistant in {ta1.subject} Subject pays {ta1.fees} and earns salary of {ta1.salary} and has current CGPA of {ta1.CGPA}")

