# coding:utf-8

class Pyhsicist:  # 练习
    def __init__(self, name, iq=120, looks='handsome', subject='physics'):
        self.name = name
        self.iq = iq
        self.looks = looks
        self.subject = subject

    def research(self, field):
        print("{0} research {1}".format(self.name, field))

    def speak(self):
        print("My name is ", self.name)
        print("I am ", self.looks)
        print("Intelligence is ", self.iq)
        print("I like ", self.subject)


class ExperimentalPhysicist(Pyhsicist):
    def __init__(self, main_study, name, iq=120, looks='handsome', subject='physics'):
        self.study = main_study
        super().__init__(name, iq, looks, subject)

    def experiment(self):
        print("{0} is in Physics Lab".format(self.name))


class TheoreticalPhysicist(Pyhsicist):
    def __init__(self, theory, name, iq=120, looks='handsome', subject='physics'):
        self.theory = theory
        super().__init__(name, iq, looks, subject)

    def research(self, field, base):
        super().research(field)
        print("My theory is {0}, it is based on {1}".format(self.theory, base))


einstein = TheoreticalPhysicist('Relativity', 'Albert Einstein', iq=160, looks='Hair is awesome')
print(einstein.theory, einstein.looks)
einstein.research('AAA', 'ZZZ')
