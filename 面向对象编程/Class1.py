# coding:utf-8

# 创建类-示例
class SuperMan:
    '''
    A class of superman
    '''

    def __init__(self, name):
        self.name = name
        self.gender = 1  # 1: male
        self.single = False
        self.illness = False

    def nine_negative_kongfu(self):
        return "Ya! You have to die."


guojing = SuperMan('guojing')  # 实例化
print(guojing.name)
print(guojing.gender)
kongfu = guojing.nine_negative_kongfu()
print(kongfu)


# 练习
class Student:
    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject

    def do_work(self, time):
        if self.grade > 3 and time > 2:
            return True
        elif self.grade < 3 and time > 0.5:
            return True
        else:
            return False


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def evaluate(self, result=True):
        if result:
            return "You are great."
        else:
            return "You should work hard."


stu_zhang = Student('zhang', 5, 'math')
tea_wang = Teacher('Yang', 'math')
tea_to_zhang = tea_wang.evaluate(stu_zhang.do_work(1))
print("Teacher {0} said : {1}, {2}".format(tea_wang.name, stu_zhang.name, tea_to_zhang))

stu_newton = Student('Newton', 8, 'physics')
tea_to_newton = tea_wang.evaluate(stu_newton.do_work(4))
print("Teacher {0} said: {1},{2}".format(tea_wang.name, stu_newton.name, tea_to_newton))


# 笔记
class Foo:
    def __init__(self):  # 初始化方法，实例一创建就执行
        print("I am in init")
        self.x = 'python'  # 实例具有了x的属性


f = Foo()
dir(f)  # 通过dir()函数获取实例的属性
print(f.x)
