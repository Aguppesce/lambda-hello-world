import json

def lambda_handler(event, context):
    print("¡Hola desde el código v1!")
    return {
        'statusCode': 200,
        'body': json.dumps('¡Hola desde Lambda v1!')
    }