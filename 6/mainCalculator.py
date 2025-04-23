import unittest
import calculator


class TestMainCalculator(unittest.TestCase):
    def test_add(self):
        res = calculator.add(2, 3)
        self.assertEqual(res, 5)

    def test_subtract(self):
        res = calculator.subtract(5, 2)
        self.assertEqual(res, 3)

    def test_multiply(self):
        res = calculator.multiply(2, 3)
        self.assertEqual(res, 6)

    def test_divide(self):
        res = calculator.divide(6, 2)
        self.assertEqual(res, 3)

        # 测试除数为零的情况
        with self.assertRaises(ValueError):
            calculator.divide(5, 0)


if __name__ == '__main__':
    unittest.main()
