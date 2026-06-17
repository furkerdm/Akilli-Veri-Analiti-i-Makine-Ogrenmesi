import json
import boto3
import joblib

# S3 istemcisi (Lambda içinde IAM rolü ile yetkilendirilir)
s3 = boto3.client('s3')

def lambda_handler(event, context):
    print("Gelen Event Yapısı: ", json.dumps(event))
    
    # Event formatını esnek şekilde parse et
    data = json.loads(event['body']) if isinstance(event.get('body'), str) else event
    
    # Eksik veri kontrolü
    if 'kaza_sayisi' not in data or 'saat' not in data or 'haftanin_gunu' not in data:
        return {
            'statusCode': 400,
            'body': json.dumps({'hata': 'Eksik veya hatalı parametre!'})
        }
    
    bucket = 'proje-3-veri-analizi'
    key = 'model.joblib'
    local_model_path = '/tmp/model.joblib'
    
    try:
        # Modeli S3'ten Lambda'nın geçici hafızasına indir
        s3.download_file(bucket, key, local_model_path)
        model = joblib.load(local_model_path)
        
        # Tahmin üret
        girdi = [[data['kaza_sayisi'], data['saat'], data['haftanin_gunu']]]
        tahmin = model.predict(girdi)[0]
        
        return {
            'statusCode': 200,
            'body': json.dumps({'beklenen_trafik_yogunlugu': round(tahmin, 2)})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'hata': str(e)})
        }