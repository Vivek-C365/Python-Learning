
file_path = 'Assignment/Assign_3/test.py'

with open(file_path, 'r') as file:
    python_code = file.read()


all_flows = [flow_1, flow_2, flow_3]
urls = []
for all_flows in python_code:
    for flow in all_flows:
        urls.append(flow["api_data"]["url"])
print("All URLs: ", urls)


