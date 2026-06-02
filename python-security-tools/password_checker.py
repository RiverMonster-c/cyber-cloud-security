import re

def verify_password(password):
    if len(password) < 8:
        return "❌ WEAK: Password must be at least 8 characters long."
    
    if not re.search("[0-9]", password):
        return "❌ WEAK: Password needs at least one number."
    
    if not re.search("[_@$!%*#?&]", password):
        return "❌ WEAK: Password needs at least one special character."
    
    return "🔒 STRONG: Password meets basic cybersecurity standards."

user_input = input("Enter a password to test its strength: ")
result = verify_password(user_input)
print(result)