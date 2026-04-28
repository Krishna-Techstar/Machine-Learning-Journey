info = [
    ("Krishnakant", "Maths"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Maths"),
    ("Bob", "Maths"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

unique_course =set()
for tup in info:
    unique_course.add(tup[1])
    print(tup[1])

    

print(unique_course)

for name,course in info:
    if(course== "English"):
        print(name,course)

dict= {}

for name,course in info:
    if(dict.get(name) == None):
        dict.update({name : set()})
        dict[name].add(course)
    else:
        dict[name].add(course)

print(dict)