# YOLO ve ByteTrack ile Araç Takibi

Bu proje, YOLOv8 modeli ve ByteTrack algoritması kullanarak bir videodaki araçları tespit edip takip etmeyi amaçlamaktadır. Bu belgede, projenin adımlarını, kullanılan araçları, kodu ve sonuçları bulabilirsiniz.

## Proje Amacı

Bu projenin amacı, araçların yoğun olduğu bir videoda araçları tespit edip takip etmek ve bu araçların sayısını belirlemektir. Bu, trafik analizi, güvenlik ve gözetim gibi uygulamalar için önemli bir adımdır.

## Gereksinimler

Projenin çalışması için aşağıdaki yazılım ve kütüphanelere ihtiyaç vardır:

- **Python 3.x:** Projenin ana programlama dili.
- **OpenCV:** Görüntü işleme kütüphanesi.
- **Ultralytics YOLOv8:** YOLO modelinin en son versiyonu.

### Kütüphanelerin Kurulumu

Gerekli kütüphaneleri kurmak için aşağıdaki komutları kullanabilirsiniz:

```bash
pip install opencv-python
pip install ultralytics
