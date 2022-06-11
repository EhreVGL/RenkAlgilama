# Renk Algilama - Python Uygulaması

## Herkese Selamlar

Bu proje, Python ile görüntü işleme çalışmalarına başladığımda yaptığım ilk projem. 

Bu projeyi yapmamdaki amaç; OpenCV kütüphanesini kullanarak kamera görüntüsündeki renkleri ayırt etmekti. 

İlk projem olduğu için -teknik açıdan- renk algılamada kullanılan maskenin daha doğru bir sonuç oluşturmasında yardımcı olan metodlar bu projede şu anlık eksik. İlerleyen zamanlarda kodları bu yönde geliştirmeyi planlıyorum.

## İçindekiler

0. [Herkese Selamlar](#herkese-selamlar)
1. [Uygulama Hakkında](#uygulama-hakkında)
2. [Yüklenmesi Gereken Kütüphaneler](#yuklenmesi-gereken-kutuphaneler)
3. [Eklenecek veya Düzenlenecek Kısımlar](#eklenecek-veya-duzenlenecek-kısımlar)
4. [Youtube Linki](#youtube-linki)

## Uygulama Hakkında

Uygulama çalıştırıldığı andan itibaren kamera görüntüsü yeni bir pencerede gösterilir. Kırmızı, yeşil, mavi ve sarı renkler için ayrı filtreleme uygulanır ve her bir filtrenin sonucu kamera görüntüsüyle eş zamanlı olarak farklı ekranlarda yansıtılır. ESC tuşuna basıldığında uygulama kapanır.


Laptop kamera görüntüsü aşağıdaki kod parçacığındaki **VideoCapture(0)** ile alınmaktadır. Başka bir kamera eklemek isterseniz 0 değerini değiştirmeniz gerekir. Uygulama çalıştırıldığın da kamera açılmazsa kameranızın ulaşılabilirliğinin açık olduğundan emin olun.

```
cap = cv2.VideoCapture(0)

```

## Yuklenmesi Gereken Kutuphaneler

- Opencv kütüphanesi

```
pip install opencv-python

```
- Numpy kütüphanesi

```
pip install numpy

```

## Eklenecek veya Duzenlenecek Kısımlar

-Renk algılama methodları ile renklerin maskeleri daha gerçekçi hale getirilecek.

## Youtube Linki

Youtube üzerinden paylaştığım uygulama videosuna [bu linkten](https://youtu.be/euDfPq38dig) ulaşabilirsiniz.
