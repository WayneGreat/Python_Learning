# Catalogue

# Package
## Package1.py
## 笔记
### `模块`
- `.py`文件
### `包`
- 有一定层次的目录结构
    - `.py` 文件或子目录
    - `__init__.py`
> 导入模块＼包
```python
import module
from module import XXX
from module import *
import module as other_name
```
> 使用
```python
import math
math.pow(2,3)
```
```python
from math import pow
from math import *
pow(2,3)
```
```python
import math as shuxue
shuxue.pow(2,3)
```
> 示例
```python
class Book:
    lang = 'learn python with wayne'

    def __init__(self, author):
        self.author = author

    def get_name(self):
        return self.author


def new_book():
    return "数据准备和特征工程"


if __name__ == '__main__': #  程序入口
    python = Book('wayne')
    author_name = python.get_name()
    print(author_name)
    published = new_book()
    print(published)

```
> 运行结果
```
wayne
数据准备和特征工程
```
### `if __name__ == '__main__':`的作用&原理
- 一个python文件通常有两种使用方法
    - 第一是作为脚本直接执行
    - 第二是 import 到其他的 python 脚本中被调用（模块重用）执行
    - 因此 `if __name__ == '__main__':` 的作用就是控制这两种情况执行代码的过程，在 `if __name__ == '__main__':` 下的代码只有在第一种情况下（即文件作为脚本直接执行）才会被执行，而 import 到其他脚本中是不会被执行的
- 每个python模块（python文件）都包含内置的变量 `__name__`，当该模块被直接执行的时候，`__name__` 等于文件名（包含后缀 .py ）
- 如果该模块 import 到其他模块中，则该模块的 `__name__` 等于模块名称（不包含后缀.py），而 `__main__` 始终指当前执行模块的名称（包含后缀.py），进而当模块被直接执行时，__name__ == 'main' 结果为真
***
## pubpackage dir
## 笔记
### `文件配置`
> 文件夹结构示例  
```
|--pubpackage
|  |--book
|  |  |--__init__.py
|  |  |--mybook.py
|--__init__.py
|--langspeak.py
|--LICENSE
|--README.md
|--setup.py
```
- `book, pubpackage文件夹` 是自己制定的文件夹，里面都需要一个 `__init__.py` 文件
- `README.md, LICENSE` 为发布包时需要添加的说明文件   

### `主要文件`  
> 示例

