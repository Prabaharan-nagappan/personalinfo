## Welcome to the personal information Library
########################################
## by: Prabaharan

########################################
## classes
########################################

import json
import os
from datetime import datetime, date
from typing import Optional, Dict, Any

class PersonalInfoSaver:
    """
    A class to save and retrieve comprehensive personal information including name, date of birth, age (auto-calculated),
    email, height, weight, BMI (auto-calculated), BMI description, bio, blood group, family details, aadhar number, and address.
    """
    def __init__(self, filename: str = "personal_info.json"):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self) -> Dict[str, Any]:
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        return {}

    def calculate_age(self, dob: str) -> int:
        """Calculate age from date of birth (format: YYYY-MM-DD)."""
        birth_date = datetime.strptime(dob, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def calculate_bmi(self, height_cm: float, weight_kg: float) -> float:
        """Calculate BMI from height (cm) and weight (kg)."""
        height_m = height_cm / 100
        if height_m <= 0:
            return 0.0
        return round(weight_kg / (height_m ** 2), 2)

    def bmi_description(self, bmi: float) -> str:
        """Return a health description based on BMI value."""
        if bmi < 18.5:
            return "Underweight: Consider a nutritious diet."
        elif 18.5 <= bmi < 25:
            return "Normal weight: Keep up the good work!"
        elif 25 <= bmi < 30:
            return "Overweight: Consider regular exercise."
        else:
            return "Obese: Consult a healthcare provider."

    def save_info(self, name: str, dob: str, email: str, height_cm: float, weight_kg: float, bio: str = "", blood_group: str = "", family_details: dict = None, aadhar_number: str = "", address: str = ""):
        """
        Save comprehensive personal information including name, date of birth, email, height, weight, bio, blood group,
        family details (as a dict), aadhar number, and address. Age, BMI, and BMI description are auto-calculated and saved as well.

        :param name: Full name of the person
        :param dob: Date of birth in the format YYYY-MM-DD
        :param email: Email address
        :param height_cm: Height in centimeters
        :param weight_kg: Weight in kilograms
        :param bio: A short biography (optional)
        :param blood_group: Blood group (optional)
        :param family_details: Family details or description (optional)
        :param aadhar_number: Aadhar number (optional)
        :param address: Address (optional)
        """
        age = self.calculate_age(dob)
        bmi = self.calculate_bmi(height_cm, weight_kg)
        bmi_desc = self.bmi_description(bmi)
        if family_details is None:
            family_details = {}
        self.data[name] = {
            "dob": dob,
            "age": age,
            "email": email,
            "height_cm": height_cm,
            "weight_kg": weight_kg,
            "bmi": bmi,
            "bmi_description": bmi_desc,
            "bio": bio,
            "blood_group": blood_group,
            "family_details": family_details,
            "aadhar_number": aadhar_number,
            "address": address
        }
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=4)

    def get_info(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve personal information for a given name.

        :param name: Full name of the person
        :return: A dictionary containing the personal information, or None if not found
        """
        return self.data.get(name, None)

class FamilyDetails:
    """
    Used to store and retrieve detailed family member information, where each member can be a string (name) or a PersonalInfoSaver object.
    """
    def __init__(self, father=None, mother=None, siblings=None, spouse=None, children=None):
        self.father = father  # Can be a string or PersonalInfoSaver
        self.mother = mother  # Can be a string or PersonalInfoSaver
        self.siblings = siblings if siblings is not None else []  # List of strings or PersonalInfoSaver
        self.spouse = spouse  # Can be a string or PersonalInfoSaver
        self.children = children if children is not None else []  # List of strings or PersonalInfoSaver

    def to_dict(self):
        def member_to_dict(member):
            if isinstance(member, PersonalInfoSaver):
                return member.data
            return member
        return {
            "father": member_to_dict(self.father),
            "mother": member_to_dict(self.mother),
            "siblings": [member_to_dict(s) for s in self.siblings],
            "spouse": member_to_dict(self.spouse),
            "children": [member_to_dict(c) for c in self.children]
        }

if __name__ == "__main__":
    # Example usage
    mother = PersonalInfoSaver()
    mother.save_info(
        "Lakshmi", "1972-02-02", "lakshmi@example.com", 160, 60,
        bio="Homemaker.",
        blood_group="B+",
        aadhar_number="2222-3333-4444",
        address="456 Park Ave, New York, NY"
    )
    family = FamilyDetails(father="Nagappan", mother=mother)
    personal = PersonalInfoSaver()
    personal.save_info(
        "prabaharan", "1996-06-15", "prabaharan@example.com", 180, 75,
        bio="Data scientist from India.",
        blood_group="B+",
        family_details=family.to_dict(),
        aadhar_number="1234-5678-9012",
        address="123 Main St, New York, NY"
    )
    print(personal.get_info("prabaharan"))


