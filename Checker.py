password = input("Enter password: ")
has_uppercase = False
has_number = False
While len(password) >= 8:
    for c in password:
        if c.isupper():
            has_uppercase = True
        elif c.isdigit():
            has_number = True
    if has_uppercase and has_number:
        print("Strong password!")
    elif has_uppercase or has_number:
        print("Moderate password!")
    else:
        print("Weak password!")
else:
    print("Password must be at least 8 characters long!")
