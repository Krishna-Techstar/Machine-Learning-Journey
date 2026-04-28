set = {1, 2, 3, 2, 4, 5,3, 3}
set2 = { 1, 2, 3, 4,5}
# add 
set.add(5)
print(set)

# remove 
set.remove(2)
print(set)

# pop 
set.pop()
print(set)

# union 
set.union(set2)
print(set)

# intersection
set.intersection(set2)
print(f"This is intersection set1{set}")
print(f"this is intersection{set2}")

#Clear
set.clear()
print(set)