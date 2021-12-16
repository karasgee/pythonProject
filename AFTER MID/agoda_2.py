import bs4
import quest as qs
import pandas as pd
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys





url = 'https://www.agoda.com/zh-hk/search?city=12080&checkIn=2021-11-21&los=1&rooms=1&adults=2&children=0&locale=zh-hk&ckuid=b2df0a67-a20c4dd4-ba6d-c74a2950fed8&prid=0&currency=TWD&correlationId=4b040e99-9898-4f7a-8286-190181a7bd9f&pageTypeId=5&realLanguageId=7&languageId=7&origin=TW&cid=1844104&userId=b2df0a67-a20c-4dd4-ba6dc74a2950fed8&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=28&currencyCode=TWD&htmlLanguage=zh-hk&cultureInfoName=zh-hk&machineName=hkcrweb2027&trafficGroupId=1&sessionId=sctqafif1lqfwtgarlssvuyq&trafficSubGroupId=84&aid=130589&useFullPageLogin=true&cttp=4&isRealUser=true&mode=production&checkOut=2021-11-22&priceCur=TWD&textToSearch=%E5%8F%B0%E4%B8%AD%E5%B8%82&travellerType=1&familyMode=off&productType=-1'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
'''
html = requests.get(url,headers=header) #headers and url
web = bs4.BeautifulSoup(html.text,'lxml')
result = web.select('PropertyCard__HotelName')
print(result)
'''
browser = webdriver.Chrome(service = Service("chromedriver.exe"))  #設定webdriver
browser.get(url)  #取得網站
time.sleep(5)
btn = browser.find_element(By.CLASS_NAME,  "Buttonstyled__ButtonStyled-sc-5gjk6l-0.kYHirW.Box-sc-kv6pi1-0.hVPGaU")
btn.click()
print("click done")
stopcontrol = input("輸入任一值 以繼續")

js = "window.scrollTo(0,0)"
ele = browser.find_element(By.TAG_NAME,'body')
height = browser.execute_script("return this.scrolly")
print(f'起始的高為{height}')
temp = browser.execute_script(js)
while True :

    ele.send_keys(Keys.PAGE_DOWN)
    print(" scroll down! ")
    height = browser.execute_script("return this.scrollY")

    print(f'現在的高為{height}')
   # print(f'底部高度為{temp} , 現時高度為{height}')
    time.sleep(1)
    if 24000 <= height:
            next_btn = browser.find_element(By.CLASS_NAME,"btn.pagination2__next")
            next_btn.click()
            time.sleep(3)

            break

