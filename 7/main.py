import unittest


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b


class TestMathFunctions(unittest.TestCase):
    def setUp(self):
        print("开始测试")

    def tearDown(self):
        print("清理测试环境")

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 0), -1)
        self.assertEqual(add(0, 0), 0)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestMathFunctions('test_add'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
