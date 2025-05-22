import tkinter as tk
from datetime import datetime
from model_loader import load_model

# 📌 Kullanıcı adı 
kullanici_adi = "Kullanıcı"

# 🧠 Modeli Hugging Face'ten yükle
print("🔄 Model yükleniyor, lütfen bekleyin...")
pipeline = load_model()
print("✅ Model yüklendi.")

# Etiket dönüşüm tablosu
etiket_yorum = {
    "LABEL_0": "✅ Bu mail SPAM DEĞİLDİR.",
    "LABEL_1": "⚠️ DİKKAT: Bu bir SPAM mail olabilir!"
}

# Tahmin fonksiyonu
def tahmin_et(event=None):
    metin = giris_alani.get("1.0", tk.END).strip()
    if not metin:
        return

    tahmin = pipeline(metin)[0]
    etiket = etiket_yorum.get(tahmin["label"], tahmin["label"])
    skor = round(tahmin["score"], 3)
    saat = datetime.now().strftime("%H:%M:%S")

    sohbet_penceresi.config(state=tk.NORMAL)
    sohbet_penceresi.insert(tk.END, f"\n🕒 {saat}\n👤 {kullanici_adi}:\n{metin}\n\n", "kullanici")
    sohbet_penceresi.insert(tk.END, f"🤖 Chatbot:\n{etiket} (Güven: {skor})\n", "chatbot")
    sohbet_penceresi.insert(tk.END, "-"*60 + "\n", "ayrac")
    sohbet_penceresi.config(state=tk.DISABLED)
    sohbet_penceresi.see(tk.END)

    giris_alani.delete("1.0", tk.END)

# Ana pencere
pencere = tk.Tk()
pencere.title("📧 Spam Mail Tespit Chatbot")
pencere.geometry("700x800")
pencere.configure(bg="#1e1e1e")

# Başlık
baslik = tk.Label(pencere, text="Spam Mail Tespit Chatbot", bg="#1e1e1e", fg="#00ffcc", font=("Arial", 18, "bold"))
baslik.pack(pady=10)

# Sohbet alanı
sohbet_penceresi = tk.Text(pencere, height=25, width=80, state=tk.DISABLED, bg="#2e2e2e", fg="#ffffff", font=("Consolas", 12))
sohbet_penceresi.tag_configure("kullanici", foreground="#00ffcc", font=("Consolas", 12, "bold"))
sohbet_penceresi.tag_configure("chatbot", foreground="#ffcc00", font=("Consolas", 12))
sohbet_penceresi.tag_configure("ayrac", foreground="#555555")
sohbet_penceresi.pack(padx=20, pady=10)

# Giriş kutusu
giris_alani = tk.Text(pencere, height=4, width=70, bg="#333333", fg="#ffffff", font=("Arial", 12))
giris_alani.pack(padx=20, pady=(0, 5))

# Gönder butonu
buton = tk.Button(pencere, text="Gönder", command=tahmin_et, bg="#00ffcc", fg="#000000", font=("Arial", 12, "bold"))
buton.pack(pady=(0, 20))

# Klavyeden Enter tuşuna basıldığında tahmin çalışsın
pencere.bind("<Return>", tahmin_et)

# Uygulama başlat
pencere.mainloop()
