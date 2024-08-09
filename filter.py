import os
import json

file_name = "webhook.json"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, file_name)

with open(file_path, "r") as file:
    data = json.load(file)


def filter_by_modular_design_code(data, code):
    data_json = {}

    for i in range(1, len(data["order"]["lines"])):
        if data["order"]["lines"][i]["customisation_details"]["design_code"] == code:
            data_json[i] = data["order"]["lines"][i]
    return data_json


def get_unique_design_codes(data):
    design_codes = set()

    for i in range(1, len(data["order"]["lines"])):
        design_codes.add(
            data["order"]["lines"][i]["customisation_details"]["design_code"]
        )
    return design_codes


design_codes = get_unique_design_codes(data)

for design_code in design_codes:
    output = filter_by_modular_design_code(data, design_code)
    with open(f"{design_code}.json", "w") as file:
        json.dump(output, file, indent=4)
