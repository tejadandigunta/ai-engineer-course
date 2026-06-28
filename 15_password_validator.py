#Password should be at least 8 characters long
#password cannot contain space

password = input("Enter password: ")

if len(password) < 8:
    print("Password must contain at least 8 characters")
elif password.find(" ") != -1:
    print("Password cannot contain space")
else:
    print("Password is valid")