import uuid
import boto3
import json

# Define the database and table name created
def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    
    # What information should be queried
    user_id = str(uuid.uuid4())
    query = json.loads(event['body'])
    first_name = query['first_name']
    age = query['age']
    
    # Define the item content that will be put in table
    table.put_item(
        Item={
            'user_id': user_id,
            'first_name': first_name,
            'age': age
        }
    )
    
    # Define response that will be returned depending on status code
    body={'user_id': user_id} 
    response = {
        'statusCode': 200,
        'body': json.dumps(body),
        'headers': {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'
      },
    }
    
    # Return response
    return response
