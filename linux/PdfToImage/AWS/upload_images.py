import boto3


AWS_ACCESS_KEY_ID = 'XXXXXXXXXXXXXXXXXXXX'

AWS_SECRET_ACCESS_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

AWS_REGION = 'us-east-1'
client = boto3.client('s3')

response = client.list_buckets()
