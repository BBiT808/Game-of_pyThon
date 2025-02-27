import requests as req

def mov():
    url = 'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=1f1209fd1763d09de17660c9fe336cc1&targetDt=20250215&boxofficeType'
    res = req.get(url).json()
    result = res['boxOfficeResult']['dailyBoxOfficeList']
    
    movies = []
    for n in result:
        movies.append(f"{n['rank']}위: {n['movieNm']}\n")
        
    print(movies)
    return "\n".join(movies)

if __name__ =='__main__':
    mov()
