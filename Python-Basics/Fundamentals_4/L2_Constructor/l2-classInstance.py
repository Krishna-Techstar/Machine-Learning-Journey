class student:
    College_Name = "Bharati Vidyapeeth"

    def __init__(self, name, prn, cgpa):
        self.name = name 
        self.prn = prn
        self.cgpa = cgpa


stut1 =student("Krishnakant" ,1, 9.85)
stut2 =student("Krishna",2,  8.95)
stut3 =student("Yash",3, 9.85)

print(stut1.name)