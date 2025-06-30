"""
BankDetails class for storing bank account and financial information.
"""
from typing import Dict, Any

class BankDetails:
    def __init__(self, bank_name: str = "", account_number: str = "", ifsc_code: str = "", branch: str = "", account_type: str = "", upi_id: str = "", pan_number: str = "", swift_code: str = "", micr_code: str = "", nominee: str = ""):
        self.bank_name = bank_name
        self.account_number = account_number
        self.ifsc_code = ifsc_code
        self.branch = branch
        self.account_type = account_type
        self.upi_id = upi_id
        self.pan_number = pan_number
        self.swift_code = swift_code
        self.micr_code = micr_code
        self.nominee = nominee

    def to_dict(self) -> Dict[str, Any]:
        return {
            "bank_name": self.bank_name,
            "account_number": self.account_number,
            "ifsc_code": self.ifsc_code,
            "branch": self.branch,
            "account_type": self.account_type,
            "upi_id": self.upi_id,
            "pan_number": self.pan_number,
            "swift_code": self.swift_code,
            "micr_code": self.micr_code,
            "nominee": self.nominee
        }
