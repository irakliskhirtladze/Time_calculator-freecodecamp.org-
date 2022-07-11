def add_time(start, duration, startday=None):
    weekdays=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    time=start.split()[0]
    ampm=start.split()[1]
    starthours=int(time.split(':')[0])
    startmins=int(time.split(':')[1])
    durhours=int(duration.split(':')[0])
    durmins=int(duration.split(':')[1])

    if ampm=='PM':
       starthours=starthours+12
    if durhours>=24:
        durdays=durhours//24

    finhours=starthours+durhours
    finmins=startmins+durmins
    if finmins>=60:
        finmins%=60
        finhours+=1

    if finhours>=24:
        finhours%=24

    if finhours>=12:
        finhours%=12
        finampm='PM'
    else:
        finampm='AM'

    if finhours==0:
        finhours=12

    if finmins<10:
        finmins='0'+str(finmins)    

    sumhours=starthours+durhours
    summins=startmins+durmins
    if summins>=60:
        summins%=60
        sumhours+=1

    if startday!=None and sumhours<24:
        finday=startday.lower().title()
        new_time=print(f'{finhours}:{finmins} {finampm}, {finday}')
    if startday!=None and 24<=sumhours<48:
        weekday=startday.lower().title()
        finday=weekdays[(weekdays.index(weekday)+1)%7]
        new_time=print(f'{finhours}:{finmins} {finampm}, {finday} (next day)')
    if startday!=None and sumhours>=48:
        weekday=startday.lower().title()
        finday=weekdays[(weekdays.index(weekday)+durdays+1)%7]
        new_time=print(f'{finhours}:{finmins} {finampm}, {finday} ({durdays+1} days later)')
    
    if startday==None and sumhours<24:
        new_time=print(f'{finhours}:{finmins} {finampm}')
    if startday==None and 24<=sumhours<48:
        new_time=print(f'{finhours}:{finmins} {finampm} (next day)')
    if startday==None and sumhours>=48:
        new_time=print(f'{finhours}:{finmins} {finampm} ({durdays+1} days later)')

    return new_time    


add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "MoNday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)

add_time('11:55 PM', '00:30', 'Sunday')
# Returns: 12:25 AM, Monday (next day)

add_time("3:30 PM", "2:12")
#expected = "5:42 PM"

add_time("11:55 AM", "3:12")
#expected = "3:07 PM"

add_time("9:15 PM", "5:30")
#expected = "2:45 AM (next day)"

add_time("11:40 AM", "0:25")
#expected = "12:05 PM"

add_time("2:59 AM", "24:00")
#expected = "2:59 AM (next day)"

add_time("11:59 PM", "24:05")
#expected = "12:04 AM (2 days later)"

add_time("8:16 PM", "466:02")
#expected = "6:18 AM (20 days later)"

add_time("5:01 AM", "0:00")
#expected = "5:01 AM"

add_time("3:30 PM", "2:12", "Monday")
#expected = "5:42 PM, Monday"

add_time("2:59 AM", "24:00", "saturDay")
#expected = "2:59 AM, Sunday (next day)"

add_time("11:59 PM", "24:05", "Wednesday")
#expected = "12:04 AM, Friday (2 days later)"

add_time("8:16 PM", "466:02", "tuesday")
#expected = "6:18 AM, Monday (20 days later)"