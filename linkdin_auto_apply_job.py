
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
import time
 
chrome_driver_path = 'Selenium_webdriver\chromedriver.exe'
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
 
driver.get(url='https://www.linkedin.com/')
 
email = driver.find_element(By.ID, 'session_key')
password = driver.find_element(By.ID, 'session_password')
signIn_btn = driver.find_element(By.CLASS_NAME, 'sign-in-form__submit-button')
 
email.send_keys('your email')
password.send_keys('your password ')
signIn_btn.send_keys(Keys.ENTER)
time.sleep(5)
 
jobs = driver.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a')
jobs.send_keys(Keys.ENTER)
time.sleep(5)
 
search_tab = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Search by title, skill, or company"]')
search_tab.send_keys('python intern', Keys.ENTER)
 
time.sleep(15)
 
easy_apply = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Easy Apply filter."]')
easy_apply.send_keys(Keys.ENTER)
time.sleep(5)
 


