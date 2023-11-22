szam = ''

# 1. feladat
while(len(szam) < 5):
   szam = input('Adj meg egy legalább 5 számjegyből álló számot! ')

# 2. feladat
print('\n2. feladat')
szam = int(szam)
if szam % 5 == 0 and szam % 10 == 0:
   print('A szám osztható öttel és tízzel.')
else:
   print('A szám nem osztható öttel és tízzel.')

# 3. feladat
szam_vissza = str(szam)
print('\n3. feladat')
print(f'A szám visszafelé olvasva: {szam_vissza[::-1]}')

# 4. feladat
szamok = []
for szam_jegyek in szam_vissza:
   szam_jegyek = int(szam_jegyek)
   if szam_jegyek % 2 == 0:
     szamok.append(szam_jegyek)
szamok.sort()
print('\n4. feladat')
print('A páros számjegyek növekvő sorrendben: ')
print(szamok)

# 5. feladat
ismetlodo_jegyek = []
for sz in szam_vissza:
   if szam_vissza.count(sz) > 1 and sz not in ismetlodo_jegyek:
      ismetlodo_jegyek.append(sz)

if ismetlodo_jegyek:
    print('\n5. feladat')
    print('Az ismétlődő számjegyek: ', ', '.join(ismetlodo_jegyek))
else:
    print('\n5. feladat')
    print("Nincsenek ismétlédő számjegyek a számban.")

# 6. feladat
print('\n6. feladat')
for index, szamjegy in enumerate(szam_vissza, start=1):
    print('x', end='')
    if (len(szam_vissza) - index) % 3 == 0 and len(szam_vissza) != index:
        print('.', end='')  