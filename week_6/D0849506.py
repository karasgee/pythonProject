import requests
import bs4
import pandas as pd
import collections

if __name__ == '__main__':

    header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36' }

    url ='https://www.momoshop.com.tw/category/LgrpCategory.jsp?l_code=4300300000&mdiv=1099600000-bt_0_996_10-&ctype=B'

    html = requests.get(url,headers=header)
    web = bs4.BeautifulSoup(html.text, 'lxml')

    product = {}
    result = web.select('.prdName')

    for i  in range(len(result)):

        product[ i ] ={ 'model' : result[i].getText()}
       # print(product[i])

    p = collections(product,)
    product_df = pd.DataFrame(product).T
   # print(product_df)
    product_df.to_excel("test.xlsx")













