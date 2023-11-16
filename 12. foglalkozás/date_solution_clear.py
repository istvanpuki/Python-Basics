from datetime import datetime

def date(y, m, d):
    
    dateFromConsole = datetime(year=y,month=m,day=d)
    
    days = dateFromConsole.strftime("%j")
    print(type(days))
    print(days[0], days[1], days[2])
    formatDays = ""
    
    for day in days:
        if day == '0' and days[0] == '0':
            formatDays = days.replace(day, "")
            if days[2] == '0':
                formatDays = formatDays + '0'

    return "A megadott dátum az év " + formatDays+ ". napja"

showDays = date( int( input("Év: ") ), int( input("Hónap: ") ), int( input("Nap: ") ) )
print(showDays)