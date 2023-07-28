import json
from selenium import webdriver
import requests
with open('C:\\Users\\Primotech\\Documents\\url_lms.json') as f:
    data = json.load(f)
num=0

 
driver = webdriver.Chrome()

for url in data:
 try:    
   driver.get(url["URL"])
   num=num+1
   r = requests.head(url)

   if r.status_code < 404:
         print("Page number",url, r.status_code)     
       
            
 except requests.exceptions.InvalidSchema:
     ("")
       
 print(num)