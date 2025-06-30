# PersonalInfoSaver

A simple Python utility to save and retrieve comprehensive personal information (name, date of birth, age, email, height, weight, BMI, BMI description, bio, blood group, family details, aadhar number, address, vehicle details) to/from a local JSON file.

## 📁 File: `personal_info.json`
This file is automatically created in the same directory to store the data in JSON format.

## ✅ Features
- Save user information: name, date of birth (dob), email, height (cm), weight (kg), bio, blood group, family details, aadhar number, address, vehicle details
- Auto-calculates age from dob
- Auto-calculates BMI from height and weight
- Provides a BMI health description
- Store detailed family and vehicle information (including type, insurance, mileage, etc.)
- Retrieve saved information by name
- Automatically loads and updates the data file

## 📦 Requirements
No external libraries required. Uses Python's built-in `json`, `os`, and `datetime` modules.

## 🛠️ Usage

```bash
pip install personalinfo
```

```python
from personalinfo import PersonalInfoSaver, FamilyDetails, VehicleDetails

# Create vehicle details
car = VehicleDetails(
    vehicle_type="Car",
    make="Toyota",
    model="Camry",
    year=2020,
    registration_number="TN01AB1234",
    color="White",
    insurance_number="INS123456789",
    insurance_expiry="2026-05-31",
    mileage=15000.5,
    engine_number="ENG987654321",
    chassis_number="CHS123456789"
)
bike = VehicleDetails(
    vehicle_type="Bike",
    make="Honda",
    model="CBR",
    year=2018,
    registration_number="TN01XY5678",
    color="Red",
    insurance_number="INS987654321",
    insurance_expiry="2025-12-31",
    mileage=22000.0,
    engine_number="ENG123456789",
    chassis_number="CHS987654321"
)

# Create family details (father as string, mother as PersonalInfoSaver)
mother = PersonalInfoSaver()
mother.save_info(
    "Lakshmi", "1972-02-02", "lakshmi@example.com", 160, 60,
    bio="Homemaker.",
    blood_group="B+",
    aadhar_number="2222-3333-4444",
    address="456 Park Ave, New York, NY",
    vehicle_details=[car]
)
family = FamilyDetails(father="Nagappan", mother=mother)

# Create the saver object and save user information
saver = PersonalInfoSaver()
saver.save_info(
    "prabaharan", "1996-06-15", "prabaharanpython@gmail.com", 170, 65,
    bio="Python developer from India.",
    blood_group="O+",
    family_details=family.to_dict(),
    aadhar_number="1234-5678-9012",
    address="123 Main St, Chennai, India",
    vehicle_details=[car, bike]
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
#   'family_details': { ... },
#   'aadhar_number': '1234-5678-9012',
#   'address': '123 Main St, Chennai, India',
#   'vehicle_details': [ ... ]
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
