import json
import boto3

def lambda_handler(event, context):
    print(event)
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    
    user_id = event['pathParameters']['user_id']
    
    result = table.get_item(
        Key={
            'user_id': user_id
        }
    )
    
    if 'Item' in result:
        return {
            'statusCode': 200,
            'body': str(result['Item'])
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'User not found'})
        }

