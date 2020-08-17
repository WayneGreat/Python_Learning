# coding:utf-8

class MyRange:  # 迭代器
    def __init__(self, n):
        self.i = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration  # 停止迭代


print("range(7):", list(range(7)))
print("MyRange(7):", [i for i in MyRange(7)])


# 斐波那契数列生成
class Fibs:  # 版本1:迭代器
    def __init__(self, max):
        self.max = max
        self.a = 0
        self.b = 1

    def __iter__(self):  # 可迭代
        return self

    def __next__(self):  # 形成迭代器
        fib = self.a
        if fib > self.max:
            raise StopIteration  # 停止迭代
        self.a, self.b = self.b, self.a + self.b
        return fib


fibs = Fibs(10000)  # 只有通过迭代后，才有数据占用内存
lst = [fibs.__next__() for i in range(10)]  # fibs.__next__():在迭代过程中执行一些功能
print(lst)


def fibs():  # 版本2:生成器
    prev, curr = 0, 1
    while True:  # 生成器的绝妙之处：它只会在迭代时才会运行，所以死循环也没有问题
        yield prev  # 等于执行 return prev ，并在当前代码挂起，下次掉用时继续往后执行代码
        prev, curr = curr, prev + curr


import itertools

# 使用itertools.islice()来对迭代器和生成器做切片操作
print(list(itertools.islice(fibs(), 10)))
print(list(itertools.islice(fibs(), 3, 10)))
