import xmltodict
import json

with open("src/metrics.xml") as file:
    data_dict = xmltodict.parse(file.read())

json_data = json.dumps(data_dict)

file_name = "1"
file_name += "data.json"

with open(file_name, "w") as json_file:
    json_file.write(json_data)

print(data_dict["v3d"])