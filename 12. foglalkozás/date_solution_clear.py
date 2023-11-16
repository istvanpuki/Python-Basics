from datetime import datetime

def date(y, m, d):
    
    dateFromConsole = datetime(year=y,month=m,day=d)
    
    days = dateFromConsole.strftime("%j")
    print(days[0], days[1], days[2])
    
    
    if days[0] == '0':
        formatDays = days.replace(days[0],"")
    if days[1] == '0':
        formatDays = days.replace(days[1],"")
    
    return "A megadott dátum az év " + formatDays+ ". napja"

showDays = date( int( input("Év: ") ), int( input("Hónap: ") ), int( input("Nap: ") ) )
print(showDays)