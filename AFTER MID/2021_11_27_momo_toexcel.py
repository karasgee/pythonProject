import bs4
import quest as qs
import pandas as pd
import requests

if __name__ == '__main__':

    url ='https://www.momoshop.com.tw/category/LgrpCategory.jsp?l_code=4300300000&mdiv=1099600000-bt_0_996_10-&ctype=B'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}

    html = requests.get(url,headers=header) #headers and url
    web = bs4.BeautifulSoup(html.text,'lxml') #web
    toexcel= {}    #設定 名為 toexcel 的空字典
    num = 1          #設定num值

    result_tab = web.select('.TabContentD')   #select後面記得加該加的標點符號
    for i in range(len(result_tab)):                         #roop for len(seult_tab)

            result_li = result_tab[i].select("li")      #取出tabcontent 中的li資料

            for j in range(len(result_li)):

                 if   result_li[ j ].select('.prdName')[0].getText() != '': #如果prdName的質不為空值則進行迴圈

                    price = result_li[ j ].select('.prdPrice')[0].getText()      #印出價錢
                    name = result_li[ j ].select('.prdName')[0].getText()   #印出產品名字 PS.select記得加符號
                    toexcel[ num ] ={'name' : name, 'price': price}               # toexcel為字典   num 為字典(toexcel)的 " Key  " 值
                    num = num + 1                                                                                #每有一回圈 num 值增加一

                                               #####      toexcel ={ Num   : {  name    :   price   }   }    #####

    toexcel_df = pd.DataFrame(toexcel).T            #轉換資料至DataFrame
    print(toexcel_df)
    toexcel_df.to_excel("Momo_toexcel.xlsx")                         #寫入excel("~~~~~~~.xlsx")
