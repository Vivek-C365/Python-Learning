import json

file_path = 'Assignment/Assign_3/test.txt'

with open(file_path) as f:
    python_code = f.read()
    
    
def urls(data):
    
    data = json.loads(data)
    print(type(data))

    for key in data:
        api_url = data[key]["api_data"]["url"]
        print("url of " + key + " - " + api_url)
    
    
def entity():
    
    flo = input(" enter Flow name")
    with open(file_path, 'r') as file:
        data = json.load(file)
    if flo in data:
        ent = input("Enter Entity")
        pro = input("Enter Prompt")
        
        dt = dict(entity = ent, prompt = pro )
        data[flo]['entities'].append(dt)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
        file.close()
    else:
        print("Flow name is not present in the file")
        

def update():
    flow = input("enter flow name")
    upt = json.loads(python_code)
    
    if flow in upt:
        new_url = input("Enter new URL: ")
        upt[flow]['api_data']['url'] = new_url
        with open (file_path,'w') as file:
            json.dump(upt, file , indent=2)
        print('This is updated URL:', upt[flow]['api_data']['url'])
        file.close()
    else:
        print(" this is key is not present in the data")

def update_all_urls():
    new_url = input("Enter the new URL: ")
    upt = json.loads(python_code)

    for key in upt:
        upt[key]['api_data']['url'] = new_url

    with open(file_path, 'w') as file:
        json.dump(upt, file, indent=2)

    print('All URLs have been updated to:', new_url)

def delete():
    data = json.loads(python_code)
    flow_name = input("enter flow name")
    if flow_name in data:
        entity_names = input("enter entity name")
        entities = data[flow_name].get('entities', [])
        for entity in entities.copy():
            if entity['entity'] in entity_names:
                entities.remove(entity)
                print(' entity get delted ')
    else:
        print("flow name is not found")  
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2) 


while True:
    print("Type 1 for fetch all urls")
    print("Type 2 for add Entity in Flow")
    print("Type 3 for update urls")
    print("Type 4 for delete entity from")
    print(" Type 0 for exit")
    ch = int(input('Type no to perform action'))
    
    if ch == 1:
        urls(python_code)
        f.close()
    elif ch == 2:
        entity()
    elif ch == 3:
        print("type 1 for update in specific flow")
        print("type 2 for update in all flow")
        choice = int(input("enter number perform update action"))
        if choice == 1:
            update()
        elif choice == 2:
            update_all_urls()
    elif ch == 4:
        delete()
    elif ch == 0:
        f.close()
        exit()