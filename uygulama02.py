print("*Lütfen aşağıdaki soruları dikkatlice okuyup cevaplayınız.*")
print("*Süreniz her bir soru için 1 dakikadır, toplamda ise 5 dakikanız vardır.*")
print("*----------------------------------------------------*")
sorular = ['Kırmızı Karanfil adlı şiir kitabı hangi yazara aittir',\
            'Marko paşa adlı eser hangi yazarımıza aittir?',\
            'Hasretinden Prangalar Eskittim, Ahmed Arif in kaç yılında yayımlanan şiir kitabıdır?',\
            'Edebiyatımızda lakabı Şiiri sokağa taşıyan şair olarak bilinen şairimiz kimdir?',\
            'Pir Sultan Abdal kaçıncı yüzyılda yaşamız bir halk ozanıdır.']
cevaplar = ['B', 'C', 'A', 'E', 'D']
cevapA = ['Can Yücel', 'Nazım Hikmet Ran', '1968', 'Ümit Yaşar Oğuzcan', '13.']
cevapB = ['Gülten Akın', 'Necip Fazıl Kısakürek', '1967', 'Ahmet Ümit', '14.']
cevapC = ['Didem Madak', 'Sabahattin Ali', '1966', 'Özdemir Asaf', '15.']
cevapD = ['Ayşe Kulin', 'Hasan Hüseyin Korkmazgil', '1965', 'Ataol Behramoğlu', '16.']
cevapE = ['Yılmaz Erdoğan', 'Adnan Yücel', '1964', 'Orhan Veli Kanık', '17.']
puan = 0
for i in range(len(sorular)):
    print("Soru " + str(i+1)+":"+sorular[i])
    print("A.) " + cevapA[i])
    print("B.) " + cevapB[i])
    print("C.) " + cevapC[i])
    print("D.) " + cevapD[i])
    print("E.) " + cevapE[i])
    cevap = input("Cevabınızı Giriniz: ")
    if cevaplar[i] == cevap.upper():
        puan +=1
print("Tebrikler, Testi Tamamladınız")
print("Aldığınız not: " +str(int((puan/len(sorular))*100)))
input() #Dikkat, Bu Satır programın kapanmamasını sağlayacak.