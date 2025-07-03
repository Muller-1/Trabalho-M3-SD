import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    # 1) log completo do event
    print("EVENT RECEIVED:", json.dumps(event))

    # 2) extrair o body de forma segura
    raw_body = event.get('body')
    if raw_body is None:
        # se vier no formato v2 do HTTP API, pode estar em event['rawBody']
        raw_body = event.get('rawBody')

    if raw_body is None:
        # nada encontrado: devolve erro
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Bad Request: não veio campo body'})
        }

    data = json.loads(raw_body)

    task = {
        'id': str(uuid.uuid4()),
        'title': data['title'],
        'description': data['description'],
        'date': data['date']
    }

    table.put_item(Item=task)

    return {
        'statusCode': 201,
        'body': json.dumps({'message': 'Tarefa criada com sucesso', 'task': task})
    }