# Class
## Class1.py
### 练习题
```
编写一个程序，用于判断学生是否已经完成作业。如果完成，教师会出表扬，否则要进行批评
```
### 运行结果
```
guojing
1
Ya! You have to die.
Teacher Yang said : zhang, You should work hard.
Teacher Yang said: Newton,You are great.
```
### 笔记
**类** `class` 是一种面向对象计算机编程语言的构造，是创建对象的蓝图，描述了所创建的对象共同的属性和方法

**对象** `object` 表示客观世界问题空间中的某个具体事物，又表示软件系统解空间的中的基本元素

**面向对象程序设计** `Object-oriented programming, OOP` 是一种程序设计范型，也是一种程序开发的方法

 ![image](https://github.com/WayneGreat/Python_Learning/blob/master/%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E7%BC%96%E7%A8%8B/Image/%E5%88%9B%E5%BB%BA%E7%B1%BB.png)
> 示例
```python
class Foo:
    def __init__(self):  # 初始化方法，实例一创建就执行
        print("I am in init")
        self.x = 'python'  # 实例具有了x的属性


f = Foo()
dir(f)  # 通过dir()函数获取实例所具有的属性
print(f.x)
```
> 运行结果
```
#实例初始化
I am in init
# 属性
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
'__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'x']
#实例中x的属性值
python
```
