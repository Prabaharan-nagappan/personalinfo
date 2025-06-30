"""
ContactDetails class for storing contact, native, and communication information.
"""
from typing import Dict, Any, List

class ContactDetails:
    def __init__(self, 
                 phone_numbers: List[str] = None,
                 email_addresses: List[str] = None,
                 emergency_contacts: List[str] = None,
                 native_place: str = "",
                 languages_known: List[str] = None,
                 communication_address: str = "",
                 permanent_address: str = "",
                 alternate_phone: str = "",
                 whatsapp_number: str = "",
                 telegram_id: str = "",
                 linkedin: str = "",
                 facebook: str = "",
                 twitter: str = "",
                 website: str = "",
                 guardian_name: str = "",
                 guardian_contact: str = ""):
        self.phone_numbers = phone_numbers if phone_numbers else []
        self.email_addresses = email_addresses if email_addresses else []
        self.emergency_contacts = emergency_contacts if emergency_contacts else []
        self.native_place = native_place
        self.languages_known = languages_known if languages_known else []
        self.communication_address = communication_address
        self.permanent_address = permanent_address
        self.alternate_phone = alternate_phone
        self.whatsapp_number = whatsapp_number
        self.telegram_id = telegram_id
        self.linkedin = linkedin
        self.facebook = facebook
        self.twitter = twitter
        self.website = website
        self.guardian_name = guardian_name
        self.guardian_contact = guardian_contact

    def to_dict(self) -> Dict[str, Any]:
        return {
            "phone_numbers": self.phone_numbers,
            "email_addresses": self.email_addresses,
            "emergency_contacts": self.emergency_contacts,
            "native_place": self.native_place,
            "languages_known": self.languages_known,
            "communication_address": self.communication_address,
            "permanent_address": self.permanent_address,
            "alternate_phone": self.alternate_phone,
            "whatsapp_number": self.whatsapp_number,
            "telegram_id": self.telegram_id,
            "linkedin": self.linkedin,
            "facebook": self.facebook,
            "twitter": self.twitter,
            "website": self.website,
            "guardian_name": self.guardian_name,
            "guardian_contact": self.guardian_contact
        }
