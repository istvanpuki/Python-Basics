"""
Feladat:
Írj egy Python programot, amely bekér egy dátumot három pozitív egész számként (év, hó, nap)! A
program határozza meg, hogy az adott dátum az év hányadik napja!

"""
from datetime import datetime

def date(y, m, d):
    
    dateFromConsole = datetime(year=y,month=m,day=d)
    #print(dateFromConsole)
    #Itt lászik, hogy a datetime() úgy működik, hogy a year, month, day kulcsok után vár egy értéket. Ez jelen esetben
    #az amit, bekértünk a konzolról.
    
    days = dateFromConsole.strftime("%j")
    #print(days)
    #print(type(days))

    #3 Jegyű számokat adott vissza. Például az év 41. napján 041 stringet kaptunk. Nekem a felesleges 0 nem tetszett, ezért levágtam.
    #Pontosabban a 0 helyére egy üres stringet varázsoltam. Hogy lett string a dátumból? 13. sor. A python beépített függvénye miatt.
    #strftime utal is a stringre :)
    #Ezt már nem volt muszáj megcsinálni, csak így elegáns szerintem! :)

    for x in days:
        if x[0] == '0':
           formatDays = days.replace(x,"")
    
    return "A megadott dátum az év " + formatDays+ ". napja"

showDays = date( int( input("Év: ") ), int( input("Hónap: ") ), int( input("Nap: ") ) )
print(showDays)