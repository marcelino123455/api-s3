import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    
    # Proceso    
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=nombre_bucket)
    return {
        'statusCode': 200,
        'bucket_creado': nombre_bucket
    }
