import pandas as pd
from deep_translator import GoogleTranslator
import numpy as np

# === 1. VERİYİ YÜKLE ===
input_file = "dataset6.csv"   # <- kendi dosya adını buraya yaz
df = pd.read_csv(input_file)

# === 2. ÇEVİRİ FONKSİYONU ===
def translate_text(text):
    try:
        return GoogleTranslator(source='en', target='tr').translate(text)
    except:
        return "[Çeviri Hatası]"

# === 3. BÜYÜK VERİ İÇİN PARÇALAMA ===
chunks = np.array_split(df, 10)  # 10 parçaya böldük
translated_chunks = []

for i, chunk in enumerate(chunks):
    print(f"Parça {i+1}/{len(chunks)} çeviriliyor...")
    chunk['text'] = chunk['text'].apply(translate_text)  # İngilizce yerine Türkçeyi yaz
    translated_chunks.append(chunk)

# === 4. PARÇALARI BİRLEŞTİR VE KAYDET ===
df_translated = pd.concat(translated_chunks)
output_file = "dataset_translated_tr6.csv"
df_translated.to_csv(output_file, index=False)

print(f"Tercüme tamamlandı. Kaydedilen dosya: {output_file}")

