# 소방청_구급통계서비스 활용시도
import requests
from decouple import config

KEY2 = config('KEY2')
URL = 'http://apis.data.go.kr/1661000/EmergencyStatisticsService/getTrafficAccidentEmgActStats'

params ={'serviceKey' : KEY2, 'pageNo' : '1', 'numOfRows' : '2', 'resultType' : 'json', 'sidoHqOgidNm' : '인천소방본부', 'rsacGutFsttOgidNm' : '부평소방서', 'rcptYm' : '202101', 'rlifOccrTyCdNm' : '기타' }

res = requests.get(URL, params=params)

print(res.content)