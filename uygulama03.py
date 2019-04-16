print(">> Adam Asmaca Oyunu Başlıyor, İyi Şanslar."
      "<<\n>> Oyunda Sorulacak Sözcükler 'Yemek' adlarından Oluşmaktadır."
      "<<\n>> Her Bir '_' Sembolü Bir Harfi İçermektedir. <<")
from random import choice
while True:
    kelime = choice (["imambayıldı", "dolma", "menemen", "sarma", "makarna", "kızartma", "içliköfte", "mantı"])
    kelime = kelime.upper()
    harfsayisi = len(kelime)
    print("Kelimemiz {} harfden oluşuyor.\n".format(harfsayisi))
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
            print("Bildiniz. Tebrikler!!")
            break
        print("Kelimeyi Tahmin Ediniz", bos)
        print(KalanCan, "Canınız Kaldı")
        Tahmin = input("Bir Harf Giriniz >>>>")
        Tahmin = Tahmin.upper()
        if Tahmin == kelime:
            print("\n\nBildiniz. Tebrikler\n\n")
            break
        if Tahmin in tahminler or Tahmin in hata:
            print("{} Bu Harf Daha Önce Girildi. Lütfen Başka Bir Harf Giriniz. ".format(Tahmin))
        elif Tahmin in kelime:
            rpt = kelime.count(Tahmin)
            print("Bildiniz.{0} Harfi Kelime İçerisinde Mevcut {1} Kere Geçiyor".format(Tahmin, rpt))
            tahminler.append(Tahmin)
        else:
            print("Harfiniz Doğru Değil. Bu Harf Kelimede Bulunmuyor.")
            hata.append(Tahmin)
            KalanCan = KalanCan - 1
    if KalanCan == 0:
        print("\n\nHiç Canınız Kalmadı. Tahmin Edemediniz.")
        print("Kelimemiz {}\n\n".format(kelime))
    print("Oyundan Çıkmak İstiyorsanız\n'Ç' Tuşuna Basın\nDevam Etmek İstiyorsanız Herhangi Bir Tuşa Basın. ")
    devam = input(">>>>")
    devam = devam.upper()
    if devam == "Ç":
        break
    else:
        continue
    input()  # Dikkat, Bu Satır programın kapanmamasını sağlayacak.
