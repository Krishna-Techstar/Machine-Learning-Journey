username = input("Enter Your Username ")
password = input("Enter Your Password ")

if(username == "admin" and password == "pass"):
    print("Login Successfully!!")
elif(username != "admin"):
    print("Invalid username")
else:
    print("Invalid Password")