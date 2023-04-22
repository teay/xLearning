# pip install python-dateutil มีแล้วไม่ต้องทำ
from datetime import datetime, date
from dateutil.relativedelta import relativedelta, SA, TH

def demo1():
    now = datetime.today()
    today = date.today()
    next_3_m = today + relativedelta(months=3)
    print('จากวันนี้           ',today)
    print('บวกไป 3เดือน จะเป็น',next_3_m)

def demo2():
    now = datetime.today()
    print(now)
    t1 = now + relativedelta(hours=3, minutes=30)
    print(t1)

demo1()
demo2()

nameBOSS = []
pictureBOSS = []
timeDelayAfterdie = []
mapBOSS = []
positionOnMapBossDie= []
dateBossDie = []
timeBossDie = []
DelayTimeIsMinute = []
timeBossHappen = []