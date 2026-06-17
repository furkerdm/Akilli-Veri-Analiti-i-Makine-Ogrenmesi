import pandas as pd
from pymongo import MongoClient
from sklearn.ensemble import RandomForestRegressor
import joblib

# MongoDB bağlantı bilgilerinizi girmeyi unutmayın
client = MongoClient("MONGO_CREDENTIALS")
db = client["trafik_analitigi"]
df = pd.DataFrame(list(db["kaza_verileri"].find({}, {"_id": 0})))

df['saat'] = pd.to_datetime(df['tarih']).dt.hour
df['haftanin_gunu'] = pd.to_datetime(df['tarih']).dt.dayofweek
X = df[['kaza_sayisi', 'saat', 'haftanin_gunu']]
y = df['trafik_yogunlugu']

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

joblib.dump(model, "model.joblib")
print("model.joblib dosyası klasörünüze başarıyla oluşturuldu!")

