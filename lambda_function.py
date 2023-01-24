import json
import boto3

def lambda_handler(event, context):
    region = event['region']
    bucket_name = event['bucket_name']
    s3_client = boto3.client('s3', region_name=region)
    location = {'LocationConstraint': region}
    s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
    return {
        'statusCode': 200,
        'body': json.dumps('Bucket Creation Successful!')
    }