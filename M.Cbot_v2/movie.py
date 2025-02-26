import requests as req
def mov():
    url= 'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=1f1209fd1763d09de17660c9fe336cc1&targetDt=20250215&boxofficeType'
    res = req.get(url).json()
    result = res['boxOfficeResult']['dailyBoxOfficeList']
    
    for n in result:
        print(n["rank"],n["movieNm"])

if __name__ =='__main__':
    mov()
