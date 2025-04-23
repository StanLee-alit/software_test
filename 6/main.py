class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        try:
            return float(self.a)+float(self.b)
        except ValueError:
            return "参数有误"

    def sub(self):
        try:
            return float(self.a)-float(self.b)
        except ValueError:
            return "参数有误"

    def mul(self):
        try:
            return float(self.a)*float(self.b)
        except ValueError:
            return "参数有误"

    def div(self):
        try:
            return float(self.a)/float(self.b)
        except ValueError:
            return "参数有误"
        except ZeroDivisionError:
            return "除数不能为0"
