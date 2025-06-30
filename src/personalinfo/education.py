"""
EducationDetails class for storing education information.
"""
from typing import Dict, Any

class EducationDetails:
    def __init__(self, degree: str = "", institution: str = "", year_of_passing: int = None, grade: str = "", specialization: str = "", board: str = "", school_name: str = "", start_year: int = None, end_year: int = None, location: str = ""):
        self.degree = degree
        self.institution = institution
        self.year_of_passing = year_of_passing
        self.grade = grade
        self.specialization = specialization
        self.board = board
        self.school_name = school_name
        self.start_year = start_year
        self.end_year = end_year
        self.location = location

    def to_dict(self) -> Dict[str, Any]:
        return {
            "degree": self.degree,
            "institution": self.institution,
            "year_of_passing": self.year_of_passing,
            "grade": self.grade,
            "specialization": self.specialization,
            "board": self.board,
            "school_name": self.school_name,
            "start_year": self.start_year,
            "end_year": self.end_year,
            "location": self.location
        }
