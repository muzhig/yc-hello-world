import json
import requests

def handler(event, context):
    resp = json.dumps({
        'event': event,
        'context': context,
    })
    return {
        'statusCode': 200,
        'body': resp,
    }
