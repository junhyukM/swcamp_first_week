# 소방청_구급통계서비스 활용시도
import requests
import json
from decouple import config

KEY = config('KEY')
URL = f'http://apis.data.go.kr/1661000/EmergencyStatisticsService/getTrafficAccidentEmgActStats'

params ={'serviceKey' : KEY, 'pageNo' : '1', 'numOfRows' : '2', 'resultType' : 'json', 'sidoHqOgidNm' : '인천소방본부', 'rsacGutFsttOgidNm' : '부평소방서', 'rcptYm' : '202101', 'rlifOccrTyCdNm' : '기타' }

res = requests.get(URL, params=params)
data = res.json()
data = data['body']['items'][0]['sidoHqOgidNm']

print(data)