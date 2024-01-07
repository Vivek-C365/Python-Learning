import re

text = """
Contact us:
Phone: +1 515151222121
Email: inf12o@example.org
For customer support, please email support@example.com or call +1 5559876543.
2124567890
212-456-7890
(212)456-7890
(212)-456-7890
212.456.7890
212 456 7890
+12124567890
+12124567890
+1 212.456.7890
+212-456-7890
1-212-456-7890
191-212-456-7890
456-7890
+14151231234
020 1234 1234

Donec ac ex at arcu viverra luctus. Nulla facilisi. Fusce id risus in felis suscipit ultricies.
"""

# Simplified phone number regex
ph_pt = r'\+?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,12}'

ph_numb = re.findall(ph_pt, text)
print("Ph_number:", ph_numb)

em = r'\b[\w]+@[\w]+\.[a-zA-Z]{2,}\b'
em_print = re.findall(em, text)
print(em_print)
