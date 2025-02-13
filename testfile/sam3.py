
if __name__ == "__main__":
    import requests as req
    url = "https://finance.naver.com/sise/sise_market_sum.naver"
    web = req.get(url)
    html = web.text
    # print(html)
    f1 = html.find('삼성전자')
    f2 = html.find('기아')
    def marketprice():
        com = input("시세를 알고 싶은 회사를 입력하세요 ! ")
        if com == "삼성":
            print('삼성전자 : '+html[f1:f1+100][19:50].replace('<td class="number">',"").replace('</td>',""))
        if com == "기아":
            print('기아 : '+html[f2:f2+100][17:50].replace('<td class="number">',"").replace('</td>',""))
    marketprice()
else:
    print('')