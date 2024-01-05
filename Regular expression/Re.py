import re
text = """Contact us at support@example.com or sales@example.com
You can reach us at +1234567890 or +1-987-654-3210
9877108932
"""
phone_pattern=r'\d{10}'
phone_numbers = re.findall(phone_pattern, text)
print("Phone Numbers:", phone_numbers)
