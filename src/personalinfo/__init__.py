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
    A class to save and retrieve personal information including name, date of birth, age (auto-calculated),
    email, height, weight, and BMI (auto-calculated) to/from a local JSON file.
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

    def save_info(self, name: str, dob: str, email: str, height_cm: float, weight_kg: float):
        age = self.calculate_age(dob)
        bmi = self.calculate_bmi(height_cm, weight_kg)
        self.data[name] = {
            "dob": dob,
            "age": age,
            "email": email,
            "height_cm": height_cm,
            "weight_kg": weight_kg,
            "bmi": bmi
        }
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=4)

    def get_info(self, name: str) -> Optional[Dict[str, Any]]:
        return self.data.get(name, None)

# Example usage:
# saver = PersonalInfoSaver()
# saver.save_info("John Doe", "1997-05-12", "john@example.com", 175, 70)
# print(saver.get_info("John Doe"))


