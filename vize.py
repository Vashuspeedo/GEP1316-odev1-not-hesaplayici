import os

# 1. Fonksiyon
def harf_notu_hesapla(vize, final):
    """Vize (%40) ve Final (%60) notlarına göre ortalama ve harf notunu hesaplar."""
    ortalama = (vize * 0.4) + (final * 0.6)
    
    # if/elif/else kullanımı
    if ortalama >= 90:
        harf = "AA"
    elif ortalama >= 85:
        harf = "BA"
    elif ortalama >= 80:
        harf = "BB"
    elif ortalama >= 70:
        harf = "CB"
    elif ortalama >= 60:
        harf = "CC"
    elif ortalama >= 50:
        harf = "DC"
    else:
        harf = "FF"
        
    return round(ortalama, 2), harf

# 2. Fonksiyon
def gecerli_not_al(mesaj):
    """Kullanıcıdan 0-100 arası geçerli bir sayısal değer alır, hatalarda çökmez."""
    # GEREKSİNİM 3: En az 1 döngü kullanımı (1. Döngü - Hata kontrolü)
    while True:
        try:
            # GEREKSİNİM 1: Girdi alma ve doğrulama
            deger = float(input(mesaj))
            if 0 <= deger <= 100:
                return deger
            else:
                print("⚠️ Hata: Not değeri 0 ile 100 arasında olmalıdır!")
        except ValueError:
            print("⚠️ Hata: Lütfen geçerli bir sayı giriniz! (Harf veya boşluk kullanmayın)")

# 3. Fonksiyon
def verileri_kaydet(ogrenci_sozlugu, dosya_adi="ogrenci_notlari.csv"):
    """Öğrenci verilerini bir CSV dosyasına kaydeder."""
    # GEREKSİNİM 6: Sonuçların bir metin dosyasına (.txt veya .csv) kaydedilmesi
    with open(dosya_adi, "w", encoding="utf-8") as dosya:
        dosya.write("OgrenciNo,Vize,Final,Ortalama,HarfNotu\n")
        for no, veriler in ogrenci_sozlugu.items():
            satir = f"{no},{veriler['vize']},{veriler['final']},{veriler['ortalama']},{veriler['harf']}\n"
            dosya.write(satir)
    print(f"\n✅ Başarılı: Veriler '{dosya_adi}' dosyasına kaydedildi.")

def ana_program():
    # GEREKSİNİM 5: Bir liste veya sözlük kullanımı
    ogrenciler = {} 
    
    # Menü döngüsü
    while True:
        print("\n--- ÖĞRENCİ NOT DEĞERLENDİRME SİSTEMİ ---")
        print("1. Yeni Öğrenci Notu Gir")
        print("2. Kayıtlı Öğrencileri Görüntüle")
        print("3. Verileri Kaydet ve Çıkış Yap")
        
        # Girdi alma
        secim = input("Lütfen yapmak istediğiniz işlemi seçin (1/2/3): ")
        
        if secim == '1':
            ogrenci_no = input("Öğrenci Numarası (Örn: 2026001): ").strip()
            if not ogrenci_no:
                print("⚠️ Hata: Öğrenci numarası boş bırakılamaz.")
                continue
                
            vize_notu = gecerli_not_al(f"{ogrenci_no} numaralı öğrencinin Vize notunu girin: ")
            final_notu = gecerli_not_al(f"{ogrenci_no} numaralı öğrencinin Final notunu girin: ")
            
            ortalama, harf = harf_notu_hesapla(vize_notu, final_notu)
            
            # Sözlüğe veri ekleme
            ogrenciler[ogrenci_no] = {
                "vize": vize_notu,
                "final": final_notu,
                "ortalama": ortalama,
                "harf": harf
            }
            # Sonuçların yazımı
            print(f"👉 {ogrenci_no} için Ortalama: {ortalama} | Harf Notu: {harf}")

        elif secim == '2':
            if not ogrenciler:
                print("\n⚠️ Henüz sisteme girilmiş bir öğrenci notu bulunmamaktadır.")
            else:
                print("\n--- KAYITLI ÖĞRENCİLER ---")
                for no, veri in ogrenciler.items():
                    print(f"Öğrenci No: {no} | Vize: {veri['vize']} | Final: {veri['final']} | Ort: {veri['ortalama']} | Harf: {veri['harf']}")
                    
        elif secim == '3':
            if ogrenciler:
                verileri_kaydet(ogrenciler)
            print("Sistemden çıkılıyor. İyi günler!")
            break
            
        else:
            print("⚠️ Hata: Geçersiz bir seçim yaptınız. Lütfen 1, 2 veya 3 tuşlayın.")

# Programı doğrudan çalıştır
if __name__ == "__main__":
    ana_program()