# 2022. október - Kockák
# Feladatlap: https://dload-oktatas.educatio.hu/erettsegi/feladatok_2022osz_kozep/k_digkult_22okt_fl.pdf
# Az alábbi kód a hivatalos mintamegoldás kis mértékben módosított verziója.

# Anni és Panni három dobókockás játéka
import random
'''
1. Kérje be a felhasználótól N értékét, vagyis a feldobások számát, és tárolja el a kapott értéket! 
'''
N = int(input("Hány alkalommal legyen feldobás? "))

'''
2. Végezzen N feldobást a három kockával úgy, hogy minden feldobásnál generál három
véletlenszámot 1 és 6 között! Figyeljen arra, hogy a program futtatása során ne mindig
ugyanazt a véletlenszám-sorozatot kapja!
3. Minden feldobás után írja ki a kockán lévő számokat, valamint azok összegét, és azt is, hogy ki nyert. A kiírás egy sorban történjen, az alábbi mintához hasonlóan! 
'''
anni_nyert = 0
panni_nyert = 0
for i in range(N):
    kocka1 = random.randint(1, 6)
    kocka2 = random.randint(1, 6)
    kocka3 = random.randint(1, 6)
    osszeg = kocka1 + kocka2 + kocka3
    if osszeg < 10:
        nyert = "Anni"
        anni_nyert += 1
    else:
        nyert = "Panni"
        panni_nyert += 1
    print(f'Dobás: {kocka1} + {kocka2} + {kocka3} = {osszeg} \tNyert: {nyert}')

'''
4. A feldobások után egy mondatban írja ki, hogy hány alkalommal kedvezett az egyik, és hány alkalommal a másik játékosnak a szerencse!
'''
print(f'A játék során {anni_nyert} alkalommal Anni, {panni_nyert} alkalommal Panni nyert.')