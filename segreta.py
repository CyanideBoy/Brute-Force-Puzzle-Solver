import time
from selenium import webdriver
import string

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://techfest.org/segreta/login')
time.sleep(2) # Let the user actually see something!
search_box = driver.find_element_by_name('email')
search_box.send_keys('_ENTER_YOUR_EMAIL_')
sbox = driver.find_element_by_name('password')
sbox.send_keys('_ENTER_YOUR_PASSWORD_')
search_box.submit()
time.sleep(2)

with open('word-list.txt') as sal:
	content = sal.readlines()
	content = [x.strip() for x in content]

for i in range(len(content)):
	y = driver.current_url
	if y=='https://techfest.org/segreta/level/15':
		abox = driver.find_element_by_name('answer')
		abox.send_keys(content[i])
		abox.submit()
	else:
		break			


time.sleep(2) # Let the user actually see something!
driver.quit()