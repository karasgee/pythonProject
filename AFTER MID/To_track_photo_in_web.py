import bs4
import quest as qs
import pandas as pd
import requests

if __name__ == '__main__':
        target ='car' #input('target?')
        lim = 5   # input('輸入limit值')
        url =(f'https://unsplash.com/s/photos/{target}')  #設定url
        print(url)

        html = requests.get(url)   #用Requesst  By  url  抓 取 資 訊
        web = bs4.BeautifulSoup(html.text,'lxml')     #設定bs4模組

        result = web.select('.YVj9w',limit=lim)    #設定抓取特定之資訊(class =={ . YVj9w }    且使用 limlit去限制抓取資料量)

        for i in range(len(result)):

            with open(target+str(i+1)+".jpg", 'wb') as f:
                picture = requests.get(result[i]['src'])
                f.write(picture.content)