![image](https://github.com/WayneGreat/Python_Learning/blob/master/Python%E5%B8%B8%E7%94%A8%E6%A8%A1%E5%9D%97/Image/pubpackage.png)

> mybook.py  
```python
class Book:
    def __init__(self,year):
        if str(year) == "2020":
            self.book = "数据准备和特征工程"
        else:
            self.book = "学python"

    def book_name(self):
        return self.book

```
> langspeak.py
```python
class LangSpeak:
    def speak(self):
        return "Life is short, You need Python."

```
> setup.py
```python
import setuptools
import os

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
# package=setuptools.find_packages()使用

with open("README.md", 'r') as f:  # 自动读取
    long_description = f.read()

setuptools.setup(
    name="wayneproject",  # 包名称
    version="1.0",  # 包版本
    author="wayne",  # 作者名称
    author_email="",  # 作者邮箱
    description="This is my first project",  # 包详细描述
    long_description=long_description,  # 长描述，使用README,打包到pipy需要
    long_description_content_type="text/markdown",  # 描述格式类型
    url="",  # 项目官网
    py_modules=['langspeak'],  # 使用包时的名称
    package=setuptools.find_packages(),
    classifiers=[  # 程序的所属分类列表
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'  # python版本依赖
)

```
### `打包上传到test.pypi`  

> 步骤
- 先在 `https://test.pypi.org/` pipy测试网站进行注册
- 编写好源码和配置好setup.py脚本后
- cmd进入到包文件夹根目录
- 输入 `python3 setup.py install` 将当前模块安装到第三方库中 
- 输入 `python3 -m pip install --user --upgrade setuptools wheel` 升级setuptools版本
- 输入 `pip install twine` 安装发包工具-twine
- 输入 `python3 setup.py sdist bdist_wheel` 进行打包
- 输入 `twine upload --repository-url https://test.pypi.org/legacy/ ./dist/*` 再输入账户密码上传(url为pypi测试网站)
- 进入test.pipy网站查看已上传的包，可以使用 `pip` 进行安装
> 示例

![image](https://github.com/WayneGreat/Python_Learning/blob/master/Python%E5%B8%B8%E7%94%A8%E6%A8%A1%E5%9D%97/Image/pypi.png)

> 测试
```python
import langspeak

ls = langspeak.LangSpeak()
print(ls.speak())
```
> 结果
```
Life is short, You need Python.
```
***
## Package2.py
## 笔记
> 文件操作符

![image](https://github.com/WayneGreat/Python_Learning/blob/master/Python%E5%B8%B8%E7%94%A8%E6%A8%A1%E5%9D%97/Image/%E6%96%87%E4%BB%B6%E6%93%8D%E4%BD%9C%E7%AC%A6.png)

> 文件写入&读取
```python
import os

print(os.getcwd())  # 获取当前python交互模式的目录

with open('test.txt', 'a') as f:
    f.write("\n学python")

f = open('test.txt')
print(f.read())  # 读取文件内容
print(dir(f))  # 获取f的方法
for line in f:  # 每行读取
    print(line)
```
> CSV文件操作
```python
import csv

data = [['name', 'number'], ['python', 111], ['java', 222], ['php', 333]]

with open('csvfile.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)

f = open('csvfile.csv')
reader = csv.reader(f)
for row in reader:
    print(row)
```
***
## Package3.py
## 运行结果  
> 示例一
```
Traceback (most recent call last):
  File "c:/Users/Wayne/Desktop/learning/Python_Learning/Python常用模块/Package3.py", line 17, in <module>
    print(c.calc("8/0"))
  File "c:/Users/Wayne/Desktop/learning/Python_Learning/Python常用模块/Package3.py", line 7, in calc
    return eval(express)
  File "<string>", line 1, in <module>
ZeroDivisionError: division by zero
```
## 笔记
> 异常处理
```python
try:
    pass
except ValueError as e: # 传入无效的参数
    pass
except Exception as e: # 常规错误的基类
    print(e.args)
    pass
```
> 内置异常类型
```
BaseException:所有异常的基类,包括退出异常和非退出异常；
SystemExit: 解释器请求退出 
KeyboardInterrupt: 用户中断执行(通常是输入^C) 
Exception: 常规错误的基类 
StopIteration: 迭代器没有更多的值 
GeneratorExit: 生成器(generator)发生异常来通知退出 
ArithmeticError: 所有数值计算错误的基类 
FloatingPointError: 浮点计算错误 
OverflowError: 数值运算超出最大限制 
ZeroDivisionError: 除(或取模)零 (所有数据类型) 
AssertionError: 断言语句失败 
AttributeError: 对象没有这个属性 
EOFError: 没有内建输入,到达EOF标记 
EnvironmentError: 操作系统错误的基类 
IOError: 输入/输出操作失败 
OSError: 操作系统错误 
WindowsError: 系统调用失败 
ImportError: 导入模块/对象失败 
LookupError: 无效数据查询的基类 
IndexError: 序列中没有此索引(index) 
KeyError: 映射中没有这个键 
MemoryError: 内存溢出错误(对于Python 解释器不是致命的) 
NameError: 未声明/初始化对象 (没有属性) 
UnboundLocalError: 访问未初始化的本地变量 
ReferenceError: 弱引用(Weak reference)试图访问已经垃圾回收了的对象 
RuntimeError: 一般的运行时错误 
NotImplementedError: 尚未实现的方法 
SyntaxError: Python语法错误 
IndentationError: 缩进错误 
TabError: Tab和空格混用 
SystemError: 一般的解释器系统错误 
TypeError: 对类型无效的操作 
ValueError: 传入无效的参数 
UnicodeError: Unicode相关的错误 
UnicodeDecodeError: Unicode解码时的错误 
UnicodeEncodeError: Unicode编码时错误 
UnicodeTranslateError: Unicode转换时错误 
Warning: 警告的基类 
DeprecationWarning: 关于被弃用的特征的警告 
FutureWarning: 关于构造将来语义会有改变的警告 
OverflowWarning: 旧的关于自动提升为长整型(long)的警告 
PendingDeprecationWarning: 关于特性将会被废弃的警告 
RuntimeWarning: 可疑的运行时行为(runtime behavior)的警告 
SyntaxWarning: 可疑的语法的警告 
UserWarning: 用户代码生成的警告
```
