import json
import boto3

# Define the database and table name created
def lambda_handler(event, context):
    print(event)
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    
    # What information should be queried
    user_id = event['pathParameters']['user_id']
    
    # Define the key that will be queried in table
    result = table.get_item(
        Key={
            'user_id': user_id
        }
    )
    
    # Write an IF statement (if present return response else if not present return another response)
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

