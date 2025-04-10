import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os

HTML_FILENAME = "alert.html" 
print("正在设置 Chrome 驱动...")
try:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    print("驱动设置完成。")
except Exception as setup_error:
    print(f"驱动设置出错: {setup_error}")
    exit()
     
driver.implicitly_wait(10)

try:
    filepath_abs = os.path.abspath(HTML_FILENAME)
    if not os.path.exists(filepath_abs):
        print(f"错误：在路径 {filepath_abs} 未找到 HTML 文件")
        driver.quit()
        exit()
    filepath_url = "file:///" + filepath_abs
    print(f"正在加载页面: {filepath_url}")
    driver.get(filepath_url)
    print("页面加载完成")
except Exception as load_error:
    print(f"加载页面出错: {load_error}")
    driver.quit() 
    exit()

try:
    button =driver.find_element(By.ID,"btn")
    button.click()
    alert =driver.switch_to.alert
    print(f"弹出警告框: {alert.text}")
    alert.accept()
    print("警告框已确认")
except NoSuchElementException as e:
    print(f"元素未找到: {e}")
except Exception as e:
    print(e)
finally:
    time.sleep(5)
    driver.quit()