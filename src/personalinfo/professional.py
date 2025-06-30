"""
ProfessionalDetails class for storing professional/career information.
"""
from typing import Dict, Any

class ProfessionalDetails:
    def __init__(self, designation: str = "", company: str = "", start_date: str = "", end_date: str = "", location: str = "", skills: list = None, responsibilities: list = None, achievements: list = None, salary: float = None, employment_type: str = "", currently_working: bool = False):
        self.designation = designation
        self.company = company
        self.start_date = start_date  # format: YYYY-MM-DD
        self.end_date = end_date      # format: YYYY-MM-DD or "Present"
        self.location = location
        self.skills = skills if skills is not None else []
        self.responsibilities = responsibilities if responsibilities is not None else []
        self.achievements = achievements if achievements is not None else []
        self.salary = salary
        self.employment_type = employment_type  # e.g., 'Full-time', 'Part-time', 'Internship', etc.
        self.currently_working = currently_working

    def to_dict(self) -> Dict[str, Any]:
        return {
            "designation": self.designation,
            "company": self.company,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "location": self.location,
            "skills": self.skills,
            "responsibilities": self.responsibilities,
            "achievements": self.achievements,
            "salary": self.salary,
            "employment_type": self.employment_type,
            "currently_working": self.currently_working
        }
