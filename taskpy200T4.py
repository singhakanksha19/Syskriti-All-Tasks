# Password Strength Checker
#Author: Akanksha Singh

# Input password
password = input("Enter password: ")

# Initialize conditions
has_upper = False
has_lower = False
has_digit = False

# Check each character
for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True

# Check all conditions
if len(password) >= 8 and has_upper and has_lower and has_digit:
    print("STRONG")
else:
    print("WEAK")