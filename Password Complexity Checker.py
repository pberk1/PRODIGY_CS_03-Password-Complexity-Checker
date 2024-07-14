import re
def password_complexity_checker (password):
    length_rule= len (password) > 10
    lowercase_rule= bool(re.search (r'[a-z]', password))
    uppercase_rule= bool(re.search (r'[A-Z]', password))
    special_char_rule= bool(re.search(r'[!@#$%^&*(),.:"{}<>?~+=`;]', password))
    number_rule= bool(re.search (r'[0-9]', password))
    total_rule= number_rule + special_char_rule + uppercase_rule + lowercase_rule + length_rule
    if total_rule == 5:
        return "Strong Password"
    elif total_rule >= 3:
        return "Ok Password"
    else: 
        return "Weak Password"
password= input("Enter your password:")
strength= password_complexity_checker(password)
print(f" password strenth: {strength}")