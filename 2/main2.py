
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MAIN_HTML_FILENAME = "mainwindow.html"
CHILD_WINDOW_TITLE = "注册页面（子窗口）"
VALID_USERNAME = "admin"
VALID_PHONE = "13800000000"
VALID_PASSWORD = "abc123456"
EXPLICIT_WAIT_TIME = 10
FINAL_WAIT_TIME = 5


class RegistrationPage:
    USERNAME_INPUT = (By.ID, "username")
    PHONE_INPUT = (By.ID, "phone")
    PASSWORD_INPUT = (By.ID, "password")
    REGISTER_BUTTON = (By.ID, "register")
    RESULT_MESSAGE = (By.ID, "result")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, EXPLICIT_WAIT_TIME)
        print("注册页面对象已创建。")
        self._verify_page()

    def _verify_page(self):
        try:
            self.wait.until(EC.title_contains(CHILD_WINDOW_TITLE))
            print(f"已确认当前在页面: {self.driver.title}")
        except TimeoutException:
            print(f"错误：等待超时，未能确认导航到页面 '{CHILD_WINDOW_TITLE}'")

    def fill_username(self, username):
        """填写用户名"""
        try:
            print(f"正在填写用户名: {username}")
            element = self.wait.until(
                EC.visibility_of_element_located(self.USERNAME_INPUT))
            element.clear()
            element.send_keys(username)
        except TimeoutException:
            print(f"错误：查找或填写用户名 '{self.USERNAME_INPUT}' 超时")
        except Exception as e:
            print(f"填写用户名时发生错误: {e}")

    def fill_phone(self, phone):
        """填写手机号"""
        try:
            print(f"正在填写手机号: {phone}")
            element = self.wait.until(
                EC.visibility_of_element_located(self.PHONE_INPUT))
            element.clear()
            element.send_keys(phone)
        except TimeoutException:
            print(f"错误：查找或填写手机号 '{self.PHONE_INPUT}' 超时")
        except Exception as e:
            print(f"填写手机号时发生错误: {e}")

    def fill_password(self, password):
        """填写密码"""
        try:
            print("正在填写密码: ******")
            element = self.wait.until(
                EC.visibility_of_element_located(self.PASSWORD_INPUT))
            element.clear()
            element.send_keys(password)
        except TimeoutException:
            print(f"错误：查找或填写密码 '{self.PASSWORD_INPUT}' 超时")
        except Exception as e:
            print(f"填写密码时发生错误: {e}")

    def fill_registration_form(self, username, phone, password):
        """一次性填写整个注册表单"""
        self.fill_username(username)
        self.fill_phone(phone)
        self.fill_password(password)
        print("注册表单填写完成。")

    def click_register_button(self):
        """点击注册按钮"""
        try:
            print("正在点击注册按钮...")
            button = self.wait.until(
                EC.element_to_be_clickable(self.REGISTER_BUTTON))
            button.click()
            print("注册按钮已点击。")
            self.wait.until(lambda d: d.find_element(
                *self.RESULT_MESSAGE).text.strip() != "")
            print("结果消息已更新。")
        except TimeoutException:
            print(f"错误：查找或点击注册按钮 '{self.REGISTER_BUTTON}' 或等待结果更新超时")
        except Exception as e:
            print(f"点击注册按钮时发生错误: {e}")

    def get_result_text(self):
        """获取注册结果的文本信息"""
        try:
            result_element = self.wait.until(
                EC.visibility_of_element_located(self.RESULT_MESSAGE))
            message = result_element.text
            print(f"获取到的注册结果消息: '{message}'")
            return message
        except TimeoutException:
            print(f"错误：查找注册结果元素 '{self.RESULT_MESSAGE}' 超时")
            return "错误：未能找到结果元素"
        except Exception as e:
            print(f"获取注册结果时发生错误: {e}")
            return f"错误：{e}"


