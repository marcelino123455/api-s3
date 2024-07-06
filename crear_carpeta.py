import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    nombre_dir = event['body']['carpeta']
    llave = nombre_dir+"/"
    # Proceso    
    s3 = boto3.client('s3')
    s3.put_object(
        Bucket=nombre_bucket,
        Body='',
        Key=llave
        )
    return {
        'statusCode': 200,
        'directorio': nombre_bucket,
        'carpeta': nombre_dir

    }
