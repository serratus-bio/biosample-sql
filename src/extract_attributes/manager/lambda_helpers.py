import boto3
import json
lambda_client = boto3.client('lambda')

# https://medium.com/swlh/processing-large-s3-files-with-aws-lambda-2c5840ae5c91
def invoke_lambda(function_name, event):
    payload = json.dumps(event).encode('utf-8')
    lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='Event',
        Payload=payload
    )
