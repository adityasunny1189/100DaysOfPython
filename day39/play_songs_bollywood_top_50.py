import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = '/home/aditya/Documents/Devlopment/chromedriver'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://gaana.com/playlist/gaana-dj-hindi-romance-top-50')

play_button = driver.find_element_by_css_selector('._play_large a')
play_button.send_keys(Keys.ENTER)

time.sleep(60)

driver.close()
