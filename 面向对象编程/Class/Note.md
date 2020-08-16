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
#### `类 class` 
- 是一种面向对象计算机编程语言的构造，是创建对象的蓝图，描述了所创建的对象共同的属性和方法

#### `对象 object` 
- 表示客观世界问题空间中的某个具体事物，又表示软件系统解空间的中的基本元素

#### `面向对象程序设计 Object-oriented programming, OOP` 
- 是一种程序设计范型，也是一种程序开发的方法

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
***
## Class2.py
### 练习题
```
创建类，能够计算任意两个日期之间的天数，周数

注：需要 pip3 install python-dateutil
```
### 运行结果
```
Between 2019-5-1, 2019-11-25
Day is: 208
Weeks is: 30
```
### 笔记
#### `类属性`
- 类属性，又称静态属性
- 只有通过类才能修改
- 实例也拥有类属性，但不能修改类属性
#### `实例属性`
- 实例属性，又称动态属性
- 通过实例创建
- 不同实例的实例属性不同
- 实例的__dict__显示当前实例的所有属性
#### `self的作用`
- 类中的方法，如无特别规定，都是以self作为第一参数
- selfs用当前实例
***
## Class3.py
### 练习题
```
创建类，能够通过 "年-月-日" 字符串创建实例，并检验年，月，日是否合法.
```
### 运行结果
```
2020 11 11
True
```
### 笔记
#### `方法与函数`
- 名称的命名、代码块的编写方式都一样
- (实例)方法不能单独调用，只能通过实例／类调用
- 方法的第一个参数必须是self
#### `类方法`
- 使用装饰器：@classmethod
- 类方法第一个参数：cls，表示类本身
#### `静态方法`
- 使用装饰器：@staticmethod
- 静态方法不与实例绑定
***
## Class4.py
### 练习题
```
请编写“物理学家”的类，并将其作为“理论物理学家”和“实验物理学家”两个类的父类
```
### 运行结果
```
Relativity Hair is awesome
Albert Einstein research AAA
My theory is Relativity, it is based on ZZZ
```
### 笔记
#### `继承`
- 即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。
#### `super()`
- super()函数是用于调用父类（超类）的一个方法。
- super是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没可题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种可题
- MRO就是类的方法解析顺序表，其实也就是继承父类方法时的顺序表。
> 示例-单继承
```python
class Person:  # 单继承
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Student(Person):
    def __init__(self, school, name, age):
        self.school = school
        super().__init__(name, age)

    def grade(self, n):
        print("{0}'s grade is {1}".format(self.name, str(n)))


stu1 = Student('Soochow', "Galileo", 27)
stu1.grade(99)
print((stu1.get_name()))
print(stu1.get_age())

```
> 运行结果
```
Galileo's grade is 99
Galileo
27
```
> 示例-多继承
```python
class K1:  # 多继承
    def foo(self):
        print("K1-foo")


class K2:
    def foo(self):
        print("K2-foo")

    def bar(self):
        print("K2-bar")


class J1(K1, K2):
    pass


class J2(K1, K2):
    def bar(self):
        print("J2-bar")


class C(J1, J2):
    pass


print(C.__mro__) # 继承父类方法时的顺序表
m = C()
m.foo()
m.bar()

```
> 运行结果2
```
(<class '__main__.C'>, <class '__main__.J1'>, <class '__main__.J2'>, <class '__main__.K1'>, <class '__main__.K2'>, <class 'object'>)
K1-foo
J2-bar
```
***
## Class5.py
### 笔记
#### `类的私有属性`
- __private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问
#### `类的私有方法`
- __private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用
>示例
```python
class Site:
    def __init__(self, name, url):
        self.name = name       # public 公共属性
        self.__url = url   # private 私有属性
 
    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)
 
    def __foo(self):          # 私有方法
        print('这是私有方法')
 
    def foo(self):            # 公共方法
        print('这是公共方法')
        self.__foo()
 
x = Site('菜鸟教程', 'www.runoob.com')
x.who()        # 正常输出
x.foo()        # 正常输出
x.__foo()      # 报错
```
#### `__str__`
- 在python中方法名如果是__xxxx__()的，那么就有特殊的功能，因此叫做“魔法”方法
- 当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
> 示例
```python
class RoundFloat:
    def __init__(self, val):
        self.value = round(val, 2)

    def __str__(self):  # str:用户; repr:解释器
        return "{0:.2f}".format(self.value)

    __repr__ = __str__


r = RoundFloat(3.1415926)
print(r)
print(type(r))
```
> 运行结果
```
3.14
<class '__main__.RoundFloat'>
```
> 图例
 ![image](https://github.com/WayneGreat/Python_Learning/blob/master/%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E7%BC%96%E7%A8%8B/Image/%E5%9B%BE%E4%BE%8B.png)
> 示例
```python
class Fraction:
    def __init__(self,number,denom=1):
        self.number = number
        self.denom = denom

    def __str__(self):
        return str(self.number) + "/" + str(self.denom)

    __repr__ = __str__

f = Fraction(2,3)
print(f)
```
> 运行结果
```
2/3
```
