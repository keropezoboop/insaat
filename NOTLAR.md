# Ozan İskender konsept sitesi: notlar

**Gizli önizleme linki:** https://claude.ai/artifact/2trghWfNELNLhKGhCxbAAN (sadece Kerem açabilir; Ozan'a göstermek için Share menüsünden erişim verilmeli)
**Kod:** `keropezoboop/insaat`, dal `claude/confident-ptolemy-ql4y5v`. Ham videolar `videolar` dalında, `kaynak/` klasöründe.

### Önizleme linkini güncelleme (yeni oturum için)
- Kaynak `index.html`. Artifact sürümü bundan üretiliyor: `<html>/<head>/<body>` etiketleri çıkarılır; en üste `<title>Ozan İskender Konsepti</title>`, Google Fonts `<link>`leri ve `<style>` (`:root`'a `color-scheme: dark` eklenir) konur; ardından `<script>document.body.classList.add('loading');</script>` ve body içeriği gelir.
- Yayınlarken `url` olarak yukarıdaki linki ver (yoksa yeni bir link oluşur). Sayfanın kullandığı `img/` ve `video/` dosyalarını `files` ile aynı yollarla gönder. Tek dosya sınırı 15 MB.
- Her değişiklikten sonra hem GitHub'a gönder hem linki güncelle.

## Tasarım kararları
- Eksper sitesine benzememeli (Ozan Eksper'i gördü). Referans: **Douglas Elliman**. Ayrıca Function (süreç kartları fikri), Snøhetta (üstüne gelince fotoğraf önizlemesi), MVRDV (dar kalın büyük harfler, bölüm noktaları).
- Koyu grafit zemin, pas turuncusu vurgu. Başlıklar **Jost ince, büyük harf, geniş aralıklı** (Elliman sakinliği). Kalın dar Barlow Condensed yalnızca 2. ekrandaki PLANLA / İNŞA ET / TESLİM ET kelimelerinde, tek vurgu olarak. IBM Plex Mono küçük etiketler. Butonlar yuvarlak kenarlı (Elliman). Açık renkli bölüm yok (renk geçişi istenmedi).
- Açılış videosunda geçişler düz kesme (üst üste binen geçişler bulanık görünüyordu). Döngü ~12 sn, siyaha kararma yok.
- Şantiye satırı Elliman ilan satırı gibi: `İLÇE | — KAT | — DAİRE | AŞAMA` (değerler Ozan'dan gelecek).
- Akış: açılış animasyonu (siyah ekranda isim) → **1. ekran:** Bursa drone montajı (Uludağ, gündüz şehir, akşam sahil), altta tek satır slogan → **2. ekran:** gece binası videosu, üstünde kendiliğinden değişen kelimeler PLANLA / İNŞA ET / TESLİM ET → Aşamalar (Temel, Kaba, İnce, Teslim; üst üste kayan tam ekranlar) → Hizmetler (liste, üstüne gelince fotoğraf) → Şantiyeler (liste) → İletişim.
- Kaldırılanlar: hikâye bölümü ("tüm inşaatçıların hikâyesi aynı"), "Nasıl çalışıyoruz" kartları, kayan turuncu şerit.

## Yapılacaklar
- [ ] 2. ekran için gerçek bir **inşaat videosu** (vinç, beton dökümü, demir bağlama). Şu an gece binası çekimi var.
- [ ] Gündüz Bursa videosunun 4K hali bulunursa değiştir (şu an 1080p kaynak).
- [ ] BIG'e tekrar bak: şantiye listesi için her projeye küçük simge fikri.
- [ ] Zaha (zha.com) açılışı: Kerem gördüğünü anlatacak / ekran kaydı atacak.
- [ ] Stok fotoğrafları Ozan'ın gerçek şantiye fotoğraflarıyla değiştir.

## Ozan'dan öğrenilecekler (doğrulanmadan siteye yazılmayacak)
1. Firma adı, logo
2. Tam olarak hangi hizmetleri veriyor (statik proje, fenni mesuliyet, şantiye şefliği, uygulama...). Sitedeki hizmet listesi tahmin, "taslak" diye işaretli.
3. 3 şantiyenin adı, yeri, türü, aşaması. Sitede yer tutucu.
4. Telefon numarası. Sitede `05XX XXX XX XX`.
5. Şantiye fotoğrafları ve videoları.

## Kurallar
- Uydurma bilgi, rakam, yorum yok; yer tutucular açıkça işaretli.
- Site herkese açık yayınlanmayacak (repo da Private yapılmalı).
