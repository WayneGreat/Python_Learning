# coding:utf-8

class Date(object):
    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    @classmethod  # 类方法
    def from_string(cls, date_as_string):
        year, month, day = map(int, date_as_string.split('-'))
        date1 = cls(year, month, day) # 等于Date(year, month, day)
        return date1

    @staticmethod  # 静态方法
    def is_date_valid(date_as_string):
        year, month, day = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 2077


d = Date.from_string('2020-11-11')
print(d.year, d.month, d.day)
is_date = Date.is_date_valid('2020-11-11')
print(is_date)
