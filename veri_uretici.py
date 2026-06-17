import pandas as pd
import numpy as np
from pymongo import MongoClient
from datetime import datetime, timedelta

# 1. Sentetik Veri Üretimi
np.random.seed(42)
tarihler = [datetime(2026, 1, 1) + timedelta(hours=i) for i in range(1000)]
kaza_sayisi = np.random.poisson(lam=1.2, size=1000)
trafik_yogunlugu = np.clip(30 + kaza_sayisi * 15 + np.random.normal(0, 10, 1000), 10, 100)

df = pd.DataFrame({
    "tarih": tarihler,
    "kaza_sayisi": kaza_sayisi,
    "trafik_yogunlugu": trafik_yogunlugu.astype(int)
})

# 2. MongoDB'ye Aktarım
client = MongoClient("mongodb+srv://erdemfurkan534_db_user:YHE3HCLu45dPLAa1@cluster0.4x7xivl.mongodb.net/?appName=Cluster0")
db = client["trafik_analitigi"]
collection = db["kaza_verileri"]

veri_sozlugu = df.to_dict(orient="records")
collection.insert_many(veri_sozlugu)
print("Veriler MongoDB'ye başarıyla yüklendi!")