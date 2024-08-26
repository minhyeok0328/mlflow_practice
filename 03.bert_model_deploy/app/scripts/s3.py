import boto3
import os

s3 = boto3.client("s3")
paginator = s3.get_paginator('list_objects_v2')
bucket_name = 'inseop-mlmodels'

def download_dir(local_path, model_name):
    for result in paginator.paginate(Bucket=bucket_name, Prefix=model_name):
        if 'Contents' in result:
            for key in result['Contents']:
                s3_key = key['Key'] # tinybert-sentiment-analysis

                local_file = os.path.join(local_path, os.path.relpath(s3_key, model_name))
                s3.download_file(bucket_name, s3_key, local_file)

# 최대한 현업코드에 가깝게 하다보니깐 난이도가 조금 있습니다. -> 코드는 그대로 활용하시면 됩니다. 
# 20분에 진행하겠습니다 :)

# 스타트업 프로젝트 => 최대한 많이 적용 해보세요!