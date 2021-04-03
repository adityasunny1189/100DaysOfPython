import json

data = {
    "Amazon": {
        "email": "adityapathak1189@gmail.com",
        "password": "Adisunny1234"
    }
}

with open('data.json', 'w') as file:
    json.dump(data, file)