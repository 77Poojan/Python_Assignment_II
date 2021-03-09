import json

data = {
    "name":"Naruto",
    "age": 19
}

with open("data_file.json","w") as write_file:
    json.dump(data,write_file)

json_data = json.dumps(data)
print(json_data) 