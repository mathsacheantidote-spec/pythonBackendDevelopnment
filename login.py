username = input("Enter username: ")
password = input("Enter password: ")

print("Your account is created successfully")
print("Login Now!")

us2 = input("Enter username: ")
p2 = input("Enter password: ")
if username == us2 and password == p2:
    print("Logged in Successfully!")
else:
    print("Invalid credentials")