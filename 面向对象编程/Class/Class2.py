# coding:utf-8

import datetime
from dateutil import rrule


class BetDate:  # 练习
    def __init__(self, start_date, stop_data):
        self.start = datetime.datetime.strptime(start_date, "%Y, %m, %d")
        self.stop = datetime.datetime.strptime(stop_data, "%Y, %m, %d")

    def days(self):
        d = self.stop - self.start
        return d.days if d.days > 0 else False

    def weeks(self):
        weeks = rrule.rrule(rrule.WEEKLY, dtstart=self.start, until=self.stop)
        return weeks.count()


fir_twe = BetDate("2019, 5, 1", "2019, 11, 25")
d = fir_twe.days()
w = fir_twe.weeks()
print("Between 2019-5-1, 2019-11-25")
print("Day is:", d)
print("Weeks is:", w)
