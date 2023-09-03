import json

database_filename = "saved_numbers.json"

def save_contact(name:str,number:str):
    contacts = {}
    try:
        data = ""
        with open(database_filename,"r") as f:
            data = f.read()
        contacts = json.loads(data)
        contacts[name] = number
        with open(database_filename,'a') as f:
            f.write(json.dumps(contacts))
    except:
        data = {}
        data[name] = number
        with open(database_filename,'w') as f:
            f.write(json.dumps(data))

def list_contacts():
    try:
        with open(database_filename,'r') as f:
            contacts = json.loads(f.read())
            print("Saved numbers:")
            for a,b in contacts.items():
                print(f"{a} : {b}")
    except:
        print("No saved numbers or file corrupt.")
