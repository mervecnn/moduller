print("soru:1:")
import moduller
x=input("İşletmenin gelirini girin:")
y=input("İşletmenin giderini girin:")
isletmeKari=moduller.isletmeKari(x,y)
print(isletmeKari)
a=input("İşletmenin toplam cirosunu girin:")
b=input("İşletmenin toplam cirosonu girin:")
adambasiCiro=moduller.adambasiCiro(a,b)
print(adambasiCiro)

print("soru:2:")
from moduller import*
aktifler=aktif.hesapla(20000,10000,5000,28000,65000,150000,25000,8000)
pasifler=pasif.hesapla(42000,60000,35000,115000,59000)
if aktifler==pasifler:
    print("bilanco dogru")
else:
    print("bilanco yanlıs")

print("soru:3:")
from moduller import etkilesim_orani 
print("YBS1 etkileşim oranı:")
ybs1=etkilesim_orani(365000,65000,870,500,1125000)
print("YBS2 etkileşim oranı:")
ybs2=etkilesim_orani(450000,25000,380,100,1450000)
print("YBS3 grubu etkileşim oranı:")
ybs3=etkilesim_orani(582000,52000,1200,650,2000000)
