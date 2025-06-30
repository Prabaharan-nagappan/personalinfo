# PersonalInfoSaver

A comprehensive Python utility to save and retrieve all personal, family, professional, vehicle, education, bank, and contact information to/from a local JSON file.

## 📁 File: `personal_info.json`
This file is automatically created in the same directory to store the data in JSON format.

## ✅ Features
- Save user information: name, date of birth (dob), email, height (cm), weight (kg), bio, blood group, aadhar number, address
- Auto-calculates age from dob
- Auto-calculates BMI from height and weight
- Provides a BMI health description
- Store detailed family information (father, mother, siblings, spouse, children)
- Store detailed vehicle information (type, make, model, year, registration, insurance, mileage, engine/chassis, etc.)
- Store detailed education information (schooling, college, degree, board, years, grades, specialization, location)
- Store professional/career information (designation, company, dates, skills, responsibilities, achievements, salary, employment type)
- Store bank details (bank name, account, IFSC, branch, account type, UPI, PAN, nominee, etc.)
- Store contact and communication details (phones, emails, native, languages, addresses, social, guardian, emergency contacts)
- Retrieve saved information by name
- Automatically loads and updates the data file

## 📦 Requirements
No external libraries required. Uses Python's built-in `json`, `os`, and `datetime` modules.

## 🛠️ Usage

```bash
pip install personalinfo
```

```python
from personalinfo import PersonalInfoSaver, FamilyDetails, VehicleDetails, EducationDetails, ProfessionalDetails, BankDetails, ContactDetails

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

# Create education details
schooling = EducationDetails(
    degree="SSLC",
    institution="ABC Matriculation School",
    year_of_passing=2011,
    grade="92%",
    board="State Board",
    school_name="ABC Matriculation School",
    start_year=2001,
    end_year=2011,
    location="Chennai"
)
ug = EducationDetails(
    degree="B.Tech",
    institution="IIT Madras",
    year_of_passing=2017,
    grade="8.9 CGPA",
    specialization="Computer Science",
    start_year=2013,
    end_year=2017,
    location="Chennai"
)

# Create professional details
prof = ProfessionalDetails(
    designation="Software Engineer",
    company="Google",
    start_date="2018-07-01",
    end_date="2022-12-31",
    location="Bangalore",
    skills=["Python", "ML"],
    responsibilities=["Developed ML models"],
    achievements=["Employee of the Year 2020"],
    salary=2500000.0,
    employment_type="Full-time",
    currently_working=False
)

# Create bank details
bank = BankDetails(
    bank_name="SBI",
    account_number="1234567890",
    ifsc_code="SBIN0001234",
    branch="Chennai Main",
    account_type="Savings",
    upi_id="peter@sbi",
    pan_number="ABCDE1234F",
    nominee="Lakshmi"
)

# Create contact details
contact = ContactDetails(
    phone_numbers=["+91-9876543210"],
    email_addresses=["peter@example.com"],
    native_place="Chennai",
    languages_known=["Tamil", "English"],
    communication_address="123 Main St, Chennai",
    whatsapp_number="+91-9876543210"
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
    "Peter", "1996-06-15", "peter@example.com", 180, 75,
    bio="Data scientist from India.",
    blood_group="B+",
    family_details=family.to_dict(),
    aadhar_number="1234-5678-9012",
    address="123 Main St, New York, NY",
    vehicle_details=[car, bike],
    education_details=[ug, schooling],
    professional_details=[prof],
    bank_details=[bank],
    contact_details=contact.to_dict()
)

# Retrieve user information
info = saver.get_info("Peter")
print(info)
# Output example:
# {
#   'dob': '1996-06-15',
#   'age': 29,
#   'email': 'peter@example.com',
#   'height_cm': 180,
#   'weight_kg': 75,
#   'bmi': 23.15,
#   'bmi_description': 'Normal weight: Keep up the good work!',
#   'bio': 'Data scientist from India.',
#   'blood_group': 'B+',
#   'family_details': { ... },
#   'aadhar_number': '1234-5678-9012',
#   'address': '123 Main St, New York, NY',
#   'vehicle_details': [ ... ],
#   'education_details': [ ... ],
#   'professional_details': [ ... ],
#   'bank_details': [ ... ],
#   'contact_details': { ... }
# }
```
