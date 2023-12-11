class Calculator:

    def adding(self, a, b):
        return a + b

    def division(self, a, b):
        try:
            print('guten morgan')
            return a / b
        except ZeroDivisionError:
            return 'На ноль не делится '
        except ValueError:
            print('No')
        except TypeError as e:
            return e
