# 아파트 매매 데이터 활용 시도
import requests
from decouple import config

KEY = config('KEY')
URL = f'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade'

params ={'serviceKey' : KEY, 'LAWD_CD' : '11110', 'DEAL_YMD' : '201512' }

res = requests.get(URL, params=params)

print(res.text)


