# 演示测试用例报告HTML
import unittest
import xmlrunner
from XTestRunner import HTMLTestRunner
import xmlrunner


class testDemo(unittest.TestCase):
    def test_success(self):
        self.assertEqual(2 + 3, 5)

    @unittest.skip("此用例跳过执行")
    def test_skip(self):
        pass

    def test_fail(self):
        self.assertEqual(5, 6)

    def test_error(self):
        self.assertEqual(a, 6)  # type:ignore


if __name__ == "__main__":

    test_suit = unittest.TestSuite()
    test_suit.addTest(
        unittest.defaultTestLoader.loadTestsFromTestCase(testDemo)
    )

    with open("main.html", "wb", encoding="utf-8") as f:
        runner = HTMLTestRunner(
            stream=f, title="测试报告", description="测试用例执行情况", tester="李昊旻"
        )
        runner.run(test_suit)

    # runner = xmlrunner.XMLTestRunner(
    #     output='main-report'
    # )
    # runner.run(test_suit)
