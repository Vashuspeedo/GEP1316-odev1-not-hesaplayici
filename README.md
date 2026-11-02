# Öğrenci Not Hesaplayıcı

## Proje Hakkında
Öğrenci Not Hesaplayıcı, Python programlama dili kullanılarak geliştirilmiş, komut satırı üzerinden çalışan başlangıç seviyesi bir not hesaplama uygulamasıdır.

Program, öğrencilerin vize ve final notlarını girerek ağırlıklı not ortalamalarını hesaplamalarını, harf notlarını öğrenmelerini ve dersten geçme veya kalma durumlarını görmelerini sağlar.

## Özellikler
- Öğrenci adı ve ders adı ekleme
- Vize ve final notlarını girme
- Notların 0 ile 100 arasında olup olmadığını kontrol etme
- Vize ve final sınavlarının yüzde ağırlıklarını belirleme
- Ağırlıklı not ortalamasını hesaplama
- Otomatik harf notu belirleme
- Geçme ve kalma durumunu gösterme
- Kayıtlı öğrencileri listeleme
- Sonuçları TXT ve CSV dosyalarına kaydetme

## Kullanılan Teknolojiler
- Python 3
- CSV modülü
- Gemini
- Gifthub Copilot

## Program Nasıl Çalıştırılır?

1. Proje dosyalarını bilgisayarınıza indirin.
2. Proje klasörünü Visual Studio Code ile açın.
3. Terminal bölümünü açın.
4. Aşağıdaki komutu çalıştırın:

```bash
python main.py
```

## Notlandırma Sistemi

| Not Ortalaması | Harf Notu |
|---|---|
| 90–100 | AA |
| 85–89 | BA |
| 80–84 | BB |
| 75–79 | CB |
| 70–74 | CC |
| 65–69 | DC |
| 60–64 | DD |
| 50–59 | FD |
| 0–49 | FF |

50 ve üzerindeki ortalamalar başarılı, 50'nin altındaki ortalamalar başarısız olarak değerlendirilir.

*Not: Kullanılan notlandırma sistemi örnek olarak belirlenmiştir. Üniversitelerin notlandırma kurallarına göre değiştirilebilir.*

## Dosya Yapısı

```text
Ogrenci_Not_Hesaplayici/
│
├── main.py
├── README.md
├── ogrenci_raporu.txt
└── ogrenci_raporu.csv
```

## Çıktı Dosyaları
Program, öğrenci sonuçlarını iki farklı formatta kaydedebilir:

- `ogrenci_raporu.txt`: Öğrenci sonuçlarını metin dosyası olarak saklar.
- `ogrenci_raporu.csv`: Öğrenci sonuçlarını tablo formatında saklar ve Excel ile açılabilir.

## Projenin Amacı
Bu projenin amacı, Python programlama dilinin temel konularını uygulamalı olarak öğrenmek ve kullanmaktır. Proje kapsamında fonksiyonlar, döngüler, koşullu ifadeler, listeler, sözlükler, veri doğrulama ve dosya işlemleri kullanılmıştır.

## Proje Bilgileri
**Ders:** GEP1316 – Kodlama Okuryazarlığı  
**Proje:** Öğrenci Not Hesaplayıcı  
**Dönem:** 2026–2027 Güz
