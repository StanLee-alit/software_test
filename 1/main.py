from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os

# --- 配置 ---
HTML_FILENAME = "delay.html" # 确保这个文件和脚本在同一个目录下

# --- 驱动设置 ---
print("正在设置 Chrome 驱动...")
try:
    # 使用 webdriver-manager 自动安装和管理 ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    print("驱动设置完成。")
except Exception as setup_error:
    print(f"驱动设置出错: {setup_error}")
    exit() # 如果驱动设置失败则退出

# 配置隐式等待 (应用于所有 find_element 调用)
# 等待最多 10 秒，让元素出现在 DOM 中。
driver.implicitly_wait(10)
try:
    filepath_abs = os.path.abspath(HTML_FILENAME)
    # 检查文件是否存在
    if not os.path.exists(filepath_abs):
        print(f"错误：在路径 {filepath_abs} 未找到 HTML 文件")
        driver.quit() # 文件不存在，退出驱动
        exit()
    # 转换为 file:/// 协议的 URL
    filepath_url = "file:///" + filepath_abs
    print(f"正在加载页面: {filepath_url}")
    driver.get(filepath_url)
    print("页面加载完成。")
except Exception as load_error:
    print(f"加载页面出错: {load_error}")
    driver.quit() # 加载出错，退出驱动
    exit()

# --- 与延迟出现的元素交互 ---
try:
    print(f"[{time.ctime()}] 尝试查找并点击 ID 为 'hidden-btn' 的按钮...")
    # 隐式等待在这里生效。Selenium 会等待最多 10 秒。
    button = driver.find_element(By.ID, "hidden-btn")
    print(f"[{time.ctime()}] 按钮已找到!")
    button.click()
    print(f"[{time.ctime()}] 按钮点击成功。")

except NoSuchElementException:
    # 如果在 10 秒隐式等待后仍未找到按钮，则执行此块
    print(f"[{time.ctime()}] 错误: 等待后未找到 ID 为 'hidden-btn' 的按钮。")
    # 如果需要，可以打印异常 'e' 的详细信息: print(f"异常详情: {e}")

except Exception as interaction_error:
    # 捕获查找或点击过程中可能出现的其他错误
    print(f"[{time.ctime()}] 交互过程中发生意外错误: {interaction_error}")

finally:
    # 这个块总是会执行，确保进行清理
    print(f"[{time.ctime()}] 交互尝试结束。")
    # 可选：让浏览器保持打开几秒钟，以便观察结果
    print("等待 5 秒后关闭浏览器...")
    time.sleep(5) # 暂停 5 秒
    # --- 清理 ---
    print("正在退出驱动...")
    driver.quit() # 关闭所有浏览器窗口并结束驱动进程
    print("驱动已退出。")

print("脚本执行完毕。")