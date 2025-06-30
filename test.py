from personalinfo import PersonalInfoSaver
# Example usage
saver = PersonalInfoSaver()
saver.save_info("John Doe", 28, "s2EwX@example.com")
print(saver.get_info("John Doe"))
# This will print the saved information for "John Doe"
# You can also test with other names
saver.save_info("Jane Smith", 32, "nYDdD@example.com")
