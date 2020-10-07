import time
class Bilgisayar():
    def __init__(self,marka="HP",ram="16GB",ekran_karti="5GB",islemci="Intel i7",klasorler=["Masaüstü"],pc_durum="Açık"):
        self.marka=marka
        self.ram=ram
        self.ekran_karti=ekran_karti
        self.islemci=islemci
        self.klasorler=klasorler
        self.pc_durum=pc_durum

    def bilgileri_goster(self):
        print("""
        Marka: {}
        Ram: {}
        Ekran kartı: {}
        İslemci: {}
        """.format(self.marka,self.ram,self.ekran_karti,self.islemci))

    def hesap_makinesi(self):
        while True:

            print("""
    Toplama icin ---> 1
    Çıkarma için ---> 2
    Çarpma için ---> 3
    Bölme için --->4
            """)

            islem=input("Bir islem giriniz:")
            if(islem=="1"):
                a=int(input("Lutfen ilk degeri giriniz:"))
                b=int(input("Lutfen ikinci degeri giriniz:"))
                print(a+b)
                break
            elif(islem=="2"):
                a = int(input("Lutfen ilk degeri giriniz:"))
                b = int(input("Lutfen ikinci degeri giriniz:"))
                print(a-b)
                break
            elif(islem=="3"):
                a = int(input("Lutfen ilk degeri giriniz:"))
                b = int(input("Lutfen ikinci degeri giriniz:"))
                print(a*b)
                break
            elif(islem=="4"):
                a = int(input("Lutfen ilk degeri giriniz:"))
                b = int(input("Lutfen ikinci degeri giriniz:"))
                if(b==0):
                    print("Bu bölme islemi gerçekleştirilemez.")
                else:
                    print(a/b)
                    break
            else:
                print("Yanlış bir işlem girdiniz.")

    def masasutu_klasor_olustur(self):
        print("Klasor olusturuluyor...")
        time.sleep(1)
        isim=input("Klasorunuze isim giriniz:")
        self.klasorler.append(isim)
        print("Klasor olusturuldu.")

    def klasor_goruntule(self):
        print(self.klasorler)

    def __len__(self):
        return len(self.klasorler)

    def pc_ac(self):
        sifre="Fenerbahçe"
        if(self.pc_durum=="Açık"):
            print("Bilgisayar zaten açık!")
        else:
            girilen_sifre = input("Şifre giriniz:")
            if(girilen_sifre==sifre):
                print("Şifre doğru. Bilgisayar açılıyor.")
                self.pc_durum="Açık"
            else:
                print("Yanlış şifre girişi!")

    def pc_kapat(self):
        if(self.pc_durum=="Kapalı"):
            print("Bilgisayar zaten kapalı!")
        else:
            print("Bilgisyar kapanıyor...")
            time.sleep(1)
            self.pc_durum="Kapalı"
            print("Bilgisayar kapandı.")

print("""
1. Bilgisayarı açma
2. Bilgisayar özelliklerini görüntüleme
3. Hesap makinesi 
4. Klasör oluşturma
5. Oluşturulan klasörleri görüntüleme
6. Toplam klasör sayısı
7. Bilgisayarı kapatma 
Çıkmak için q'ya basınız.
""")

pc=Bilgisayar()

while True:
    numara = input("Lutfen bir numara giriniz:")
    if(numara=="q"):
        print("Çıkış yapılıyor...")
        time.sleep(1)
        print("Çıkış yapıldı.")
        break
    elif(numara=="1"):
        pc.pc_ac()
    elif(numara=="2"):
        pc.bilgileri_goster()
    elif(numara=="3"):
        pc.hesap_makinesi()
    elif(numara=="4"):
        pc.masasutu_klasor_olustur()
    elif(numara=="5"):
        pc.klasor_goruntule()
    elif(numara=="6"):
        print(pc.__len__())
    elif(numara=="7"):
        pc.pc_kapat()
    else:
        print("Yanlış bir numara girişi gerçekleştirdiniz!")
