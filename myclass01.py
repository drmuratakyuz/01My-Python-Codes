class Ogrenci:
    'Tüm öğrenciler için temel sınıf'
    Ogrenci_sayisi = 0
    
    def __init__(self, adi, numarasi):
        self.adi = adi
        self.numarasi = numarasi
        Ogrenci.Ogrenci_sayisi += 1
        
    def OgrenciSayisiGoster(self):
        print("Toplam öğrenci: %d" % Ogrenci.Ogrenci_sayisi)

    def OgrenciGoster(self):
        print("Adi : ", self.adi,  ", Numarası: ", self.numarasi)
        
ogr1 = Ogrenci("Öğrenci1", 1000)
ogr2 = Ogrenci("Öğrenci2", 2000)
ogr3 = Ogrenci("Öğrenci3", 3000)

ogr1.OgrenciGoster()
ogr2.OgrenciGoster()
ogr3.OgrenciGoster()
print("Toplam öğrenci %d" % Ogrenci.Ogrenci_sayisi)

ogr1.yas = 15 #ilk defa değişken oluşturma
print(ogr1.yas)
ogr1.yas = 16 #değişkeni değiştirme
print(ogr1.yas)
#del ogr1.yas #değişkeni bellekten çıkarma
#print(ogr1.yas)

print("Ogrenci.__doc__:", Ogrenci.__doc__)
print("Ogrenci.__name__:", Ogrenci.__name__)
print("Ogrenci.__module__:", Ogrenci.__module__)
print("Ogrenci.__bases__:", Ogrenci.__bases__)
print("Ogrenci.__dict__:", Ogrenci.__dict__)