import json
def create_json():
    data = [{
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }]
    return data


with open("createJson.json", "w") as f:
    json.dump(create_json(), f, indent=4)