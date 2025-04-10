
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest
import os

HTML_FILENAME = "alert.html"

@pytest.fixture(scope="class")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver  # 返回 driver 对象供测试类使用
    # 测试结束后关闭浏览器
    driver.quit()

@pytest.fixture(scope="class")
def load_test_page(driver):
    # 加载本地网页
    filepath_abs = os.path.abspath(HTML_FILENAME)
    if not os.path.exists(filepath_abs):
        pytest.fail(f"HTML文件未找到: {filepath_abs}")
    driver.get(f"file:///{filepath_abs}")

class TestAlertHandling:
    def test_alert_interaction(self, driver, load_test_page):
        """测试弹窗交互流程"""
        try:
            # 点击按钮触发弹窗
            button = driver.find_element(By.ID, "btn")
            button.click()
            
            # 处理弹窗
            alert = driver.switch_to.alert
            alert_text = alert.text
            print(f"弹出警告框: {alert_text}")
            alert.accept()
            
            # 断言弹窗内容
            assert "预期文本" in alert_text, "弹窗内容不符合预期"
            print("警告框已确认")
            
        except NoSuchElementException as e:
            pytest.fail(f"元素未找到: {e}")
        except Exception as e:
            pytest.fail(f"测试失败: {e}")