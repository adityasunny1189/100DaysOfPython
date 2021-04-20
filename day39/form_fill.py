from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = '/home/aditya/Documents/Devlopment/chromedriver'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://secure-retreat-92358.herokuapp.com/')

fName = driver.find_element_by_name('fName')
lName = driver.find_element_by_name('lName')
email = driver.find_element_by_name('email')
button = driver.find_element_by_css_selector('button')

fName.send_keys('Aditya')
lName.send_keys('Pathak')
email.send_keys('aditya@gmail.com')
button.send_keys(Keys.ENTER)

driver.close()






# Google Search

# driver.get('https://www.google.com')
#
# search = driver.find_element_by_name('q')
# search.send_keys('Python')
# search.send_keys(Keys.ENTER)

# driver.close()
