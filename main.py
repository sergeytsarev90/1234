class Calculator:

    def adding(self, a, b):
        return a + b

    def division(self, a, b):
        try:
            print('hello world')
            return a / b
        except ZeroDivisionError:
            return 'На ноль делить нельзя '
        except ValueError:
            print('Не')
        except TypeError as e:
            return e
