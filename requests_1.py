import requests
from xml_to_dict import XMLtoDict
from decouple import config

KEY = config('KEY')
URL = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade'

params ={'serviceKey' : 'KEY', 'LAWD_CD' : '11110', 'DEAL_YMD' : '201512' }

res = requests.get(URL, params=params)

# xd = XMLtoDict()
# data = xd.parse(res.content)


print(res.text)


