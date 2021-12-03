if __name__ == '__main__':

    hotel ={'name':
            {'上雅居' :{'score':9.6,'price':3900},
            '家家陽光' :{'score':9.6,'price':3600},
            '冬山驛' :{'score':9.2,'price':3300},
            '大福謙' :{'score':9.7,'price':4500}}}
    print('分數高於9.5的住宿: ')
    print(f"上雅居 ，分數為 {hotel['name']['上雅居']['score']}，價格為TWD{hotel['name']['上雅居']['price']}")
    print(f"家家陽光 ，分數為 {hotel['name']['家家陽光']['score']}，價格為TWD{hotel['name']['家家陽光']['price']}")
    print(f"大福謙 ，分數為 {hotel['name']['大福謙']['score']}，價格為TWD{hotel['name']['大福謙']['price']}")