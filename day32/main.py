import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
response_data = response.json()
latitude = response_data['iss_position']['latitude']
longitude = response_data['iss_position']['longitude']
print(latitude)
print(longitude)
