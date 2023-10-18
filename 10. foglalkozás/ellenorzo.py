# 1. feladat
TAJ = input("Kérem a TAJ-számot: ") #String típusú legyen, hogy végig tudjunk majd rajta iterálni

# 2. feladat
utolso_szamjegy = TAJ[-1]
print(f"Az ellenőrzőszámjegy: {utolso_szamjegy}")

# 3. feladat
szorzatosszeg = 0

for i in range(0,8):
    #print(i)
    if (i+1) % 2 == 1:
        szorzatosszeg= szorzatosszeg + int( TAJ[i] ) * 3
    else:
        szorzatosszeg= szorzatosszeg + int( TAJ[i] ) * 7

print(f"A szorzatok összege: {szorzatosszeg}")

# 4. feladat
if szorzatosszeg % 10 == utolso_szamjegy:
    print("Helyes a szám")
else:
    print("Hibás a szám")

#print(szorzatosszeg%10)