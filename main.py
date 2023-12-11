class Calculator:

    def adding(self, a, b):
        return a + b

    def division(self, a, b):
        try:
            print('Привет мир')
            return a / b
        except ZeroDivisionError:
            return 'На ноль делить нельзя совсем'
        except ValueError:
            print('Не')
        except TypeError as e:
            return e
