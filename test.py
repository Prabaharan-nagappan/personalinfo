from src.personalinfo import PersonalInfoSaver, FamilyDetails, VehicleDetails

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

# Create the saver object
saver = PersonalInfoSaver()

# Save user information with all fields and structured family and vehicle details
Peter_family = FamilyDetails(
    father="S. Kumar",
    mother="L. Devi",
    siblings=["R. Prakash"]
)
saver.save_info(
    "Peter", "1996-06-15", "Peter@example.com", 170, 65,
    bio="Python developer from India.",
    blood_group="O+",
    family_details=Peter_family.to_dict(),
    aadhar_number="1234-5678-9012",
    address="123 Main St, Chennai, India",
    vehicle_details=[car, bike]
)

# Retrieve user information
info = saver.get_info("Peter")
print(info)

# Example usage for another person
john_family = FamilyDetails(
    father="Mark Doe",
    mother="Jane Doe",
    siblings=["Anna Doe"]
)
saver.save_info(
    "John Doe", "1997-05-12", "s2EwX@example.com", 180, 75,
    bio="Software engineer from NY.",
    blood_group="A+",
    family_details=john_family.to_dict(),
    aadhar_number="9876-5432-1098",
    address="456 Park Ave, New York, NY",
    vehicle_details=[car]
)
print(saver.get_info("John Doe"))

# You can also test with other names
jane_family = FamilyDetails(
    father="Tom Smith",
    mother="Lisa Smith"
)
saver.save_info(
    "Jane Smith", "1993-08-22", "nYDdD@example.com", 165, 60,
    bio="Graphic designer.",
    blood_group="B+",
    family_details=jane_family.to_dict(),
    aadhar_number="1111-2222-3333",
    address="789 Elm St, Los Angeles, CA",
    vehicle_details=[bike]
)
print(saver.get_info("Jane Smith"))