from datetime import datetime

def date(y, m, d):
    
    dateFromConsole = datetime(year=y,month=m,day=d)
    
    days = dateFromConsole.strftime("%j")
    
    for x in days:
        if x[0] == '0':
           formatDays = days.replace(x,"")
    
    return "A megadott dátum az év " + formatDays+ ". napja"

showDays = date( int( input("Év: ") ), int( input("Hónap: ") ), int( input("Nap: ") ) )
print(showDays)