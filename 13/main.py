#!/usr/bin/env -S python -v

# 使用selenium编写前端自动化测试脚本,访问网易邮箱,设置智能时间等待3秒,浏览器窗口自动化

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

try:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://mail.126.com/")
    
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)
    frame = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//iframe[contains(@id,'URS-iframe')]")
        )
    )
    driver.switch_to.frame(frame)

    email_input = wait.until(
        EC.presence_of_element_located((By.NAME, "email")))
    email_input.send_keys("zhangsan@126.com")

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("Lhm123456")

    login_button = None
    try:
        login_button = driver.find_element(By.NAME, "dologin")
    except:
        try:
            login_button = driver.find_element(By.ID, "dologin")
        except:
            try:
                login_button = driver.find_element(By.CLASS_NAME, "loginBtn")
            except:
                try:
                    login_button = driver.find_element(
                        By.XPATH, "//input[@type='submit']"
                    )
                except:
                    print("无法找到登录按钮，请检查页面结构")

    if login_button:
        login_button.click()
        time.sleep(3)

    driver.get_screenshot_as_file("main.png")
    driver.switch_to.default_content()

    time.sleep(5)
    mainhandle = driver.current_window_handle

    try:
        help_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "帮助")))
        help_link.click()

        allhandle = driver.window_handles
        helphandle = next(h for h in allhandle if h != mainhandle)
        driver.switch_to.window(helphandle)

        search_input = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "searchIconInner"))
        )
        search_input.send_keys("如何重置密码")

        time.sleep(10)
    except Exception as e:
        print(f"处理帮助页面时出错: {e}")

except Exception as e:
    print(f"脚本执行出错: {e}")
finally:
    if "driver" in locals():
        driver.quit()
