import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ddt import ddt, data, unpack


@ddt
class TestBaiduImproved(unittest.TestCase):

    driver = None
    base_url = "https://www.baidu.com"

    @classmethod
    def setUpClass(cls):
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()

    def baidu_search(self, search_key):
        self.driver.get(self.base_url)
        try:
            search_box = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "kw"))
            )
            search_box.clear()
            search_box.send_keys(search_key)

            search_button = self.driver.find_element(By.ID, "su")
            search_button.click()

            WebDriverWait(self.driver, 10).until(
                EC.title_contains(search_key)
            )

            time.sleep(10)

        except Exception as e:
            print(f"执行搜索'{search_key}'时出错:{e}")
            self.fail(f"搜索'{search_key}'失败")

    @data(
        ("selenium",),
        ("seleniumhq",),
        ("python",),
        ("unittest",)
    )
    @unpack
    def test_search_key(self, search_key):
        self.baidu_search(search_key)
        self.assertIn(search_key, self.driver.title, f"页面标题应包含 '{search_key}'")


@ddt
class TestGoogle(unittest.TestCase):
    driver = None
    base_url = "https://www.google.com"

    @classmethod
    def setUpClass(cls):
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()

    def google_search(self, search_key):
        self.driver.get(self.base_url)
        try:
            search_box = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "q"))
            )
            search_box.clear()
            search_box.send_keys(search_key)
            search_box.submit()

        except Exception as e:
            print(f"执行搜索'{search_key}'时出错:{e}")
            self.fail(f"搜索'{search_key}'失败")

    @data(
        ("selenium",),
        ("seleniumhq",),
        ("python",),
        ("unittest",)
    )
    @unpack
    def test_search_key(self, search_key):
        self.google_search(search_key)
        self.assertIn(search_key, self.driver.title, f"页面标题应包含 '{search_key}'")


if __name__ == "__main__":
    unittest.main(verbosity=2)
