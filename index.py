import json
import requests


def handler(event, context):
    resp = json.dumps({
        'event': event,
    })
    return {
        'statusCode': 200,
        'body': resp,
        'headers': {
            'Content-Type': 'application/json',
        },
    }
