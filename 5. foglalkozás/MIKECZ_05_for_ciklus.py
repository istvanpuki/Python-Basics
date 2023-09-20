# For ciklus. Ha valamit többször akarunk végrehajtani, akkor érdemes használni
# például Ha 10-szer kiakarok iratattatni valammit, 10 print parancsot is használhatok, de
# Ez nem lenne túl elegáns megoldás. Helyette érdemes ciklust használni

# for (bármilyen változó név) általában i-t szoktak, hogy érthető legyen. Az i az iterátorra utal
# ciklus test sorbehuzassal kezdődik, hogy lásd majd hol fut a ciklus
# a range(10)-el 0-9ig tartományt hozunk létre
# a ciklus 10 ismétlésszámot jelent ebben az esetben
# 10-szer írja ki a ciklustest utasításait. Jelen esetben 3 utasításunk van
# Amit 10-szer ismétel meg. Az összesen 30 print utasítás kiírása
for i in range(10):
    print(i)
    print("hello")
    print("üdvözöllek")

fruits = ["Apple", "Pear", "Banana", "Orange", "Plum"]
for i in fruits:
    print(i)

for i in range(1,6):
   print(i)
   print("Üdv a Python foglalkozáson!")

#
#Bővebben
#http://wiki.ubuntu.hu/index.php/Python_kezd%C5%91knek_kurzus_2._lecke
#szóközöknek jelentősége van a Ciklus kezdete miatt.