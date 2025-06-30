# PersonalInfoSaver

A simple Python utility to save and retrieve personal information (name, age, email) to/from a local JSON file.

## 📁 File: `personal_info.json`
This file is automatically created in the same directory to store the data in JSON format.

## ✅ Features
- Save user information: name, age, and email
- Retrieve saved information by name
- Automatically loads and updates the data file

## 📦 Requirements
No external libraries required. Uses Python's built-in `json` and `os` modules.

## 🛠️ Usage

```bash
pip install personalinfo

```python
from personalinfo import PersonalInfoSaver

# Create the saver object
saver = PersonalInfoSaver()

# Save user information
saver.save_info("prabaharan", 30, "prabaharan@example.com")

# Retrieve user information
info = saver.get_info("prabaharan")
print(info)  # Output: {'age': 30, 'email': 'prabaharan@example.com'}

# Example usage
saver = PersonalInfoSaver()
saver.save_info("John Doe", 28, "s2EwX@example.com")
print(saver.get_info("John Doe"))  # This will print the saved information for "John Doe"

# You can also test with other names
saver.save_info("Jane Smith", 32, "nYDdD@example.com")
```
