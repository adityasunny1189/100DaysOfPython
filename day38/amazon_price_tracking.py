import lxml
import smtplib
import requests
from bs4 import BeautifulSoup

headers = {
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}

url = 'https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/dp/B08N5LNQCX/ref=sr_1_3?crid=19494P5CVXDEC&dchild=1&keywords=macbook+air&qid=1618715711&sprefix=mac%2Caps%2C438&sr=8-3'

response = requests.get(url, headers=headers)

html_data = response.text

soup = BeautifulSoup(html_data, "lxml")
macbook_price = soup.select_one('#priceblock_ourprice').getText()
actual_price_of_macbook = float(macbook_price.split('$')[1])

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user='aditya9102833743@gmail.com', password='Adisunny1234')
    connection.sendmail(from_addr='aditya9102833743@gmail.com',
                        to_addrs='adityapathak1189@gmail.com',
                        msg=f"Subject:Macbook Sale\n\nThe current price of macbook is: {actual_price_of_macbook}")
