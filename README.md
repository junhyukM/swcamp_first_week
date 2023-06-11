# 주중 학습한 내용 중 requests 간단히 재시도

## 공공데이터 포털에서 제공하는 아파트 매매 데이터 사용
## 에러가 생겨 정상적으로 마무리 못함. 
``` python 
# 아래와 같은 에러에 막혀 정상적으로 끌어오지 못함
<?xml version="1.0" encoding="UTF-8" standalone="yes"?><response><header><resultCode>99</resultCode><resultMsg>SERVICE KEY IS NOT REGISTERED ERROR.</resultMsg></header></response> 
```

- 구글링을 해 보았는데, service key 의 인코딩 디코딩 문제라고 되어있어 시도해보았지만 인코딩 디코딩을 정상적으로 하지 않아서 문제인건지 모르겠음. 의견들은 만약 그래도 안되면 API의 문제일 확률도 있다고 함. 그거였으면 좋겠음.


