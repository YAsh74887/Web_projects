from  selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
dt =driver.find_element(By.XPATH,'//*[@id="articlecount"]/a[1]')
# list =[]
# for time in dt:
#   p=(time)
t=(dt.text)

  
# print(p.text)
# li = list(p.split(" "))
# print(li)
# driver.close()