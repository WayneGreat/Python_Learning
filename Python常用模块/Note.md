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
## mypackage dir
## 笔记
> 示例

![image](https://github.com/WayneGreat/Python_Learning/blob/master/Python%E5%B8%B8%E7%94%A8%E6%A8%A1%E5%9D%97/Image/%E5%8C%85%E7%BB%93%E6%9E%84.png)

> Cmd运行

![image](https://github.com/WayneGreat/Python_Learning/blob/master/Python%E5%B8%B8%E7%94%A8%E6%A8%A1%E5%9D%97/Image/cmd%E6%BC%94%E7%A4%BA.png)
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
