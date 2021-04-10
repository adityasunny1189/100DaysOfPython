import requests

STOCK = "RELIANCE.BSE"
COMPANY_NAME = "Tesla Inc"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


stocks_params = {
    'apikey': '464TGEKEMHROJ063',
    'symbol': STOCK,
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'outputsize': 'full'
}
response = requests.get('https://www.alphavantage.co/query', params=stocks_params)
stocks_data = response.json()
# print(stocks_data)
stocks_closing_data = float(stocks_data['Time Series (Daily)']['2021-04-09']['1. open'])
stocks_opening_data = float(stocks_data['Time Series (Daily)']['2021-04-08']['1. open'])
print(stocks_closing_data - stocks_opening_data)


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


news_params = {
    'apikey': '4be6baca7a7446e295ddbf8afd7b8162',
    'q': 'TSLA',
    'from': '2021-04-10',
    'sortBy': 'popularity'
}
response = requests.get('https://newsapi.org/v2/everything', params=news_params)
news_data = response.json()['articles'][0]['title']
print(news_data)


# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
