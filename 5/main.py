
import os
import time
import csv
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MAIN_HTML_FILENAME = "mainwindow.html"
CHILD_WINDOW_TITLE = "注册页面(子窗口)"

VALID_USERNAME_REF = "admin"
VALID_PHONE = "13800000000"
VALID_PASSWORD_REF = "abc123456"

CSV_DATA_FILENAME = "user.csv"
TXT_DATA_FILENAME = "user.txt"
DATA_SOURCE_TYPE = "csv"

EXPLICIT_WAIT_TIME = 10
WAIT_BETWEEN_ATTEMPTS = 1
FINAL_WAIT_TIME = 3


class RegistrationPage:
    USERNAME_INPUT = (By.ID, "username")
    PHONE_INPUT = (By.ID, "phone")
    PASSWORD_INPUT = (By.ID, "password")
    REGISTER_BUTTON = (By.ID, "register")
    RESULT_MESSAGE = (By.ID, "result")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, EXPLICIT_WAIT_TIME)
        self._verify_page()

    def _verify_page(self):
        try:
            self.wait.until(EC.title_is(CHILD_WINDOW_TITLE))
        except TimeoutException:
            print(f"错误：等待超时！未能确认导航到标题为 '{CHILD_WINDOW_TITLE}' 的页面。")
            print(f"实际页面标题是: '{self.driver.title}'")
            raise TimeoutException(f"未能切换并验证子窗口 '{CHILD_WINDOW_TITLE}'")

    def fill_username(self, username):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(self.USERNAME_INPUT))
            element.clear()
            element.send_keys(username)
        except TimeoutException:
            print(f"  错误：查找或填写用户名 '{self.USERNAME_INPUT}' 超时")
        except Exception as e:
            print(f"  填写用户名时发生错误: {e}")

    def fill_phone(self, phone):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(self.PHONE_INPUT))
            element.clear()
            element.send_keys(phone)
        except TimeoutException:
            print(f"  错误：查找或填写手机号 '{self.PHONE_INPUT}' 超时")
        except Exception as e:
            print(f"  填写手机号时发生错误: {e}")

    def fill_password(self, password):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(self.PASSWORD_INPUT))
            element.clear()
            element.send_keys(password)
        except TimeoutException:
            print(f"  错误：查找或填写密码 '{self.PASSWORD_INPUT}' 超时")
        except Exception as e:
            print(f"  填写密码时发生错误: {e}")

    def fill_registration_form(self, username, phone, password):
        self.fill_username(username)
        self.fill_phone(phone)
        self.fill_password(password)

    def click_register_button(self):
        try:
            button = self.wait.until(
                EC.element_to_be_clickable(self.REGISTER_BUTTON))
            button.click()
            self.wait.until(lambda d: d.find_element(
                *self.RESULT_MESSAGE).text.strip() != "")
            return True
        except TimeoutException:
            print(f"  错误：查找/点击注册按钮 '{self.REGISTER_BUTTON}' 或等待结果更新超时")
            return False
        except Exception as e:
            print(f"  点击注册按钮或等待结果时发生错误: {e}")
            return False

    def get_result_text(self):
        try:
            result_element = self.driver.find_element(*self.RESULT_MESSAGE)
            message = result_element.text.strip()
            return message
        except NoSuchElementException:
            print(f"  错误：注册结果元素 '{self.RESULT_MESSAGE}' 未找到")
            return "错误：未能找到结果元素"
        except Exception as e:
            print(f"  获取注册结果时发生错误: {e}")
            return f"错误：{e}"


def initialize_driver():
    print("正在设置 Chrome 驱动...")
    try:
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        print("驱动设置完成，浏览器窗口已最大化。")
        return driver
    except Exception as setup_error:
        print(f"驱动设置出错: {setup_error}")
        return None


def close_driver(driver):
    if driver:
        print(f"测试流程结束，等待 {FINAL_WAIT_TIME} 秒后关闭浏览器...")
        time.sleep(FINAL_WAIT_TIME)
        driver.quit()
        print("浏览器已关闭。")


def load_page(driver, filename):
    try:
        filepath_abs = os.path.abspath(filename)
        if not os.path.exists(filepath_abs):
            print(f"错误: HTML文件未找到，路径: {filepath_abs}")
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
            print(f"已成功切换到子窗口，句柄: {child_handle}")
            return True
        else:
            print("错误：未能找到子窗口句柄（虽然检测到窗口数量为2）。")
            return False
    except TimeoutException:
        print("错误：等待子窗口打开超时（窗口数量未在预期时间内变为2）。")
        return False
    except Exception as e:
        print(f"切换到子窗口时发生错误: {e}")
        return False


