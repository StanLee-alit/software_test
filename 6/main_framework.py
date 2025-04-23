import unittest
# 这是Python文档提供的实例用法


class TestUpper(unittest.TestCase):
    def test_main(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())

    def test_split(self):
        s = "Hello World"
        self.assertEqual(s.split(), ['Hello', 'World'])
        with self.assertRaises(TypeError):
            s.split(2)

    def test_jia(self):
        self.assertEqual(jia(2, 3), 5)
        self.assertEqual(jia(-3, 2), -1)

    def test_jian(self):
        self.assertEqual(jian(3, 2), 1)
        self.assertEqual(jian(2, 3), -1)

    def test_cheng(self):
        self.assertEqual(cheng(2, 3), 6)
        self.assertEqual(cheng(-2, 3), -6)

    def test_chu(self):
        # self.assertEqual(chu(2, 0), 1)
        self.assertEqual(chu(2, 2), 1)


def jia(a, b):
    return a+b


def jian(a, b):
    return a-b


def cheng(a, b):
    return a*b


def chu(a, b):
    if b == 0:
        raise ValueError("除数不能为零")
    return a/b


if __name__ == '__main__':
    unittest.main()
