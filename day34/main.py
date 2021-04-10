import requests
import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# export TWILIO_ACCOUNT_SID='ACb07a2c09fe04be9f5e1756a3827432a9'
# export TWILIO_AUTH_TOKEN='f0d64f775dee3e89e602b3692b14a1d8'

API_KEY = '2313259ba3996d7bb15ba572b9fe2c5a'
parameters = {
    'lat': 28.6667,
    'lon': 77.2167,
    'exclude': 'current,minutely,daily',
    'appid': API_KEY
}
will_rain = False

response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
data = response.json()
sliced_hourly_data = data['hourly'][:12]
for i in sliced_hourly_data:
    condition_code = i['weather'][0]['id']
    if int(condition_code) > 802:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Bring Umbrella.",
            from_='+12485721562',
            to='+919102833743'
        )
    print(message.sid)


# Automated code on runpythonanywhere
import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

API_KEY = '2313259ba3996d7bb15ba572b9fe2c5a'
parameters = {
    'lat': 28.6667,
    'lon': 77.2167,
    'exclude': 'current,minutely,daily',
    'appid': API_KEY
}
will_rain = False

response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
data = response.json()
sliced_hourly_data = data['hourly'][:12]
for i in sliced_hourly_data:
    condition_code = i['weather'][0]['id']
    if int(condition_code) > 802:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
            body="Bring Umbrella.",
            from_='+12485721562',
            to='+919102833743'
        )
    print(message.status)
