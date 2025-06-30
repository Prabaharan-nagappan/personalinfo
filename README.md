# PersonalInfoSaver

A simple Python utility to save and retrieve personal information (name, date of birth, age, email, height, weight, BMI) to/from a local JSON file.

## 📁 File: `personal_info.json`
This file is automatically created in the same directory to store the data in JSON format.

## ✅ Features
- Save user information: name, date of birth (dob), email, height (cm), weight (kg)
- Auto-calculates age from dob
- Auto-calculates BMI from height and weight
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

# Save user information (name, dob [YYYY-MM-DD], email, height in cm, weight in kg)
saver.save_info("prabaharan", "1996-06-15", "prabaharanpython@gmail.com", 170, 65)

# Retrieve user information
info = saver.get_info("prabaharan")
print(info)  # Output: {'dob': '1996-06-15', 'age': 29, 'email': 'prabaharanpython@gmail.com', 'height_cm': 170, 'weight_kg': 65, 'bmi': 22.49}

# Example usage
saver = PersonalInfoSaver()
saver.save_info("John Doe", "1997-05-12", "s2EwX@example.com", 180, 75)
print(saver.get_info("John Doe"))  # This will print the saved information for "John Doe"

# You can also test with other names
saver.save_info("Jane Smith", "1993-08-22", "nYDdD@example.com", 165, 60)
```
