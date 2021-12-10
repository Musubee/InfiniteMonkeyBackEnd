from __future__ import annotations
import boto3
from decimal import Decimal

def create_table(dynamodb=None, local=False) -> None:
    if not dynamodb:
        if local:
            dynamodb = boto3.resource('dynamodb')
        else:
            dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.create_table(
            TableName='SimulationRuns',
            KeySchema = [
                {
                    'AttributeName': 'date',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'time',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'date',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'time',
                    'AttributeType': 'S' # Might have to change this to like ms since midnight if sorting the string is an issue
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
            )
    return table

def put_simulation_run(
        date: str, 
        time: str, 
        char_count: int, 
        percentage: float, 
        generated_string: str, 
        work_title: str,
        dynamodb=None,
        local=False
    ) -> None:
    if not dynamodb:
        if local:
            dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
        else:
            dynamodb = boto3.resource('dynamodb')
    
    percentage = Decimal(str(percentage))
    table = dynamodb.Table('SimulationRuns')
    response = table.put_item(
        Item={
            'date': date,
            'time': time,
            'info': {
                'char_count': char_count,
                'percentage': percentage,
                'generated_string': generated_string,
                'work_title': work_title,
            }
        }
    )
    return response
