# coding:utf-8

import os
import csv

print(os.getcwd())  # 获取当前python交互模式的目录
# 方法一
f = open('test.txt', 'w')  # 覆盖原来的test.txt文件或创建
f.write("Life is short,You need Python")  # 写入文件
f.close()  # 文件保存
f = open('test.txt')
print(f.read())  # 读取文件内容
print(dir(f))  # 获取f的方法
# 方法二
with open('test.txt', 'a') as f:
    f.write("\n学python")
f = open('test.txt')
for line in f:  # 每行读取
    print(line)

f.seek(0)  # 可使指针回到起始位置

# csv文件操作
data = [['name', 'number'], ['python', 111], ['java', 222], ['php', 333]]
with open('csvfile.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)
f = open('csvfile.csv')
reader = csv.reader(f)
for row in reader:
    print(row)

# excel文件操作--pip install openpyxl
