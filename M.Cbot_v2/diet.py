import requests as req
from bs4 import BeautifulSoup as bs

def busan_menu():
    url = "https://www.pusan.ac.kr/kor/CMS/MenuMgr/menuListOnBuilding.do?mCode=MN202"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}
    web = req.get(url,headers = headers)
    soup = bs(web.content, 'html5lib')
    menu = soup.select('.menu-tbl')[:1]
    won = soup.select('.menu-tit01')[:1]
    menu = soup.select('h3.menu-tit01+p')[:1]
    day = soup.select('.day')[:1]
    date = soup.select('.date')[:1]
    
    result =""
    for d, dd, w, m in zip(day, date, won,menu):
        result += f"{'='*15}\n{d.text}요일 !\n{dd.text}\n{w.text}\n{m.text}{'='*15}"
    print(result)
    return result

if __name__=='__main__':
    busan_menu()