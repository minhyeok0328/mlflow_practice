from fastapi import FastAPI, UploadFile, File
from io import BytesIO
from PIL import Image
from predict import predict

app = FastAPI() # 백엔드 서버가 완성

# 라우터 (경로)
@app.get('/') # 127.0.0.1:8000/
def root():
    return {"Hello":"FastAPI!"}

@app.get('/items/{item_id}')
def show_item(item_id):
    return {"Hello":item_id}

@app.post('/api/v1/predict')
async def image_predict_api(file: UploadFile = File(...)): # redoc => 파일 업로드 가능
    raw_data = await file.read()
    image_bytes_io = BytesIO(raw_data)
    print(image_bytes_io)
    image = Image.open(image_bytes_io)
    pred = predict(image)

    return pred

# api/v1/predict => 천천히 나중에 deprecated
# - 이미지 파일 2개 이상 업로드 가능 (업데이트 안한사람들 => 업데이트를 유도하는 방향) 

# api/v2/predict => 신규 버전
# - 이미지 파일 1개만 가능


# uvicorn main:app --reload
# - reload: 코드가 변경되면 서버를 새로 시작.

# FastAPI 가장 큰 특징 2개
# - 비동기?? -> python 비동기가 아닌가요? 파이썬은 기본적으로 동기? => ASGI-비동기 (<- WSGI-동기)
# 동기-비동기
# (스타벅스) => 말차프라푸치노휘핑크림10번초콜렛10개 - 아아 - 아아 - 아아
# 동기:
# - 말차프라푸치노휘핑크림10번초콜렛10개 - 아ㅏ................................................................
# - 무조건 들어간 순서대로 아웃풋이 결정
# 비동기: 
# - 말차프라푸치노휘핑크림10번초콜렛10개(주문받았어)
# - 아아 (접수완료)
# - 아아 (접수완료)
# - 아아 (접수완료)
# Queue 

# - 데이터타입 -> pydantic

# FastAPI
# 혹시 그럼 Flask랑은 어떤 차이가 있을까요? 그냥 Flask 쓰면 안될까요? 어떻게 생각하세요?
# - 수빈: Swagger까지 만들어준다? => Flask - Swagger 붙이면 되죠.

# FastAPI
# (1) 비동기 (ASGI)
# (2) 데이터 타입 지정 (Pydantic)

# 간단한 모델을 불러와서 REST API (실습)

# 15시 15분에 뵙겠습니다 :)

# + 장고랑은 어떤 차이가 있나요?
# + FastAPI => Microservices

# 4시 15분에 뵙겠습니다:)
