import boto3
import csv
import json
from datetime import datetime

profile = input('Insira o profile: ')
region = input('Insira a região: ')

# Conectando com o S3
session = boto3.Session(profile_name=profile, region_name=region)
s3 = boto3.client("s3")

# Conectando com o Dynamo
dynamodb = boto3.resource("dynamodb")


def lambda_handler(event, context):
    # Definindo bucket_name e object_key do evento
    bucket_name = event["bucket_name"]
    object_key = event["object_key"]

    # Baixando o arquivo CSV do S3
    csv_file = s3.get_object(Bucket=bucket_name, Key=object_key)["Body"].read()

    # Convertendo o arquivo CSV em uma lista de dicionários
    with open('arquivo_exemplo.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]

    # Iterando os dados e adicionando ao DynamoDB
    table = dynamodb.Table("mytable")
    for row in data:
        # Removendo as máscaras do CPF e CNPJ
        row["cpf"] = row["cpf"].replace("-", "").replace(".", "")
        row["cnpj"] = row["cnpj"].replace("-", "").replace(".", "").replace("/", "")

        # Formatando os campos de data para aaaa-MM-dd
        row["date1"] = datetime.strptime(row["date1"], "%d/%m/%Y").strftime("%Y-%m-%d")
        row["date2"] = datetime.strptime(row["date2"], "%d/%m/%Y").strftime("%Y-%m-%d")

        # Adicionando os dados ao DynamoDB
        table.put_item(Item=row)

    return {"statusCode": 200, "body": json.dumps("Success")}

