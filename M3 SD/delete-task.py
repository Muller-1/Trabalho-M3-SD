import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    task_id = event['pathParameters']['id']

    table.delete_item(Key={'id': task_id})

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Tarefa deletada com sucesso'})
    }