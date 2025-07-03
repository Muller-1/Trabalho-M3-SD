import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    task_id = event['pathParameters']['id']
    data = json.loads(event['body'])

    # Usamos atributos nomeados para evitar palavras reservadas
    update_expr = "SET #t = :t, #dsc = :d, #dt = :dt"
    expr_attr_names = {
        "#t": "title",
        "#dsc": "description",
        "#dt": "date"
    }
    expr_attr_values = {
        ":t": data['title'],
        ":d": data['description'],
        ":dt": data['date']
    }

    table.update_item(
        Key={'id': task_id},
        UpdateExpression=update_expr,
        ExpressionAttributeNames=expr_attr_names,
        ExpressionAttributeValues=expr_attr_values
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Tarefa atualizada com sucesso'})
    }