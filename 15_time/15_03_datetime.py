import time,datetime,threading

print(datetime.datetime.now())
dt=datetime.datetime(2015,10,21,16,29,0)
print(dt.year,dt.month,dt.day)
print(dt.hour,dt.minute,dt.second)
print(datetime.datetime.fromtimestamp(1000000))
print(datetime.datetime.fromtimestamp(time.time()))

halloween2015=datetime.datetime(2015,10,31,0,0,0)
newyear2016=datetime.datetime(2016,1,1,0,0,0)
oct31_2015=datetime.datetime(2015,10,31,0,0,0)
print(halloween2015==oct31_2015)
print(halloween2015>newyear2016)
print(newyear2016>halloween2015)
print(newyear2016!=oct31_2015)

delta=datetime.timedelta(days=11,hours=10,minutes=9,seconds=8)
print(delta.days,delta.seconds,delta.microseconds)
print(delta.total_seconds())
print(str(delta))

dt=datetime.datetime.now()
print(dt)
thousandDays=datetime.timedelta(days=1000)
print(dt+thousandDays)

oct21st=datetime.datetime(2015,10,21,16,29,0)
aboutThirtyYears=datetime.timedelta(days=365*30)
print(oct21st)
print(oct21st-aboutThirtyYears)
print(oct21st-2*aboutThirtyYears)

halloween2016=datetime.datetime(2016,10,31,0,0,0)
while datetime.datetime.now()<halloween2016:
	time.sleep(1)

oct21st=datetime.datetime(2015,10,21,16,29,0)
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
print(oct21st.strftime('%I:%M %p'))
print(oct21st.strftime("%B of '%y"))

print(datetime.datetime.strptime('October 21, 2015','%B %d, %Y'))
print(datetime.datetime.strptime('2015/10/21 16:29:00','%Y/%m/%d %H:%M:%S'))
print(datetime.datetime.strptime("October of '15","%B of '%y"))
print(datetime.datetime.strptime("November of '63","%B of '%y"))

print('Start of program.')

def takeANap():
	time.sleep(5)
	print("wake up!")

threadObj=threading.Thread(target=takeANap)
threadObj.start()
print('End of program.')

threadObj=threading.Thread(target=print,args=['Cats','Dogs','Frogs'],kwargs={'sep':' & '})
threadObj.start()

