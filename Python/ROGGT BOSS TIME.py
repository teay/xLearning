# pip install python-dateutil มีแล้วไม่ต้องทำ
from datetime import datetime, date
from dateutil.relativedelta import relativedelta, SA, TH
import pandas as pd

# ดึงเวลาบอสตาย ได้เวลาบอสเกิด

now = datetime.today()
print("เวลาบอสตาย",now)
DateTimeBaphometHappen = now + relativedelta(hours=2, minutes=0)
print("เวลาบอสเกิด"        ,DateTimeBaphometHappen)