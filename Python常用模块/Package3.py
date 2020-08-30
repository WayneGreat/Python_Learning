# coding:utf-8

# 示例一
class Calculator:
    is_raise = False

    def calc(self, express):
        try:
            return eval(express)
        except ZeroDivisionError:
            if self.is_raise:
                return "Zero can no be division"
            else:
                raise


if __name__ == "__main__":
    c = Calculator()
    #c.is_raise = True
    print(c.calc("8/0"))

# 示例二
while True:
    try:
        a = float(input('first number:'))
        b = float(input('second number:'))
        r = a / b
        print("{0} / {1} = {2}".format(a, b, r))
        break
    except ZeroDivisionError:  # 内置异常类型——分母为零
        print("The second numbers can not be zero.Try again.")
    except ValueError:  # 值不为数值类型
        print("Please enter number.Try again.")
    except:  # 其他异常
        break
