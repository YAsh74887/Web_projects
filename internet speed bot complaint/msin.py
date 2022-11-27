from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

user_id = "Your twitter user id "
password = "your twutter password "

ideal_download_speed = 20
ideal_upload_speed = 20

# getting speed data from speedtest.net
driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.speedtest.net/")
time.sleep(2)
accept = driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]')
accept.click()
go = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
go.click()
time.sleep(50)
download_speed = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
download_speed=float(download_speed.text)

upload_speed = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
upload_speed =float(upload_speed.text)
time.sleep(5)



# if internet spped is less than ideal speed below code will trigger and will send tweet to your service provider 
if download_speed < ideal_download_speed and upload_speed < ideal_upload_speed:
  driver.get("https://twitter.com/i/flow/login")
  time.sleep(10)
  twitter_user = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
  twitter_user.send_keys(user_id)
  twitter_user.send_keys(Keys.ENTER)
  time.sleep(10)
  twitter_password = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
  twitter_password.send_keys(password)
  twitter_password.send_keys(Keys.ENTER)
  time.sleep(10)
  tweet = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
  tweet.click()
  time.sleep(10)
  send_msg = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
  
  send_msg.send_keys(f"Why my internet speed is slow \ndownload:{download_speed} \nupload:{upload_speed}")
  time.sleep(10)

# in above code tweet box will pop up then tag according to your service provider 
driver.close()