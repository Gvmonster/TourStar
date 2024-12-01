import boto3
import pandas as pd
from io import StringIO
import stomp
import json

s3 = boto3.client('s3')

def fileUpload(bucket_name, file_key, s3):
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    csv_content = response['Body'].read().decode('utf-8')

    csv_buffer = StringIO(csv_content)

    data = pd.read_csv(csv_buffer)

    print(data.head())

    return 

"""def producer():
    def __init__(self, host, port):
        self.connect_ActiveMQ = stomp.Connection([(host, port)])
        self.connect_ActiveMQ.connect(wait=True)  

    def send_data(self, destinatario, assunto, corpo):
        mensagem = {
            "destinatario": destinatario,
            "assunto": assunto,
            "corpo": corpo
        }"""


fileUpload('wonders-of-world-data-2024', 'wonders_of_world.csv' , s3)
fileUpload('wonders-of-world-data-2024', 'tips_wonders_of_world.csv', s3)