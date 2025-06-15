import pandas as pd
import string
import nltk
import re

# İlk kez çalıştırırken aşağıdakini aktif et
nltk.download('stopwords')
from nltk.corpus import stopwords

# Türkçe stopword listesi
stop_words = set(stopwords.words('turkish'))

# CSV dosyasını oku (başlıklı)
df = pd.read_csv("mail_data.csv")

# [Çeviri Hatası] içeren satırları kaldır
df = df[~df["text"].str.contains("Çeviri Hatası", na=False)]

# Küçük harfe çevir
df["text"] = df["text"].str.lower()

# Noktalama işaretlerini sil
df["text"] = df["text"].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)))

# Sayıları sil
df["text"] = df["text"].apply(lambda x: re.sub(r'\d+', '', x))

# Stopword temizliği
df["text"] = df["text"].apply(lambda x: ' '.join([kelime for kelime in x.split() if kelime not in stop_words]))

# Boş veya çok kısa kalan satırları sil
df = df[df["text"].str.strip().str.len() > 5]

# Temiz veri dosyasını kaydet
df.to_csv("temizlenmis_veri_english.csv", index=False)
