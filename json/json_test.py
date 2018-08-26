# Looks like a Python dictionary
import json

people_string = '''
{
    "people": [
     {
         "name": "John Smith",
         "phone": "615-555-7165",
         "emails": ['johnsmith@bogusemail.com', 'john_smith@work.com'],
         "has_license": false
    },
    {
        "name": "Jane Doe",
        "phone": "565-342-2313",
        "emails": null,
        "has_license": true
        }
    ]
}
'''

data = json.loads(people_string)

for person in data['people']:
    del person['phone']
