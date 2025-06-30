import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.personalinfo import PersonalInfoSaver, VehicleDetails, EducationDetails, FamilyDetails, ProfessionalDetails, ContactDetails

class TestPersonalInfoSaver(unittest.TestCase):
    def setUp(self):
        self.saver = PersonalInfoSaver(filename="test_personal_info.json")

    # def tearDown(self):
    #     import os
    #     if os.path.exists("test_personal_info.json"):
    #         os.remove("test_personal_info.json")

    def test_save_and_get_info(self):
        car = VehicleDetails(vehicle_type="Car", make="Toyota", model="Camry", year=2020)
        edu = EducationDetails(degree="B.Tech", institution="IIT Madras", year_of_passing=2017, grade="8.9 CGPA", specialization="CS", start_year=2013, end_year=2017)
        prof = ProfessionalDetails(
            designation="Software Engineer",
            company="Google",
            start_date="2018-07-01",
            end_date="2022-12-31",
            location="Bangalore",
            skills=["Python", "ML"],
            responsibilities=["Developed ML models"],
            achievements=["Employee of the Year 2020"],
            salary=2500000.0,
            employment_type="Full-time",
            currently_working=False
        )
        contact = ContactDetails(
            phone_numbers=["+91-9876543210"],
            email_addresses=["peter@example.com"],
            native_place="Chennai",
            languages_known=["Tamil", "English"],
            communication_address="123 Main St, Chennai",
            whatsapp_number="+91-9876543210"
        )
        family = FamilyDetails(father="Nagappan", mother="Lakshmi")
        self.saver.save_info(
            name="Peter",
            dob="1996-06-15",
            email="peter@example.com",
            height_cm=180,
            weight_kg=75,
            bio="Data scientist from India.",
            blood_group="B+",
            family_details=family.to_dict(),
            aadhar_number="1234-5678-9012",
            address="123 Main St, New York, NY",
            vehicle_details=[car],
            education_details=[edu],
            professional_details=[prof],
            contact_details=contact.to_dict()
        )
        info = self.saver.get_info("Peter")
        self.assertIsNotNone(info)
        self.assertEqual(info["email"], "peter@example.com")
        self.assertEqual(info["vehicle_details"][0]["make"], "Toyota")
        self.assertEqual(info["education_details"][0]["institution"], "IIT Madras")
        self.assertEqual(info["family_details"]["father"], "Nagappan")
        self.assertEqual(info["professional_details"][0]["company"], "Google")
        self.assertEqual(info["professional_details"][0]["designation"], "Software Engineer")
        self.assertIn("Python", info["professional_details"][0]["skills"])
        self.assertEqual(info["contact_details"]["native_place"], "Chennai")
        self.assertIn("+91-9876543210", info["contact_details"]["phone_numbers"])

if __name__ == "__main__":
    unittest.main()
