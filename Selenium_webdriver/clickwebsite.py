from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver  = "Selenium_webdriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver)


driver.get("https://www.appbrewery.co/p/newsletter")
search= driver.find_element(By.XPATH,'//*[@id="member_email"]')
search.send_keys("yashthorat60@gmail.com")
search.send_keys(Keys.ENTER)
time.sleep(16)