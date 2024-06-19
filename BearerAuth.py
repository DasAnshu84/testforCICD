import json
def error(message):
        return {
            'statusCode': 403,
            'body': json.dumps(message)
        }

Valid_Token = "f83c6105-1731-4cd9-9d94-9543ff01bfe1"

def validatingBearertoken(event):

    Bearer = event.get("headers",{}).get("authorization",None)
    
    if Bearer is None                   :   return 0,error("Bearer Token Missing")
    if Bearer != f"Bearer {Valid_Token}":   return 0,error("Bearer Token Not valid")
    
    parameters = event.get("queryStringParameters",None)
    
    if parameters is None               :   return 0,error("Parameters Missing")
    return 1,parameters