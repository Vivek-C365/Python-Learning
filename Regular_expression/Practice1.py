import re
text = """

Contact us:
Phone: +1 515151222121
Email: inf12o@example.org
For customer support, please email support@example.com or call +1 5559876543.

Donec ac ex at arcu viverra luctus. Nulla facilisi. Fusce id risus in felis suscipit ultricies.

"""
ph_pt=r'[\b+]+\w+\s+\d{10}'
ph_numb = re.findall(ph_pt, text)
print("Ph_number:",  ph_numb)

em = r'[\w]+@[\w]+\.[\w]+'
em_print = re.findall(em,text)
print(em_print)
