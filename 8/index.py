import unittest


def setUpModule():
    print("模块开始")


def tearDownModule():
    print("模块结束")


class indexTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("测试类开始")

    @classmethod
    def tearDownClass(cls):
        print("测试类结束")

    def setUp(self):
        print("测试用例开始")

    def tearDown(self):
        print("测试用例结束")

    def test_Case1(self):
        print("测试用例1")

    def test_Case2(self):
        print("测试用例2")
class myTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("测试类myTest开始")
    @classmethod
    def tearDownClass(cls):
        print("测试类myTest结束")
    def test_Case3(self):
        print("测试用例3")


if __name__ == '__main__':
    unittest.main()
