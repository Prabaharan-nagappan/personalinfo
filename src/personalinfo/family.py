"""
FamilyDetails class for storing family member information.
"""
from typing import Dict, Any

class FamilyDetails:
    def __init__(self, father=None, mother=None, siblings=None, spouse=None, children=None):
        self.father = father
        self.mother = mother
        self.siblings = siblings if siblings is not None else []
        self.spouse = spouse
        self.children = children if children is not None else []

    def to_dict(self) -> Dict[str, Any]:
        def member_to_dict(member):
            # Avoid circular import by not importing PersonalInfoSaver here
            if hasattr(member, 'data'):
                return member.data
            return member
        return {
            "father": member_to_dict(self.father),
            "mother": member_to_dict(self.mother),
            "siblings": [member_to_dict(s) for s in self.siblings],
            "spouse": member_to_dict(self.spouse),
            "children": [member_to_dict(c) for c in self.children]
        }
