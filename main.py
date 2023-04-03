import re

def check_password_strength(password):
    strength=0

    if len(password)<8:
        print("weak password")

    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]',password):
        print("password is modrate")
        strength=1
    else:
        strength=2

        return strength
while True:
    password = input("Enter Password: ")
    strength = check_password_strength(password)

    if strength == 2:
        print("Password is strong")
        break
    print("Try Again!")