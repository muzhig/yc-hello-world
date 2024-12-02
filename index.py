import json
import requests

# https://functions.yandexcloud.net/d4ek0v5nv8uek7ed0d9l

def handler(event, context):
    # {
    #     "httpMethod": "GET", 
    #     "headers": {
    #         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    #         "Accept-Encoding": "gzip, deflate, br, zstd", 
    #         "Accept-Language": "en-US,en;q=0.9",
    #         "Cache-Control": "max-age=0",
    #         "Host": "functions.yandexcloud.net", 
    #         "Sec-Ch-Ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"", 
    #         "Sec-Ch-Ua-Mobile": "?0", 
    #         "Sec-Ch-Ua-Platform": "\"macOS\"", 
    #         "Sec-Fetch-Dest": "document", 
    #         "Sec-Fetch-Mode": "navigate", 
    #         "Sec-Fetch-Site": "none", 
    #         "Sec-Fetch-User": "?1", 
    #         "Uber-Trace-Id": "f2c954ab6f49694a:0000:0000:1", 
    #         "Upgrade-Insecure-Requests": "1", 
    #         "User-Agent": "Mozilla/5.0 Chrome/131.0.0.0 Safari/537.36", 
    #         "X-Forwarded-For": "0.0.0.0", 
    #         "X-Real-Remote-Address": "[0.0.0.0]:0000", 
    #         "X-Request-Id": "40ed3bea-fd66-4dce-8ff1-e40464e9ef82", 
    #         "X-Trace-Id": "3ea79760-0000-0000-0000-537de4ec7e75"
    #     }, 
    #     "url": "", 
    #     "params": {}, 
    #     "multiValueParams": {}, 
    #     "pathParams": {}, 
    #     "multiValueHeaders": {...},
    #     "body": "", 
    #     "isBase64Encoded": True
    # }

    resp = json.dumps(event)
    return {
        'statusCode': 200,
        'body': resp,
        'headers': {
            'Content-Type': 'application/json',
        },
    }
