import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = '/home/aditya/Documents/Devlopment/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://orteil.dashnet.org/cookieclicker/')

big_cookie = driver.find_element_by_id('bigCookie')
store = driver.find_elements_by_css_selector('#sectionRight #store #products .enabled')
items_price = driver.find_elements_by_css_selector('#price')

game_is_on = True
timeout = time.time() + 60*5

while game_is_on:
    if time.time() > timeout:
        break
    big_cookie.send_keys(Keys.ENTER)
    time.sleep(5)
    store = driver.find_elements_by_css_selector('#sectionRight #store #products .enabled')
    store[-1].send_keys(Keys.ENTER)


cookies = driver.find_element_by_css_selector('#cookies')
print(cookies.text)

driver.close()
