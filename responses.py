import json


with open('data/responses.json', 'r') as myfile:
    data = myfile.read()
responses = json.loads(data)
responses = responses['intents']
command = ""
print((responses[0]))
