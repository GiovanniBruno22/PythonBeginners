import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        return False
    
    parts = email.split('@')
    username = parts[0]
    domain = parts[1]
    
    if len(username) > 64:
        return False
    
    if len(domain) > 255:
        return False
    
    domain_parts = domain.split('.')
    if any(len(part) > 63 for part in domain_parts):
        return False
    
    return True

# Example usage
email = input("Enter an email address: ")
if validate_email(email):
    print("Email address is valid.")
else:
    print("Email address is invalid.")