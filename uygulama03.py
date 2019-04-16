print['Adam Asmaca Oyununa Hoşgeldiniz.',\
      'Bu Oyunda Sorulan Kelimeler Şehir İsimlerinden Oluşmaktadır.',\
      'Her Bir *_*Sembolü Bir Harfi Temsil Etmektedir.']
from random import choice
while True:
    kelime = choice (["ankara", "tekirdağ", "sivas", "kars", "lüleburgaz", "adana", "bursa", "tokat"])
    kelime = kelime.upper()
    harfsayisi = len(kelime)
    print("Kelimemiz {} harflidir.\n".format(harfsayisi))
    tahminler = []
    hata = []
    KalanCan = 5
    while KalanCan > 0:
        bos = ""
        for girilenharf in kelime:
            if girilenharf in tahminler:
                bos = bos + girilenharf
            else:
                bos = bos + " _ "
        if bos == kelime:
            print("Kelimeyi Doğru Bildiniz. Tebrikler!!")
            break
        print("Kelimeyi Tahmin Ediniz", bos)
        print(KalanCan, "Canınız Kaldı")
        Tahmin = input("Bir Harf Giriniz >>>>")
        Tahmin = Tahmin.upper()
        if Tahmin == kelime:
            print("\n\nDoğru Bildiniz. Tebrikler\n\n")
            break
        if Tahmin in tahminler or Tahmin in hata:
            print("{} Daha Önce Söylendi. Lütfen Başka Bir Harf Söyleyin. ".format(Tahmin))
        elif Tahmin in kelime:
            rpt = kelime.count(Tahmin)
            print("Dogru.{0} Harfi Kelimemiz İçerisinde {1} Kere Geçiyor".format(Tahmin, rpt))
            tahminler.append(Tahmin)
        else:
            print("Maalesef Yanlış. Kelimede Böyle Bir Harf Geçmiyor.")
            hata.append(Tahmin)
            KalanCan = KalanCan - 1
    if KalanCan == 0:
        print("\n\nHiç Hakkınız Kalmadı. Maalesef Bilemediniz.")
        print("Kelimemiz {}\n\n".format(kelime))
    print("Oyundan Çıkmak İstiyorsanız\n'H' Tuşuna Basınız\nDevam Etmek İçin Başka Bir Tuşa Basınız. ")
    devam = input(">>>>")
    devam = devam.upper()
    if devam == "H":
        break
    else:
        continue
