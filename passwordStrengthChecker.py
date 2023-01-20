import re

def check_password_strength(password):
    # Check the length of the password
    if len(password) < 8:
        return "Too short"
    
    # Check for at least one lowercase letter
    if not re.search("[a-z]", password):
        return "Too weak"
    
    # Check for at least one uppercase letter
    if not re.search("[A-Z]", password):
        return "Too weak"
    
    # Check for at least one digit
    if not re.search("[0-9]", password):
        return "Too weak"
    
    # Check for at least one special character
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return "Too weak"
    
    return "Strong"

# Test the function
password = input("Enter a password: ")
result = check_password_strength(password)
print(result)
