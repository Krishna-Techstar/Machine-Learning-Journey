info ={
    "Name": "Krishna",
    "CGPA": 9.85,   
    2:"alpha",
    "Subject": ["COA", "CGM", "TOC", "CN", "SPOs"]
}
# key  
dict_keys = info.keys()
print(dict_keys)
#values
dict_val = info.values()
print(dict_val)


print(info["CGPA"])
#print(info["CGPA2"])
print(info.get("CGPA2"))

print("end of code ceo in making")

info.update({
    "City":"Mumbai"
})
print(info)