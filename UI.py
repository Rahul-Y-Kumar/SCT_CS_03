print("\n" + "="*50)
print("** Welcome to the 🔐 Password Strength Checker! **")
print("="*50 + "\n")
print("Please enter a password to check its strength.")
password_info = input("📝 Enter Password: ")
result = check_password_strength(password_info)
print("\n" + "-"*50)
for key, value in result.items():
    if isinstance(value, dict):
        print(f"{key}:")
        for sub_key, sub_value in value.items():
            print(f"  {sub_key}: {'✅' if sub_value else '❌'}")
    else:
        print(f"{key}: {value}")
print("-"*50)


return {
        "🔹 Password Entered": password,
        "🔹 Strength": strength,
        "🔹 Criteria": {
            "✔ Length (8+ characters)": length_criteria,
            "✔ Uppercase Letter": uppercase_criteria,
            "✔ Lowercase Letter": lowercase_criteria,
            "✔ Number": number_criteria,
            "✔ Special Character": special_char_criteria
        }
    }
