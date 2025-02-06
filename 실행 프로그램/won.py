import requests  # requests라는 모듈을 가져옴
import json  # json이라는 형식의 라이브러리를 가져옴
url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=xItBWhMQuUZDrFMj4YnvlNqRhWmypC1v&data=AP01'
res = requests.get(url).text
data = json.loads(res)
# print(type(data))
result = data[-1]['deal_bas_r']

print('='*40)
print(f'오늘의 환율은 1달러에 {result} 원 입니다.')
print('='*40)