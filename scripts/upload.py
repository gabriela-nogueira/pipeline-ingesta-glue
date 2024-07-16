from dotenv import load_dotenv
from datetime import datetime
import boto3
import os

def upload_data_to_s3():
    load_dotenv()

    actual_date = datetime.today().strftime("%d-%m-%y")

    AWS_SERVER_PUBLIC_KEY = os.getenv('AWS_ACESS_KEY')
    AWS_SERVER_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
    AWS_SESSION_TOKEN = os.getenv('AWS_USER_TOKEN')

    # pegando o path atual
    path = os.getcwd().split('\\scripts')[0]
    
    # criando o objeto de client do tipo s3
    s3 = boto3.client('s3', 
                        aws_access_key_id=AWS_SERVER_PUBLIC_KEY,
                        aws_secret_access_key=AWS_SERVER_SECRET_KEY,
                        aws_session_token = AWS_SESSION_TOKEN
    )

    s3.upload_file(
        Filename=f"{path}/pre_processed/data_{actual_date}.parquet",
        Bucket="fiap-mlet-gsnogueira",
        Key=f"raw_data/{actual_date}/arquivo.parquet"
    )

    return None
