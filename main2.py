import json
with open("if/data/user.json", "r") as file:
    data = json.load(file)
    data.append({
        "name": "petar petrovic",
        "age" : 35,
        "height" : 190,
        "gender" : "male"

    })
    print(data)

with open("if/data/user.json", "w") as file:
    json.dump(data, file, indent=4)