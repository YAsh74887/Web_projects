from selenium import webdriver
import time
from selenium.webdriver.common.by import By
def driver_open(link):
  driver.get(link)
  return driver
  
driver = webdriver.Chrome('chromedriver.exe')
driver_open("https://housinganywhere.com/s/Munich--Germany/shared-rooms")
time.sleep(5)

data = driver.find_elements(By.TAG_NAME,'h3')
list = []
for n in data:
  list.append(n.text)
  
print(list)  
n=0
for i in list:
 
  data = list[n]
  print(data)
  form = driver.get('https://forms.gle/iz5bSNXLQcjZ5H6e9')
  input = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/input')
  time.sleep(5)
  input.send_keys(data)
  time.sleep(5)
  click = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
  click.click()
  other_response = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
  other_response.click()
  n=n+1
   
  time.sleep(5) 
  

 
 

