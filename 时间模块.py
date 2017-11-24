#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
class TimeHeleer():
    def __init__(self):
        pass
    def now(self):
        now = datetime.now()
        return now
    def get_excute_time(self,year,month,day,hour,minute,second):
         time=datetime(year=year,month=month,day=day,hour=hour,minute=minute,second=second)
         return time
    def getTimeStamp(self,year,month,day,hour,minute,second):
        time = datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
        return time.timestamp()
    def strToTime(self,string):
        time=datetime.strptime(string,'%Y-%m-%d %H:%M:%S')

        return time
time=TimeHeleer()
print(time.strToTime('2016-12-13 10:53:34'));#1475287518.0小数位表示毫秒数


