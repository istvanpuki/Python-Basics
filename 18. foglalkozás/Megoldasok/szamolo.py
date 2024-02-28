#Digitális kultúra érettségi minta a 2024-es érettségi követelmények szerint

import random # 5. feladatnál szükségünk van a random modulra.

# 1. feladat
print("Milyen műveletet szeretne gyakorolni?\n\n1. Összeadás\n2. Kivonás \n3. Szorzás ")

# 2. feladat
valasz = int( input ("\nVálasztás (1-3): ") )

# 3. feladat
db = 0
ok = 0

# 4. feladat
while ok < 5:
    # 5. feladat
    db += 1
    a = random.randint(1, 10) # A random számok beolvasása
    b = random.randint(1, 10)

    if valasz == 1:
        d = a + b # A művelet eredménye letárolva, ahogy a feladat kéri
        c = int(input(f"{a} + {b} = ")) # A felhasználó által megadott érték, amit fejben számol ki
        if c == d:
            ok += 1
            print("Helyes")
        else:
            print("Hibás")

    elif valasz == 2:
        d = a - b # A művelet eredménye letárolva, ahogy a feladat kéri
        c = int(input(f"{a} - {b} = "))
        if c == d:
            ok += 1
            print("Helyes")
        else:
            print("Hibás")

    elif valasz == 3:
        d = a * b # A művelet eredménye letárolva, ahogy a feladat kéri
        c = int(input(f"{a} * {b} = "))
        if c == d:
            ok += 1
            print("Helyes")
        else:
            print("Hibás")

# 6. feladat
print(f"Gratulálunk!\nSikerült {ok} helyes műveletet elvégezni {db} próbálkozásból.")