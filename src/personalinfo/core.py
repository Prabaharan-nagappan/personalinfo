"""
PersonalInfoSaver main class for personal information management.
"""
import json
import os
from datetime import datetime, date
from typing import Optional, Dict, Any, List, Union
from .vehicle import VehicleDetails
from .education import EducationDetails
from .family import FamilyDetails
from .professional import ProfessionalDetails
from .bank import BankDetails
from .contact import ContactDetails

class PersonalInfoSaver:
    def __init__(self, filename: str = "personal_info.json"):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self) -> Dict[str, Any]:
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        return {}

    def calculate_age(self, dob: str) -> int:
        birth_date = datetime.strptime(dob, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def calculate_bmi(self, height_cm: float, weight_kg: float) -> float:
        height_m = height_cm / 100
        if height_m <= 0:
            return 0.0
        return round(weight_kg / (height_m ** 2), 2)

    def bmi_description(self, bmi: float) -> str:
        if bmi < 18.5:
            return "Underweight: Consider a nutritious diet."
        elif 18.5 <= bmi < 25:
            return "Normal weight: Keep up the good work!"
        elif 25 <= bmi < 30:
            return "Overweight: Consider regular exercise."
        else:
            return "Obese: Consult a healthcare provider."

    def save_info(
        self,
        name: str,
        dob: str,
        email: str,
        height_cm: float,
        weight_kg: float,
        bio: str = "",
        blood_group: str = "",
        family_details: dict = None,
        aadhar_number: str = "",
        address: str = "",
        vehicle_details: Optional[List[Union[VehicleDetails, dict]]] = None,
        education_details: Optional[List[Union[EducationDetails, dict]]] = None,
        professional_details: Optional[List[Union[ProfessionalDetails, dict]]] = None,
        bank_details: Optional[List[Union[BankDetails, dict]]] = None,
        contact_details: dict = None
    ):
        age = self.calculate_age(dob)
        bmi = self.calculate_bmi(height_cm, weight_kg)
        bmi_desc = self.bmi_description(bmi)
        if family_details is None:
            family_details = {}
        if vehicle_details is None:
            vehicle_details = []
        if contact_details is None:
            contact_details = {}
        data = {
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
            "address": address,
            "vehicle_details": [v.to_dict() if isinstance(v, VehicleDetails) else v for v in vehicle_details],
            "contact_details": contact_details
        }
        if education_details:
            def get_sort_year(e):
                if isinstance(e, EducationDetails):
                    return e.end_year or e.year_of_passing or 0
                return e.get("end_year") or e.get("year_of_passing") or 0
            sorted_edu = sorted(education_details, key=get_sort_year, reverse=True)
            data["education_details"] = [e.to_dict() if isinstance(e, EducationDetails) else e for e in sorted_edu]
        if professional_details:
            def get_sort_prof(e):
                if isinstance(e, ProfessionalDetails):
                    return e.end_date or e.start_date or ""
                return e.get("end_date") or e.get("start_date") or ""
            sorted_prof = sorted(professional_details, key=get_sort_prof, reverse=True)
            data["professional_details"] = [p.to_dict() if isinstance(p, ProfessionalDetails) else p for p in sorted_prof]
        if bank_details:
            data["bank_details"] = [b.to_dict() if isinstance(b, BankDetails) else b for b in bank_details]
        self.data[name] = data
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=4)

    def get_info(self, name: str) -> Optional[Dict[str, Any]]:
        return self.data.get(name, None)
