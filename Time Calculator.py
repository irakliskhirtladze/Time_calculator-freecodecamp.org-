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
