from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')
print("break")
a = driver.get_cookies()
b = []
for i in a:
    if i['name'] == 'xs' or i['name'] == 'c_user':
        b.append(i['value'])


