#! C:\Python35\python3.exe

import sys
sys.path.insert(0,'../')

import os
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'bookingSysterm.settings'

 # 让django进行初始化设置
import django
django.setup()

from infos.models import ReservationInfo
import datetime

today = datetime.date.today()
for i in range(1,7):
    t = today + datetime.timedelta(days=i)
    print(t)
    # for j in range(1,17):
    #     reser = ReservationInfo(date=t,tb_id=j)
    #     reser.save()