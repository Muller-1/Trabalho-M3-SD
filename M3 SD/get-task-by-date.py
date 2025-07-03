import json
import boto3
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    date_param = event['pathParameters']['date']

    response = table.scan(
        FilterExpression=Attr('date').eq(date_param)
    )

    tasks = response.get('Items', [])

    return {
        'statusCode': 200,
        'body': json.dumps(tasks)
    }