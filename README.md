![online](https://raw.githubusercontent.com/0kan87/online/refs/heads/main/screenshot.png)

Programı .exe olarak derleyeceğiz. 

Bu GUI uygulamasını exe'ye çevirmek için şu adımları izleyelim:

1. Önce gerekli kütüphaneleri yükleyin:
```bash
pip install PyQt5
pip install auto-py-to-exe
```

2. Programı exe'ye çevirmek için:
```bash
auto-py-to-exe
```

Bu komut bir arayüz açacak. Bu arayüzde:
1. "Script Location" kısmında Python dosyanızı seçin
2. "One File" seçeneğini işaretleyin
3. "Window Based" seçeneğini işaretleyin
4. "Convert" butonuna tıklayın

Yeni arayüzün özellikleri:
1. Başlat/Durdur düğmesi
2. Minimum ve maksimum bekleme süresi ayarı
3. Geri sayım göstergesi
4. Aktivite sayacı
5. Durum mesajları
6. Desteklenen uygulamalar listesi

Güvenlik özellikleri:
1. Fareyi sol üst köşeye götürerek programı durdurabilirsiniz
2. Programı kapatırken otomatik olarak aktiviteyi durdurur
3. Hata durumlarında güvenli çıkış yapar

İsterseniz .exe dosyasını oluşturduktan sonra, programı her Windows başlangıcında otomatik başlatmak için Windows'un Başlangıç klasörüne kısayolunu ekleyebilirsiniz:
1. Windows + R tuşlarına basın
2. `shell:startup` yazın
3. Oluşturduğunuz .exe dosyasının kısayolunu bu klasöre kopyalayın

Teams, Slack, WhatsApp Web, Telegram Web ve Discord gibi çoğu mesajlaşma uygulamasında çalışır çünkü hepsi benzer "aktivite algılama" sistemini kullanır.


Yeni özellikler:
1. Dakika:saniye formatında geri sayım eklendi
2. Desteklenen uygulamaların listesi eklendi
3. Aktivite sayacı eklendi (kaçıncı aktivite olduğunu gösterir)
4. Daha temiz ve detaylı ekran çıktısı

Önemli Notlar:
1. WhatsApp ve Telegram'ın masaüstü uygulamalarında çalışması web versiyonlarına göre daha tutarsız olabilir
2. Her uygulama farklı sürelerde "uzakta" durumuna geçer:
   - Teams: genelde 5 dakika
   - Slack: genelde 10 dakika
   - WhatsApp Web: genelde 15 dakika
   - Skype: genelde 5 dakika

Bu yüzden program 1-2 dakikada bir aktivite simüle ederek hepsini kapsıyor. İsterseniz `wait_time` değerlerini değiştirerek bekleme süresini artırabilir veya azaltabilirsiniz.
Evet, bu tür programlar maalesef virüs yazılımları tarafından yanlış pozitif (false positive) olarak algılanabiliyor. Bunun birkaç nedeni var:

Program mouse ve keyboard hareketlerini simüle ediyor
Sistem seviyesinde işlemler yapıyor
PyAutoGUI gibi otomasyon kütüphaneleri kullanıyor

Antivirüs programınıza göre güvenilir listeye ekleme adımları değişir. Windows Defender kullanıyorsanız, şu adımları izleyebilirsiniz:

1. Windows Defender'ı açmak için:
   - Windows + I (Ayarlar)
   - "Windows Güvenliği" -> "Virüs ve tehdit koruması"

2. "Virüs ve tehdit koruması ayarları" altında:
   - "Ayarları yönet" veya "Virüs ve tehdit koruması ayarları"na tıklayın
   - Aşağı kaydırarak "Dışlamalar" veya "Özel Durumlar"ı bulun
   - "Dışlama ekle veya kaldır"a tıklayın

3. Dışlama eklemek için:
   - "Dışlama Ekle" -> "Dosya"yı seçin
   - .exe dosyasının bulunduğu konuma gidin ve seçin

Ancak program silinmeden önce bu ayarları yapmanız gerekiyor. Şu adımları deneyebilirsiniz:

1. Önce Windows Defender'da dışlamayı ayarlayın
2. Windows Defender'ı geçici olarak kapatın
3. Programı yeniden derleyin/kurun
4. Dışlamayı ekleyin
5. Windows Defender'ı tekrar açın

Alternatif olarak, programı farklı bir klasöre (örneğin C:\Programs\ gibi) kurarak ve bu klasörü önceden güvenilir listeye ekleyerek de deneyebilirsiniz.
