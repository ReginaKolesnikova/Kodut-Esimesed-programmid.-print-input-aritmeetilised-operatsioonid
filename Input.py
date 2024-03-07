#1 task
nimi=input("Mis on sinu nimi: ")
print("Tere tulemast, "+nimi+"!\n")


#2 task
print(" ")
kysimus=input("3+8/(4 - 2)*4= ")
if kysimus=="19":
     print("Oige!")
else:
    print("Vale!")

#2.1 task
print(" ")
print("Ruudu sees asub ring")
r=float(input("Ringi raadius on: "))
Skv=4*(r*r)
print("ruudu pindala=",Skv)
Pkv  = r*2*4
print("ruudu ümbermõõt=",Pkv)
Skr  = 3,14 * (r*r)
print("ringi pindala=",Skr)
Pkr  = 2 * 3,14 * r
print("ringi ümbermõõt=",Pkr)


#2.2 task
print(" ")
radearth=6378.1
print ("Maa radius on", radearth,"km")
diameuro=25.75
print ("2 euro diameter on", diameuro,"mm")
earth=(radearth*2*3.14)
print("Maa diameter ~",earth,"km")
amount=(earth/diameuro)
x = round(amount)
print(x,": 2-euroseid ümber Maa")


# 3 task
print(" ")
print("kill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll kill-koll killkoll kill-koll")

#4 task
print(" ")
print('''Rong see sõitis tsuhh tsuhh tsuhh,\n
piilupart oli rongijuht.\n
Rattad tegid rat tat taa,\n
rat tat taa ja tat tat taa.\n
Aga seal rongi peal,\n
kas sa tead, kes olid seal?\n''')

#5 task
print(" ")
a=float(input("esimene pikkus:"))
b=float(input("teine pikkus:"))
perpram=(a+b)*2
print("ümbermõõt on", perpram)
plopram=a*b
print("pindala on", plopram)

#6 task
print(" ")
print("Kütusekulu arvutamine")
lit=float(input("tangitud kütuse liitrid: "))
kil=float(input("läbitud kilomeetrid: "))
keskm=(lit/kil)*100
print("kütusekulu 100km kohta keskmiselt on", keskm)

#7 task
print(" ")
print("Rulluisutajad")
sredsko = 29.9
print("Rulluisutaja keskmine kiirus on 29,9 km/h")
rasvmin=(sredsko/60)
print(rasvmin, "km/min")

#8 task
print(" ")
print("Ajateisendus")
aja=int(input("aja minutes: "))
o=aja/60
hours = round(o)
xi=hours*60
minutes=aja-xi
print(hours,":",minutes)
