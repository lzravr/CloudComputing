import json
import base64
import boto3

bucket = 'lazar-s3'

def readFile(fajl):
    base64_bytes = fajl
    fajl = base64.b64decode(base64_bytes)
    return fajl

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    if event:
        dogadjaj = event['httpMethod']
        print(dogadjaj)
        
        if dogadjaj == "GET":
            zahtev = event['queryStringParameters']
            data = s3.get_object(Bucket=bucket, Key=zahtev['file'])
            contents = data['Body'].read()
            file = base64.b64encode(contents)
            
            print(contents)
            
            return { 
                'statusCode': 200, 
                'headers' : {
                    'Content-Type' : 'text/plain',
                    'Content-Disposition' : 'attachment; filename="' +zahtev['file'] +'"'
                },
                
                'body' : file,
                'isBase64Encoded': True
            }
            
        if dogadjaj == "POST":
            
            body = json.loads(event['body'])
            
            naziv_fajla = body['filename']
            sadrzaj_fajla = readFile(body['file'])
            
            try:
                s3_response = s3.put_object(Bucket=bucket, Key=naziv_fajla, Body=sadrzaj_fajla)
            except Exception as e:
                print(e)
                raise e
        
        if dogadjaj == "DELETE":
            zahtev = event['queryStringParameters']
            try:
                response = s3.delete_object(Bucket=bucket, Key=zahtev['filename'])
            except Exception as e:
                print(e)
                raise e
                
            return { 
                'statusCode': 200, 
                'body' : json.dumps('DELETED') 
            }
            
        if dogadjaj == "PUT":
            # body = json.loads(event['body'])
            zahtev = event['queryStringParameters']
            data = s3.get_object(Bucket=bucket, Key=zahtev['filename'])
            sadrzaj_fajla = data['Body'].read()
            
            nov_fajl = zahtev['newfilename']
            
            try:
                s3_response = s3.put_object(Bucket=bucket, Key=nov_fajl, Body=sadrzaj_fajla)
                response = s3.delete_object(Bucket=bucket, Key=zahtev['filename'])
            except Exception as e:
                print(e)
                raise e
            return { 
                'statusCode': 200, 
                'body' : json.dumps("RENAMED") 
                
            }
        
    return {
        'statusCode': 200,
        'body': json.dumps("dsadsa")
    }

