import json
from sozluk import yanit_ver
import tkinter as tk
from tkinter import scrolledtext
import time

MAX_MESAJ = 10  # Maksimum mesaj sayısı
mesaj_sayisi = 0  # Mevcut mesaj sayısını tutacak sayaç
yaziyor_mesaji = None  # "BasicAI yazıyor..." mesajını takip etmek için

def karakter_karakter_yaz(metin, index=0):
    """Metni karakter karakter yazdırır"""
    if index < len(metin):
        sohbet_alani.config(state=tk.NORMAL)
        sohbet_alani.insert(tk.END, metin[index])
        sohbet_alani.see(tk.END)
        sohbet_alani.config(state=tk.DISABLED)
        # Bir sonraki karakteri yazdırmak için zamanlayıcı kur
        # Rastgele bir gecikme ile daha doğal görünüm sağla
        pencere.after(50, karakter_karakter_yaz, metin, index + 1)

def yaziyor_goster():
    """'BasicAI yazıyor...' mesajını gösterir"""
    global yaziyor_mesaji
    sohbet_alani.config(state=tk.NORMAL)
    yaziyor_mesaji = "●\n"
    sohbet_alani.insert(tk.END, yaziyor_mesaji)
    sohbet_alani.see(tk.END)
    sohbet_alani.config(state=tk.DISABLED)

def yaziyor_kaldir():
    """'BasicAI yazıyor...' mesajını kaldırır"""
    global yaziyor_mesaji
    if yaziyor_mesaji:
        sohbet_alani.config(state=tk.NORMAL)
        # Son satırı sil
        sohbet_alani.delete("end-2c linestart", "end")
        sohbet_alani.config(state=tk.DISABLED)
        yaziyor_mesaji = None

def mesaj_gonder():
    global mesaj_sayisi
    mesaj = kullanici_girdisi.get()
    
    if mesaj_sayisi >= MAX_MESAJ:
        sohbet_guncelle("Mesaj limitiniz doldu. Yeni bir sohbete başlamaya ne dersiniz?")
        kullanici_girdisi.config(state=tk.DISABLED)
    else:
        # Önce kullanıcı mesajını normal şekilde göster
        sohbet_guncelle(f"\nKullanıcı: {mesaj}\n")
        kullanici_girdisi.delete(0, tk.END)
        
        # "BasicAI yazıyor..." mesajını göster
        yaziyor_goster()
        
        # Bot yanıtını al
        bot_yanit = yanit_ver(mesaj)
        
        # Kısa bir gecikme sonra "yazıyor..." mesajını kaldır
        pencere.after(1000, yaziyor_kaldir)
        
        # Ve bot yanıtını karakter karakter yazdırmaya başla
        pencere.after(1200, lambda: karakter_karakter_yaz(f"\nBasicAI: {bot_yanit}"))
        
        mesaj_sayisi += 1

def sohbet_guncelle(mesaj):
    sohbet_alani.config(state=tk.NORMAL)
    sohbet_alani.insert(tk.END, mesaj)
    sohbet_alani.see(tk.END)
    sohbet_alani.config(state=tk.DISABLED)

# Ana pencere
pencere = tk.Tk()
pencere.title("BasicAI")
pencere.geometry("600x400")

# Sohbet alanı
sohbet_alani = scrolledtext.ScrolledText(pencere, wrap=tk.WORD, width=60, height=20, font=("Arial", 10))
sohbet_alani.pack(pady=10)
sohbet_alani.config(state=tk.DISABLED)

# Kullanıcı girdisi alanı
kullanici_girdisi = tk.Entry(pencere, width=50, font=("Arial", 12))
kullanici_girdisi.pack(pady=10)

# Mesaj gönderme işlevini Enter tuşuna bağla
pencere.bind("<Return>", lambda event: mesaj_gonder())

# Pencereyi çalıştır
pencere.mainloop()
