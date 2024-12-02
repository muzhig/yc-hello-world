import requests

def handler(event, context):
    uuid = requests.get('https://httpbin.org/uuid').json()['uuid']
    return {
        'statusCode': 200,
        'body': f'UUID: {uuid}',
    }