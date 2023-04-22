# pip install python-dateutil มีแล้วไม่ต้องทำ
from datetime import datetime, date

from dateutil.relativedelta import relativedelta, SA, TH

def demo1():
    now = datetime.today()
    today = date.today()
    next_3_m = today + relativedelta(months=3)
    print('จากวันนี้           ',today)
    print('บวกไป 3เดือน จะเป็น',next_3_m)

    d1 = today + relativedelta(weeks=5)
    print(d1)

    d2 = today + relativedelta(years=1, months=6)
    print(d2)

    d3 = today + relativedelta(days=1)
    print(d3)

def demo2():
    now = datetime.today()
    print(now)
    t1 = now + relativedelta(hours=3, minutes=30)
    print(t1)

def demo_weekday():
    childrenday = date(2023, 1, 1) + relativedelta(weekday=SA(+2))
    print(childrenday)
    print(datetime.strftime(childrenday, "%a %b %d %m %y"))
    thanksgiving = date(2023, 11,1) + relativedelta(weekday=TH(4))
    print(datetime.strftime(thanksgiving, "%a %b %d-%m-%Y"))

def demo3():
    d1 = date(2023, 4, 22)
    d2 = d1 + relativedelta(months=1)
    d3 = d2 + relativedelta(months=-2)
    print(d2)
    print(d3)

demo1()
demo2()
demo_weekday()
demo3()