def read_user_data_from_csv(filename):
    users = []
    filepath_abs = os.path.abspath(filename)
    if not os.path.exists(filepath_abs):
        print(f"错误: CSV 数据文件未找到: {filepath_abs}")
        return users

    try:
        with open(filepath_abs, mode='r', encoding='utf-8', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            if 'username' not in reader.fieldnames or 'password' not in reader.fieldnames:
                print(
                    f"错误: CSV 文件 '{filename}' 缺少 'username' 或 'password' 列头.")
                return []
            for i, row in enumerate(reader):
                username = row.get('username', '').strip()
                password = row.get('password', '').strip()
                if username and password:
                    users.append({'username': username, 'password': password})
                else:
                    print(f"警告: 跳过 CSV 文件第 {i+2} 行的无效数据（用户名或密码为空）: {row}")
    except FileNotFoundError:
        print(f"错误: CSV 数据文件 '{filepath_abs}' 未找到。")
    except Exception as e:
        print(f"读取 CSV 文件 '{filename}' 时发生错误: {e}")
    return users


def read_user_data_from_txt(filename):
    users = []
    filepath_abs = os.path.abspath(filename)
    if not os.path.exists(filepath_abs):
        print(f"错误: TXT 数据文件未找到: {filepath_abs}")
        return users

    try:
        with open(filepath_abs, mode='r', encoding='utf-8') as txtfile:
            for i, line in enumerate(txtfile):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if ':' not in line:
                    print(f"警告: 跳过 TXT 文件第 {i+1} 行的无效格式（缺少':'）：'{line}'")
                    continue
                parts = line.split(':', 1)
                username = parts[0].strip()
                password = parts[1].strip()
                if username and password:
                    users.append({'username': username, 'password': password})
                else:
                    print(f"警告: 跳过 TXT 文件第 {i+1} 行的无效数据（用户名或密码为空）：'{line}'")
    except FileNotFoundError:
        print(f"错误: TXT 数据文件 '{filepath_abs}' 未找到。")
    except Exception as e:
        print(f"读取 TXT 文件 '{filename}' 时发生错误: {e}")
    return users


def main():
    print("--- 自动化测试开始 ---")
    all_user_data = []
    data_file_used = ""

    print(f"配置的数据源类型: '{DATA_SOURCE_TYPE}'")
    if DATA_SOURCE_TYPE.lower() == 'csv':
        data_file_used = CSV_DATA_FILENAME
        all_user_data = read_user_data_from_csv(data_file_used)
    elif DATA_SOURCE_TYPE.lower() == 'txt':
        data_file_used = TXT_DATA_FILENAME
        all_user_data = read_user_data_from_txt(data_file_used)
    else:
        print(
            f"错误: 无效的 DATA_SOURCE_TYPE 配置: '{DATA_SOURCE_TYPE}'. 请在脚本中设置为 'csv' 或 'txt'.")
        return

    if not all_user_data:
        print(f"错误:未能从数据文件 '{data_file_used}' 加载任何有效用户数据，测试中止。")
        return

    print(f"准备使用来自 '{data_file_used}' 的 {len(all_user_data)} 条数据进行测试。")

    driver = initialize_driver()
    if not driver:
        print("错误：浏览器驱动初始化失败，测试中止。")
        return

    main_window_handle = None
    registration_page = None

    try:
        if not load_page(driver, MAIN_HTML_FILENAME):
            return

        main_window_handle = driver.current_window_handle
        print(f"主窗口句柄已记录: {main_window_handle}")

        if not click_open_window_button(driver):
            return

        if not switch_to_child_window(driver, main_window_handle):
            return

        try:
            registration_page = RegistrationPage(driver)
        except TimeoutException as page_verify_error:
            print(f"错误：无法初始化 RegistrationPage 对象，原因：{page_verify_error}")
            return

        print(f"\n--- 开始循环测试 {len(all_user_data)} 个用户 ---")
        results_summary = {'success': 0, 'failure_expected': 0,
                           'failure_unexpected': 0, 'errors': 0}

        for index, user_data in enumerate(all_user_data):
            username = user_data['username']
            password = user_data['password']
            print(
                f"\n[ ==> 测试用户 {index + 1}/{len(all_user_data)}: 用户名='{username}' <== ]")

            registration_page.fill_registration_form(
                username, VALID_PHONE, password)

            if not registration_page.click_register_button():
                print("  错误：点击注册按钮或等待结果时失败，跳过此用户。")
                results_summary['errors'] += 1
                continue

            result = registration_page.get_result_text()

            print("-" * 25)
            if result == "注册成功！":
                print(f"测试结果：用户 '{username}' 注册成功！(与预期不符)")
                results_summary['success'] += 1
            elif result == "用户名或密码错误":
                print(f"测试结果：用户 '{username}' 注册失败 - 用户名或密码错误 (符合预期)。")
                results_summary['failure_expected'] += 1
            elif "错误：" in result:
                print(f"测试结果：用户 '{username}' 操作时遇到内部错误: {result}")
                results_summary['errors'] += 1
            else:
                print(f"测试结果：用户 '{username}' 注册失败，收到意外消息：'{result}'")
                results_summary['failure_unexpected'] += 1
            print("-" * 25)

            if index < len(all_user_data) - 1:
                time.sleep(WAIT_BETWEEN_ATTEMPTS)

        print("\n--- 所有用户数据处理完毕 ---")

        print("\n--- 测试结果摘要 ---")
        print(f"总测试用户数: {len(all_user_data)}")
        print(f"  注册成功 (预期外): {results_summary['success']}")
        print(
            f"  注册失败 (预期内，信息为'用户名或密码错误'): {results_summary['failure_expected']}")
        print(f"  注册失败 (预期外消息): {results_summary['failure_unexpected']}")
        print(f"  操作/内部错误: {results_summary['errors']}")
        print("--- 摘要结束 ---")

    except Exception as e:
        print(f"\n!!!!!! 自动化流程执行过程中发生严重错误 !!!!!!")
        print(f"错误类型: {type(e).__name__}")
        print(f"错误信息: {e}")
        print("详细错误追溯:")
        traceback.print_exc()

    finally:
        close_driver(driver)
        print("--- 自动化测试结束 ---")


if __name__ == "__main__":
    main()
