from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os

HTML_FILENAME = "mainwithframe.html" 
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
    driver.switch_to.frame("login-frame")
    print("页面加载完成")
except Exception as load_error:
    print(f"加载页面出错: {load_error}")
    driver.quit() 
    exit()

try:
    name =driver.find_element(By.ID,'username')
    name.send_keys('admin')
    pwd =driver.find_element(By.ID,'password')
    pwd.send_keys('123456')
    button =driver.find_element(By.ID,'login-btn')
    button.click()
except Exception as e:
    print(e)
finally:
    time.sleep(15)
    driver.quit()    
        
    