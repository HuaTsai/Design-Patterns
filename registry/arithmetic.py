from registry import Registry

ARITHMETIC = Registry("arithmetic")

@ARITHMETIC.register
class Add:
    def __call__(self, x, y):
        return x + y

@ARITHMETIC.register
class Subtract:
    def __call__(self, x, y):
        return x - y

