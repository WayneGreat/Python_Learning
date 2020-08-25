# Catalogue

# Package
### Package1.py
### `笔记`
#### `模块`
- `.py`文件
#### `包`
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
#### `if __name__ == '__main__':`的作用&原理
- 一个python文件通常有两种使用方法
    - 第一是作为脚本直接执行
    - 第二是 import 到其他的 python 脚本中被调用（模块重用）执行
    - 因此 `if __name__ == '__main__':` 的作用就是控制这两种情况执行代码的过程，在 `if __name__ == '__main__':` 下的代码只有在第一种情况下（即文件作为脚本直接执行）才会被执行，而 import 到其他脚本中是不会被执行的
- 每个python模块（python文件）都包含内置的变量 `__name__`，当该模块被直接执行的时候，`__name__` 等于文件名（包含后缀 .py ）
- 如果该模块 import 到其他模块中，则该模块的 `__name__` 等于模块名称（不包含后缀.py），而 `__main__` 始终指当前执行模块的名称（包含后缀.py），进而当模块被直接执行时，__name__ == 'main' 结果为真
***
### mypackage dir
### `笔记`
> 示例

![image](https://github.com/WayneGreat/Python_Learning/blob/master/Python%E5%B8%B8%E7%94%A8%E6%A8%A1%E5%9D%97/Image/%E5%8C%85%E7%BB%93%E6%9E%84.png)

> Cmd运行

![image](https://github.com/WayneGreat/Python_Learning/blob/master/Python%E5%B8%B8%E7%94%A8%E6%A8%A1%E5%9D%97/Image/cmd%E6%BC%94%E7%A4%BA.png)
***
### 