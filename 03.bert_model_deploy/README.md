# FastAPI EC2 호스팅

(1) 로컬에서 Docker 기반으로 서버세팅

- Docker => Folder 단위 관리
- FastAPI => app 폴더 관리 => python package(requirements.txt)

- 로컬에서 한번 빌드를 해봐야죠.
  > docker-compose build

(2) EC2 인스턴스 생성

- GUI 선택...

SSH를 통해 서버에 접속

> chmod 400 "fastapi-backend-keypair.pem"
> ssh -i "/Users/inseop/Desktop/fastapi-backend-bertmodel/02.bert_model_deploy/fastapi-backend-keypair.pem" ec2-user@ec2-3-35-219-35.ap-northeast-2.compute.amazonaws.com

(3) 도커 컨테이너 푸쉬

(4) EC2에서 컨테이너 풀
