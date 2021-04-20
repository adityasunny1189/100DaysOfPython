from selenium import webdriver

chrome_driver_path = '/home/aditya/Documents/Devlopment/chromedriver'

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://www.python.org')

events_time = driver.find_elements_by_css_selector('.event-widget time')
events_name = driver.find_elements_by_css_selector('.event-widget li a')

events = {}

for i in range(len(events_name)):
    events[i] = {
        'time': events_time[i].text,
        'name': events_name[i].text
    }

for (i, j) in events.items():
    print(i, j)

driver.close()
