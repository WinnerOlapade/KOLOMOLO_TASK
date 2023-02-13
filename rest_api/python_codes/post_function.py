import uuid
import boto3
import json


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    
    user_id = str(uuid.uuid4())
    query = json.loads(event['body'])
    first_name = query['first_name']
    age = int(query['age'])
    
    table.put_item(
        Item={
            'user_id': user_id,
            'first_name': first_name,
            'age': age
        }
    )
    
    body={'user_id': user_id} 
    response = {
        'statusCode': 200,
        'body': json.dumps(body),
        'headers': {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'
      },
    }
    
    return response
