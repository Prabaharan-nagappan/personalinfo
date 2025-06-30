from src.personalinfo import PersonalInfoSaver

# Create the saver object
saver = PersonalInfoSaver()

# Save user information (name, dob [YYYY-MM-DD], email, height in cm, weight in kg)
saver.save_info("prabaharan", "1996-06-15", "prabaharan@example.com", 170, 65)

# Retrieve user information
info = saver.get_info("prabaharan")
print(info)  # Output: {'dob': '1995-04-10', 'age': 30, 'email': 'prabaharan@example.com', 'height_cm': 170, 'weight_kg': 65, 'bmi': 22.49}

# Example usage
saver = PersonalInfoSaver()
saver.save_info("John Doe", "1997-05-12", "s2EwX@example.com", 180, 75)
print(saver.get_info("John Doe"))  # This will print the saved information for "John Doe"

# You can also test with other names
saver.save_info("Jane Smith", "1993-08-22", "nYDdD@example.com", 165, 60)