def initialize_driver():
    """初始化并返回 ChromeDriver 实例"""
    print("正在设置 Chrome 驱动...")
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        print("驱动设置完成。")
        return driver
    except Exception as setup_error:
        print(f"驱动设置出错: {setup_error}")
        return None


def close_driver(driver):
    """安全地关闭 WebDriver"""
    if driver:
        print(f"等待 {FINAL_WAIT_TIME} 秒后关闭浏览器...")
        time.sleep(FINAL_WAIT_TIME)
        driver.quit()
        print("浏览器已关闭。")


def load_page(driver, filename):
    """加载本地 HTML 文件"""
    try:
        filepath_abs = os.path.abspath(filename)
        if not os.path.exists(filepath_abs):
            print(f"错误:HTML文件未找到路径 {filepath_abs}")
            return False
        filepath_url = "file:///" + filepath_abs.replace("\\", "/")
        print(f"正在加载页面: {filepath_url}")
        driver.get(filepath_url)
        print(f"页面 '{driver.title}' 加载完成。")
        return True
    except Exception as load_error:
        print(f"加载页面 '{filename}' 出错: {load_error}")
        return False


def click_open_window_button(driver):
    """在主页面点击“打开新窗口”按钮"""
    try:
        button_locator = (By.XPATH, '//button[contains(text(), "打开新窗口")]')
        print("正在查找并点击 '打开新窗口' 按钮...")
        button = WebDriverWait(driver, EXPLICIT_WAIT_TIME).until(
            EC.element_to_be_clickable(button_locator)
        )
        button.click()
        print("'打开新窗口' 按钮已点击。")
        return True
    except TimeoutException:
        print("错误：查找或点击 '打开新窗口' 按钮超时。")
        return False
    except Exception as e:
        print(f"点击 '打开新窗口' 按钮时发生错误: {e}")
        return False


def switch_to_child_window(driver, main_window_handle):
    """等待并切换到新打开的子窗口"""
    print("正在等待并切换到子窗口...")
    try:
        WebDriverWait(driver, EXPLICIT_WAIT_TIME).until(
            EC.number_of_windows_to_be(2))

        all_handles = driver.window_handles
        child_handle = None
        for handle in all_handles:
            if handle != main_window_handle:
                child_handle = handle
                break

        if child_handle:
            driver.switch_to.window(child_handle)
            print(f"已成功切换到子窗口，句柄: {child_handle}, 标题: '{driver.title}'")
            return True
        else:
            print("错误：未能找到子窗口句柄。")
            return False
    except TimeoutException:
        print("错误：等待子窗口打开超时。")
        return False
    except Exception as e:
        print(f"切换到子窗口时发生错误: {e}")
        return False


def main():
    """执行主要的自动化流程"""
    driver = initialize_driver()
    if not driver:
        return

    main_window_handle = None

    try:
        if not load_page(driver, MAIN_HTML_FILENAME):
            return
        main_window_handle = driver.current_window_handle
        print(f"主窗口句柄已记录: {main_window_handle}")

        if not click_open_window_button(driver):
            return

        if not switch_to_child_window(driver, main_window_handle):
            return

        registration_page = RegistrationPage(driver)

        registration_page.fill_registration_form(
            VALID_USERNAME, VALID_PHONE, VALID_PASSWORD)
        registration_page.click_register_button()

        result = registration_page.get_result_text()

        if result == "注册成功！":
            print("-------------------")
            print("测试结果：注册成功！")
            print("-------------------")
        elif result:
            print("-------------------")
            print(f"测试结果：注册失败，信息：{result}")
            print("-------------------")
        else:
            print("-------------------")
            print("测试结果：未能获取有效的注册结果信息。")
            print("-------------------")

    except Exception as e:
        print(f"\n!!! 自动化流程执行过程中发生严重错误 !!!")
        print(f"错误类型: {type(e).__name__}")
        print(f"错误信息: {e}")

    finally:
        close_driver(driver)


if __name__ == "__main__":
    main()
