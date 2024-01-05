import re
text = """

Contact us:
Phone: +1 1234567891
Email: inf12o@example.org
For customer support, please email support@example.com or call +1 5559876543.

Donec ac ex at arcu viverra luctus. Nulla facilisi. Fusce id risus in felis suscipit ultricies.

"""
ph_pt=r'\d{10}'
# ph_pt1 = '\A+1'
# ph_ch = re.findall("ph_pt1",text)
ph_numb = re.findall(ph_pt, text)
print("Ph_number:",  ph_numb)

em = r'[\w]+@[\w]+\.[\w]+'
em_print = re.findall(em,text)
print(em_print)
