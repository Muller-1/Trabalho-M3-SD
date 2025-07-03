import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    task_id = event['pathParameters']['id']

    response = table.get_item(Key={'id': task_id})

    if 'Item' in response:
        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Tarefa não encontrada'})
        }