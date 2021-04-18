from selenium import webdriver

chrome_driver_path = '/home/aditya/Documents/Devlopment/chromedriver'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/dp/B08N5LNQCX/ref=sr_1_3?crid=19494P5CVXDEC&dchild=1&keywords=macbook+air&qid=1618715711&sprefix=mac%2Caps%2C438&sr=8-3')
price = driver.find_element_by_id('priceblock_ourprice')

print(price.text)

driver.close()
