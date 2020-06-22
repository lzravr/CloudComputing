import json
import boto3
import io

def getStats(sadrzaj):
    no_lines = 0
    no_words = 0
    no_chars = 0
    for line in sadrzaj:
        words = line.split()
        no_lines += 1
        no_words += len(words)
        no_chars += len(line)
    return (no_lines, no_words, no_chars)

def lambda_handler(event, context):
    
    s3 = boto3.client("s3")
    db_resource = boto3.resource('dynamodb')
    db = db_resource.Table('lazar-s3-list')
    
    s3_records = event["Records"][0]
    bucket_name = str(s3_records["s3"]["bucket"]["name"])
    file_name = str(s3_records["s3"]["object"]["key"])
        
    if event['Records'][0]['eventName'] == 'ObjectCreated:Put':
        file = s3.get_object(Bucket=bucket_name, Key=file_name)
        content = file["Body"].read()
        
        b = io.BytesIO(content)
        (lines, words, chars) = getStats(b)
        db.put_item(Item={
            'id': file_name,
            'lines': lines,
            'words': words,
            'chars': chars
        })
        
       
    if event['Records'][0]['eventName'] == 'ObjectRemoved:Delete':
        print ('Object deleted')
        try:
            db.delete_item(Key={'id': file_name })
        except:
            print('Deletion error')
            
            
    if event['Records'][0]['eventName'] == 'ObjectCreated:Copy':
        file = s3.get_object(Bucket=bucket_name, Key=file_name)
        content = file["Body"].read()
        b = io.BytesIO(content)
        (lines, words, chars) = getStats(b)
        db.put_item(Item={
            'id': file_name,
            'lines': lines,
            'words': words,
            'chars': chars
        })
    
    return {
        'statusCode': 200,
        'body': "OK"
    }

