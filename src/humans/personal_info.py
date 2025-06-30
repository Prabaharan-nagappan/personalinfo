import json
import os

class PersonalInfoSaver:
    def __init__(self, filename="personal_info.json"):
        self.filename = filename
        self.data = self._load_data()

    def _load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        return {}

    def save_info(self, name, age, email):
        self.data[name] = {"age": age, "email": email}
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=4)

    def get_info(self, name):
        return self.data.get(name)

# Example usage:
saver = PersonalInfoSaver()
saver.save_info("Alice", 30, "alice@example.com")
print(saver.get_info("Alice"))
