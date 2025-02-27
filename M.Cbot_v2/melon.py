import requests as req
from bs4 import BeautifulSoup as bs

url = "https://www.melon.com/chart/index.htm"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}
web = req.get(url, headers=headers)
soup = bs(web.content, 'html.parser')

def mel():
    title = soup.select('.wrap_song_info .rank01')[:10]
    name = soup.select('.checkEllipsis a')[:10]  # 10위까지 !!

    result = ""
    for i, (t, n) in enumerate(zip(title, name), 1):
        result += f'{i}위 : {t.text.strip()} / {n.text}\n'

    print(result)
    return result

if __name__ =='__main__':
    mel()
