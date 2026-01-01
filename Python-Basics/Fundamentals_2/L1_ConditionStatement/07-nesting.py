#username and passwords
username = input("Enter the username ")
password = input("Enter the password ")

if (username == "admin" and password == "Pass123"):
    print("Login Successful")
else:
    if username != "admin":
        print("Invalid Username ")
    else:
        print("Invaild Password")
