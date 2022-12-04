#Listák indexelése
first_names = ["Józsi", "Géza", "Tamás", "Enikő", "Roxána"]
print(first_names)
print(first_names[0]) #indexszám. 0tól kezdődik az indexelés. Az első elem az 0.
#0. Józsi 1. Géza 2. Tamás 3. Enikő 4. Roxána
print(first_names[4])
print(first_names[-1]) #utolsó elem a listából. Ez akkor hasznos, ha nem tudod mekkora a listád hossza

#Listák szeletelése
print(first_names[0:3])   #0,1,2 index benne van. a 3. Enikő már nincs benne, ezért ki se írja
print(first_names[2:4])

#mátrix lista
numbers = [[1,2,3], [4,5,6], [7,8,9]] #ez 2 dimenziós lista ez esetben
print(numbers)
print(numbers[0]) #indexelve. a belső listára mutat a 0. index. [1,2,3]
print(numbers[2] [1]) #a 2-es indexből ad vissza az első index számú elemet. Ez a 8-as most

#0-99 számok generálása. A range azt jelenti, hogy hány db. számot hozunk létre.
# a Legnagyobb szám így range-1
szamlista = range(100)
print(szamlista)
print(list(szamlista)) #Lista típussá kényszerítünk


# A W3school feladataival lehet gyakorolni az Operators és a List témakörben egyaránt! :)