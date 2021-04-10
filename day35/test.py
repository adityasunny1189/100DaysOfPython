import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

stocks_on_date1 = str((datetime.datetime.today() - datetime.timedelta(days=1)).date())
stocks_on_date2 = str((datetime.datetime.today() - datetime.timedelta(days=2)).date())

stocks_params = {
    'apikey': '464TGEKEMHROJ063',
    'symbol': STOCK,
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'outputsize': 'full'
}

news_params = {
    'apikey': '4be6baca7a7446e295ddbf8afd7b8162',
    'q': STOCK,
    'from': '2021-04-10',
    'sortBy': 'popularity'
}

response = requests.get('https://www.alphavantage.co/query', params=stocks_params)
stocks_data = response.json()

response = requests.get('https://newsapi.org/v2/everything', params=news_params)
news_data_list = response.json()['articles']

news_message = {}
for i in range(0, 2):
    news_message[news_data_list[i]['title']] = news_data_list[i]['url']

stocks_closing_data = float(stocks_data['Time Series (Daily)'][stocks_on_date1]['1. open'])
stocks_opening_data = float(stocks_data['Time Series (Daily)'][stocks_on_date2]['1. open'])

stocks_price_diff = stocks_closing_data - stocks_opening_data
in_profit = False
diff_margin_percent = round((stocks_price_diff / stocks_opening_data) * 100, 2)

if stocks_price_diff > 0:
    in_profit = True

if in_profit:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
            body = f'Stocks in profit\nGain = {diff_margin_percent}%\n{news_message}',
            from_='+12485721562',
            to='+919102833743'
        )
    print(message.status)
else:
    print('message not sent')
