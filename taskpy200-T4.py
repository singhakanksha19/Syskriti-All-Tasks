# Task_PY200_T4: Password Strength Checker

def check_password_strength(s):
    issues = []

    # Rule 1: length >= 8
    if len(s) < 8:
        issues.append("Password must be at least 8 characters long.")
    
    # Rule 2: has at least 1 digit
    if not any(ch.isdigit() for ch in s):
        issues.append("Password must contain at least one digit.")
    
    # Rule 3: has at least 1 uppercase
    if not any(ch.isupper() for ch in s):
        issues.append("Password must contain at least one uppercase letter.")
    
    # Rule 4: has at least 1 lowercase
    if not any(ch.islower() for ch in s):
        issues.append("Password must contain at least one lowercase letter.")
    
    if issues:
        print("WEAK")
        print("Issues found:")
        for issue in issues:
            print("-", issue)
    else:
        print("STRONG")

# Example usage:
password = input("Enter password: ")
check_password_strength(password)