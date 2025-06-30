"""
VehicleDetails class for storing vehicle information.
"""
from typing import Dict, Any

class VehicleDetails:
    def __init__(self, vehicle_type: str = "", make: str = "", model: str = "", year: int = None, registration_number: str = "", color: str = "", insurance_number: str = "", insurance_expiry: str = "", mileage: float = None, engine_number: str = "", chassis_number: str = ""):
        self.vehicle_type = vehicle_type
        self.make = make
        self.model = model
        self.year = year
        self.registration_number = registration_number
        self.color = color
        self.insurance_number = insurance_number
        self.insurance_expiry = insurance_expiry
        self.mileage = mileage
        self.engine_number = engine_number
        self.chassis_number = chassis_number

    def to_dict(self) -> Dict[str, Any]:
        return {
            "vehicle_type": self.vehicle_type,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "registration_number": self.registration_number,
            "color": self.color,
            "insurance_number": self.insurance_number,
            "insurance_expiry": self.insurance_expiry,
            "mileage": self.mileage,
            "engine_number": self.engine_number,
            "chassis_number": self.chassis_number
        }
