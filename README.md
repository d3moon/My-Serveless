
# My Serveless

Esse projeto tem o intuito de desenvolver uma função para ser executada em um ambiente Cloud, preferencialmente em 
lambdas na AWS. 
A aplicação receberá dois parâmetros bucket_name e object_key, referente a um arquivo CSV
em um bucket do s3, via requisição HTTP. A função deverá ler o arquivo no bucket, tratar as 
informações e salvar no banco DynamoDB.



## Installation


```bash
  cd my-serveless
  pip install boto3
  python3 my-serveless
```
    