import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r"[A-Z]", password))
    lowercase_criteria = bool(re.search(r"[a-z]", password))
    number_criteria = bool(re.search(r"[0-9]", password))
    special_char_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    
    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    
    if strength_score == 5:
        strength = "🔒 Very Strong"
    elif strength_score == 4:
        strength = "🛡️ Strong"
    elif strength_score == 3:
        strength = "⚠️ Moderate"
    elif strength_score == 2:
        strength = "❗ Weak"
    else:
        strength = "🚨 Very Weak"
