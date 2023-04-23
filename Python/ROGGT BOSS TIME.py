# pip install python-dateutil มีแล้วไม่ต้องทำ
from datetime import datetime, date
from dateutil.relativedelta import relativedelta, SA, TH
import pandas as pd

# ดึงเวลาบอสตาย ได้เวลาบอสเกิด

now = datetime.today()
print("เวลาบอสตาย",now)
DateTimeBaphometHappen = now + relativedelta(hours=2, minutes=0)
print("เวลาบอสเกิด"        ,DateTimeBaphometHappen)
print("complete")

now = datetime.today()
print("เวลาบอสตาย",now)
DateTimeBaphometHappen = now + relativedelta(hours=2, minutes=0)
print("เวลาบอสเกิด"        ,DateTimeBaphometHappen)
print("complete")
print("############################################################")

money = int(input("กรอกจำนวนเงินที่ต้องการแลกเปลี่ยน : "))
money_type = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
 
for t in money_type:
    if money >= t:
        print("{} บาท = {}".format(t, int(money / t)))
        money = money % t
print("complete")
print("############################################################")