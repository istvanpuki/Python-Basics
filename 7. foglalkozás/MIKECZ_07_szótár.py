#Szótár adattípus / Dictionary

alkalmazottak = []

alkalmazott1 = {
  "név": "Géza",
  "cím": "Debrecen",
  "kor": 28,
  "felnőtt": True
}

alkalmazott2 = {
  "név": "Roland",
  "cím": "Budapest",
  "kor": 15,
  "felnőtt": False
}

alkalmazott3 = {
  "név": "Kitti",
  "cím": "Sopron",
  "kor": 30,
  "felnőtt": True
}

print(alkalmazott1)
print(alkalmazott2)
print(alkalmazott3)

print(alkalmazott1.get("név"))
print(alkalmazott2.items())

#Feladat. Az alkalmazottak tömbhöz fűzd hozzá az alkalmazottakat, majd irattasd ki a három alkalmazott nevét a listából! (Csak a nevüket)

alkalmazottak.append(alkalmazott1)
alkalmazottak.append(alkalmazott2)
alkalmazottak.append(alkalmazott3)
print(alkalmazottak)

for alkalmazott in alkalmazottak:
    print(alkalmazott.get("név"))