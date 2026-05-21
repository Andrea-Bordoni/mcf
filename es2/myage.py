from datetime import datetime,timedelta

datenow=datetime.now()
mydate_str=input('inserisci la tua data di nascita d-m-y e orario H-M-S: ')
mydate=datetime.strptime(mydate_str,"%d-%m-%Y %H-%M-%S")
print('sei nato il ',mydate)
print('Oggi è il ',datenow)
timediff=datenow-mydate
print(timediff)
tots=timediff.total_seconds()
print('sei nato ' ,timediff.days,' giorni fa')
print('sei nato ' ,tots,' secondi fa')
toty=int(timediff.days/365)
print('sei nato ',toty,' anni fa')


