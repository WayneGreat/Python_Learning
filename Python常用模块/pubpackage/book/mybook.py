#coding:utf-8

class Book:
    def __init__(self,year):
        if str(year) == "2020":
            self.book = "数据准备和特征工程"
        else:
            self.book = "学python"

    def book_name(self):
        return self.book
