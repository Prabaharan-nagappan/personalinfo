from src.personalinfo import PersonalInfoSaver

# Create the saver object
saver = PersonalInfoSaver()

# Save user information with all fields
saver.save_info(
    "prabaharan", "1996-06-15", "prabaharan@example.com", 170, 65,
    bio="Python developer from India.",
    blood_group="O+",
    family_details="Father: S. Kumar, Mother: L. Devi, Brother: R. Prakash",
    aadhar_number="1234-5678-9012",
    address="123 Main St, Chennai, India"
)

# Retrieve user information
info = saver.get_info("prabaharan")
print(info)

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
print(saver.get_info("Jane Smith"))