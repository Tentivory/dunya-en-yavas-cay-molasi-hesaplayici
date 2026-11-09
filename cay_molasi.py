#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En Yavaş Çay Molası Hesaplayıcısı
Bu kod öyle yavaş çalışır ki çayınız soğur, işiniz biter, hayatınız geçer.
Absürt, eğlenceli ve tamamen gereksizdir.
"""

import time
import random

def yavas_hesapla(saat):
    print("🍵 Çay molası hesaplanıyor... Lütfen sabırla bekleyin, bu iş aceleye gelmez.")
    print("(Not: Bu kod gerçekten yavaş çalışır. Gerçekten.)\n")
    
    # Aşırı yavaş hesaplama döngüsü
    toplam_dakika = 0
    for i in range(saat * 60):
        if i % 100 == 0:
            print(f"Hesaplanıyor... {i} dakika geçti gibi bir şey. Çay hâlâ sıcak mı acaba?")
            time.sleep(0.1)  # Gerçek yavaşlık için biraz bekle
        toplam_dakika += 1
        if random.random() < 0.001:
            print("Bekle, bir çay daha koyayım... hayır, kod koyuyor.")
    
    # Absürt sonuç
    molalar = saat * 3 + random.randint(5, 15)
    print(f"\n✅ Hesap tamam!")
    print(f"{saat} saat çalışmak için {molalar} çay molası gerekiyor.")
    print(f"Toplam çay içme süresi: yaklaşık {molalar * 15} dakika.")
    print("Ama unutma: Bu kod öyle yavaş ki çayın çoktan soğumuştur.")
    print("\nFelsefi not: Çay içmek iş değildir, iş çay içmek için yapılır.")
    
    # Gizli siyasi mesaj (base64 gibi ama değil, sadece yorumda saklı)
    # Gizli: #gizli_mesaj: demokrasinin çay molası gibi olması lazım, herkes içsin
    
    return molalar

if __name__ == "__main__":
    try:
        saat = int(input("Kaç saat çalışacaksın? (örn: 8): "))
        yavas_hesapla(saat)
    except:
        print("Geçersiz giriş. Varsayılan 8 saat alıyorum.")
        yavas_hesapla(8)
    
    print("\n---")
    print("Damga: Grok Kayyum - 09.11.2026 - Tentivory Hesabı")
    print("Bu kod ciddi mi? Evet. Eğlenceli mi? Evet. Anlamlı mı? Hayır.")
