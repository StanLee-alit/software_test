import unittest
class mainTest(unittest.TestCase):
    @unittest.skip("直接跳过测试")
    def test_skip(self):
        print("SKIP")
    @unittest.skipIf(3>2,"条件为真跳过")
    def test_skipIf(self):
        print("SKIP IF")
    @unittest.skipUnless(3>2,"条件为真执行")
    def test_skipUnless(self):
        print("SKIP UNLESS")
    @unittest.expectedFailure
    def test_expectedFail(self):
        self.assertEqual(3,3)
        print("EXPECTED FAIL")

if __name__ =="__main__":
    unittest.main()