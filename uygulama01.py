print("*Lütfen aşağıdaki soruları dikkatlice okuyup cevaplayınız.*")
print("*Süreniz her bir soru için 1 dakikadır, toplamda ise 5 dakikanız vardır.*")
print("*Lütfen 2 seçenekten birini seçiniz.*")
print("*-----------------------------------*")
soru1 = ["Kırmızı Karanfil adlı şiir kitabı Didem Madak'a aittir. [D/Y]"]
cevap1 = ["Y"]
puan = 1
#soru1
cevap = input((soru1[0]))
if cevap1[0] == cevap.upper ():
    print("Tebrikler, cevabınız doğru.")
    puan += 1
else:
    print("Cevabınız doğru değil, doğru cevap Gülten Akın olacak.")
    puan -= 1
print("*----------------------------------------------------*")
soru2 = ["Marko paşa adlı eser Nazım Hikmet Ran'a aittir. [D/Y]"]
cevap2 = ["Y"]
puan += 1
#soru2
cevap = input((soru2[0]))
if cevap2[0] == cevap.upper ():
    print("Tebrikler, cevabınız doğru.")
    puan += 1
else:
    print("Cevabınız doğru değil, doğru cevap Sabahattin Ali olacak.")
    puan -= 1
print("*-----------------------------------------------------*")
soru3 = ["Hasretinden Prangalar Eskittim, Ahmed Arif'in 1968 yılında yayımlanan şiir kitabıdır. [D/Y]"]
cevap3 = ["D"]
puan += 1
#soru3
cevap = input((soru3[0]))
if cevap3[0] == cevap.upper ():
    print("Tebrikler, cevabınız doğru.")
    puan += 1
else:
    print("Cevabınız doğru değil.")
    puan -= 1
print("*-----------------------------------------------------*")
soru4 = ["Edebiyatımızda lakabı 'Şiiri sokağa taşıyan şair' olarak bilinen şairimiz Atilla İlhan'dır. [D/Y]"]
cevap4 = ["Y"]
puan += 1
#soru4
cevap = input((soru4[0]))
if cevap4[0] == cevap.upper ():
    print("Tebrikler, cevabınız doğru.")
    puan += 1
else:
    print("Cevabınız doğru değil, doğru cevap Orhan Veli Kanık olacak.")
    puan -= 1
print("*-----------------------------------------------------*")
soru5 = ["Pir Sultan Abdal 16. yüzyılda Sivas bölgesinde yaşamız bir halk ozanıdır. [D/Y]"]
cevap5 = ["D"]
puan += 1
#soru5
cevap = input((soru5[0]))
if cevap5[0] == cevap.upper ():
    print("Tebrikler, cevabınız doğru.")
    puan += 1
else:
    print("Cevabınız doğru değil.")
    puan -= 1
print("*-----------------------------------------------------*")
#test sonu
print("tebrikler testi tamamladınız. Aldığınız puan: "+str(puan*1))
