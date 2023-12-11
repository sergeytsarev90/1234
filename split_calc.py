from main import Calculator


class SplitForCalc(Calculator):

    def __init__(self, s):
        self.s = s


    __const = 'HI'

    def make_calc(self):
        s = self.s.split()
        if s[1] == '+':
            print(self.__const)
            return self.adding(int(s[0]), int(s[2]))
        elif s[1] == '-':
            return self.division(int(s[0]), int(s[2]))
        else:
            return 'Это не выражение с точки зрения арифмеитики'


# c = Calculator(int(s[0]), int(s[2]))
c = SplitForCalc('-2 + 2').make_calc()
print(c)
print(SplitForCalc.__const)
