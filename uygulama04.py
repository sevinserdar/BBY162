#uygulama1
text = ("Açık bilim, araştırma çıktılarına ve süreçlerine herkesin serbestçe erişmesini, bunların ortak kullanımını, dağıtımını ve üretimini kolaylaştıran bilim uygulamasıdır.")
slices = text[:20]
print(slices)

#uygulama2
liste = ["Açık Bilim", "Açık Erişim", "Açık Lisans", "Açık Eğitim", "Açık Veri", "Açık Kültür"]
for i in liste:
    print(i)

#uygulama3
sozluk = {"elma" : "Ağaçta yetişen bir tür meyve" , "salatalık" : "Fidan üzerinde büyüyen bir tür sebze" }
bul = input("Bulmak istediğiniz kelimeyi giriniz:")
print("Lütfen, küçük harf giriniz.")
while True:
    if bul == "elma":
        print(sozluk["elma"])
        break
    elif bul == "salatalık":
        print(sozluk["salatalık"])
        break
    else:
        print("yanlış giriş")
        break




