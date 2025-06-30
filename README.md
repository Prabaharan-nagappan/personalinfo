# PersonalInfoSaver

A simple Python utility to save and retrieve comprehensive personal information (name, date of birth, age, email, height, weight, BMI, BMI description, bio, blood group, family details, aadhar number, address) to/from a local JSON file.

## 📁 File: `personal_info.json`
This file is automatically created in the same directory to store the data in JSON format.

## ✅ Features
- Save user information: name, date of birth (dob), email, height (cm), weight (kg), bio, blood group, family details, aadhar number, address
- Auto-calculates age from dob
- Auto-calculates BMI from height and weight
- Provides a BMI health description
- Retrieve saved information by name
- Automatically loads and updates the data file

## 📦 Requirements
No external libraries required. Uses Python's built-in `json`, `os`, and `datetime` modules.

## 🛠️ Usage

```bash
pip install personalinfo
```

```python
from personalinfo import PersonalInfoSaver

# Create the saver object
saver = PersonalInfoSaver()

# Save user information (all fields are optional except name, dob, email, height, weight)
saver.save_info(
    "prabaharan", "1996-06-15", "prabaharanpython@gmail.com", 170, 65,
    bio="Python developer from India.",
    blood_group="O+",
    family_details="Father: S. Kumar, Mother: L. Devi, Brother: R. Prakash",
    aadhar_number="1234-5678-9012",
    address="123 Main St, Chennai, India"
)

# Retrieve user information
info = saver.get_info("prabaharan")
print(info)
# Output example:
# {
#   'dob': '1996-06-15',
#   'age': 29,
#   'email': 'prabaharanpython@gmail.com',
#   'height_cm': 170,
#   'weight_kg': 65,
#   'bmi': 22.49,
#   'bmi_description': 'Normal weight: Keep up the good work!',
#   'bio': 'Python developer from India.',
#   'blood_group': 'O+',
#   'family_details': 'Father: S. Kumar, Mother: L. Devi, Brother: R. Prakash',
#   'aadhar_number': '1234-5678-9012',
#   'address': '123 Main St, Chennai, India'
# }

# Example usage for another person
saver.save_info(
    "John Doe", "1997-05-12", "s2EwX@example.com", 180, 75,
    bio="Software engineer from NY.",
    blood_group="A+",
    family_details="Father: Mark Doe, Mother: Jane Doe, Sister: Anna Doe",
    aadhar_number="9876-5432-1098",
    address="456 Park Ave, New York, NY"
)
print(saver.get_info("John Doe"))

# You can also test with other names
saver.save_info(
    "Jane Smith", "1993-08-22", "nYDdD@example.com", 165, 60,
    bio="Graphic designer.",
    blood_group="B+",
    family_details="Father: Tom Smith, Mother: Lisa Smith",
    aadhar_number="1111-2222-3333",
    address="789 Elm St, Los Angeles, CA"
)
```
