#soru:1
def isletmeKari (x,y):
    x=int(x)
    y=int(y)
    isletmeKari=x-y
    print(isletmeKari)
def adambasiCiro (a,b):
    a=int(a)
    b=int(b)
    adambasiCiro=a/b
    print(adambasiCiro)

#soru:2
class aktif:
    def hesapla(kasa,alınan,bankalar,alacak,ticari,binalar,tasitlar,demirB):
        aktif=(kasa+alınan+bankalar+alacak+ticari+binalar+tasitlar+demirB)
        return aktif
class pasif:
    def hesapla(satıcılar,banka,bankaK,borc,özS):
        pasif=(banka+satıcılar+bankaK+borc+özS)
        return pasif
#soru:3
class etkilesim_orani:
    def __init__(begeni,self,paylasim,yorum,icerik,takip):
        etki=(((begeni+yorum+paylasim)/icerik)/takip)*100
        print(float(etki))
        if etki>=0.20:
           print("basarili")
        else:
            print("basarısız")
