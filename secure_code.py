import hashlib

stored_user = "admin"
stored_password_hash = hashlib.sha256("admin123".encode()).hexdigest()

username = input("Enter Username: ")
password = input("Enter Password: ")

password_hash = hashlib.sha256(password.encode()).hexdigest()

if username == stored_user and password_hash == stored_password_hash:
    print("Login Successful")
else:
    print("Login Failed")