import smtplib
from autoscraper import AutoScraper

user_id = "YouR EmaiLid"
password = "YOur PAssword"
url = "https://www.amazon.in/s?k=contacts+wallet+for+men+blue&i=luggage&crid=21EJ69QFD1AUV&sprefix=contacts+wallet+for+men+blu%2Cluggage%2C214&ref=nb_sb_noss"
wanted =[ " ₹399.00","CONTACTS Genuine Leather Slim Wallet | RFID Blocking Skinny Minimal Thin Front Pocket Wallet Sleeve Card Holder for Men (Blue)"]

n = True
while n:
  try:
    scraper = AutoScraper()
    result= scraper.build(url,wanted)
    if len(result) > 1:
      n = False

      
  except: 
    scraper = AutoScraper()
    result= scraper.build(url,wanted)
    if len(result) > 1:
      n = False
 
 
result=result[0] 
x=result.split("₹")
x=(x[1])  

text=f"Subject:Price Alert!!!\n\nYour product is avalible for DISCOUNT current price\nCurrent Price: {x}\ncheck now:{url}"

if result == "₹399.00":
  connection = smtplib.SMTP("smtp.gmail.com", 587)
  connection.starttls()
  connection.login(user_id, password)
  connection.sendmail(from_addr=user_id, to_addrs=user_id, msg=text)
  connection.close()
  print("done")

