import requests

url_endpoint = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin'

pin_code = '846004'
date = '03-05-2021'

params = {
    'pincode': pin_code,
    'date': date
}

response = requests.get(url_endpoint, params)
data = response.json()['centers']

print(data)
