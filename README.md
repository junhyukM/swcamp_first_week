# 주중 학습한 내용 중 requests 간단히 재시도

## 공공데이터 포털에서 제공하는 아파트 매매 데이터 사용 (reqeusts_1.py)
## 에러가 생겨 정상적으로 마무리 못함. 
``` python 
# 아래와 같은 에러에 막혀 정상적으로 끌어오지 못함
<?xml version="1.0" encoding="UTF-8" standalone="yes"?><response><header><resultCode>99</resultCode><resultMsg>SERVICE KEY IS NOT REGISTERED ERROR.</resultMsg></header></response> 
```

- 구글링을 해 보았는데, service key 의 인코딩 디코딩 문제라고 되어있어 시도해보았지만 인코딩 디코딩을 정상적으로 하지 않아서 문제인건지 모르겠음. 의견들은 만약 그래도 안되면 API의 문제일 확률도 있다고 함. 그거였으면 좋겠음.


### 공공데이터 포털에서 제공하는 소방청 구급통계 데이터 사용 (requests_2.py)
- 무슨 문제인지 알아보고 싶어서 다른 데이터를 호출하려 시도 - json 형식으로 받았고, 강의에서 봤던 코드까지만 했지만 tag 안쪽으로 들어가서 한글로 입력한 데이터를 보려고 하면 
```
Traceback (most recent call last):
  File "C:\Users\82109\Desktop\swcamp25\req_0610\requests_2.py", line 12, in <module>
    data = res.json()
           ^^^^^^^^^^
  File "C:\Users\82109\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\models.py", line 975, in json
    raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)
requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```
위와 같은 에러가 나온다. 이유는 서칭을 꽤나 해봤지만 찾지 못하겠고 시간 소요만 너무 오래될 것 같아서 여기서  stop





## > 주말동안 오랜 시간은 아니지만 30분 정도씩 짧게 복습 또는 연습을 해봤다. 앞으로 루틴 처럼 작은 작업이지만 지속적으로 연결 할 수있도록 작은 목표를 가지기로 결심한다.