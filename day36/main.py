import requests

TOKEN = 'coderboy1189'
USERNAME = 'adityasunny1189'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# Create an account

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create a graph

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': 'graph1',
    'name': 'Problem Solving Graph',
    'unit': 'Questions',
    'type': 'int',
    'color': 'shibafu'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Posting a value on the graph

pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/graph1'

pixel_data = {
    'date': '20210411',
    'quantity': '2'
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)














