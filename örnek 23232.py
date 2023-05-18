class magaza_sinifi:
    def __init__(self,magaza_adi,satici_adi,satici_cinsi,satis_tutari):
        self.__magaza_adi=magaza_adi
        self.__satici_adi=satici_adi
        self.__satici_cinsi=satici_cinsi
        self.__satis_tutari=satis_tutari
    

    def get_satici_adi(self):
        return self.__satici_adi
    
    def set_satici_adi(self,satici_adi):
        self.__satici_adi=satici_adi

    def get_satici_cinsi(self):
        return self.__satici_cinsi
    
    def set_satici_cinsi(self,satici_cinsi):
        self.__satici_cinsi=satici_cinsi
    
    def get_satis_tutari(self):
        return self.__satis_tutari
    
    def set_satis_tutari(self, satis_tutari):
        self.__satis_tutari = satis_tutari
    
    

        
    
def main():
    store={}
    while True:
        magaza_adi=input("mağaza adi giriniz(çıkmak için h/H ye bas): ")
        if magaza_adi=="h" or magaza_adi=="H":
            break

        satici_adi=input("satici adi giriniz: ")
        satici_cinsi=input("satici cinsini gir(beyaz eşya,tv,bilgisayar vb.): ")

        satis_tutari=float(input("satiş tutarini giriniz: "))
        a = magaza_sinifi(magaza_adi, satici_adi, satici_cinsi,satis_tutari)
        if magaza_adi  in store:
            store[magaza_adi]["satislar"].append(satis_tutari)
            store[magaza_adi]["store"].append(a)
        else:
            store[magaza_adi]={"satislar":[satis_tutari],"store":[a]}

    for magaza in store:
        print(f"{magaza} mağazasında toplam satış tutari:{magaza_satis_tutar(store[magaza])}")
        for a in store[magaza]["store"]:
            print(a)
def magaza_satis_tutar(magaza_dict):
        toplam_satis_tutari=0
        satislar = magaza_dict["satislar"]
        toplam_satis_tutari = sum(satislar)
        return toplam_satis_tutari
main()
            