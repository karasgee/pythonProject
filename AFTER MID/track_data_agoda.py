import bs4
import quest as qs
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By
import time
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
#browser.get_window_size() 網站大小之值
#browser.maximize_window() 最大化視窗
#print(browser.session_id) 連線id
#print(browser.title)  網站標題

result_price = browser.find_elements(By.CLASS_NAME,"PropertyCardPrice__Value")
result_name = browser.find_elements(By.CLASS_NAME,"PropertyCard__HotelName")
for i in range(len(result_price)):

        print(f'{i+1}.飯店名為 {result_name[i].text}    價格為 NT. ${result_price[i].text}元')
input("")