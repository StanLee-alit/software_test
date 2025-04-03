import time
import os 

from selenium import webdriver
from browsermobproxy import Server

# --- 修改这里的路径 ---
bmp_path = r"D:\临时文件夹Temp\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat"

# (可选) 检查路径是否存在，增加健壮性
if not os.path.exists(bmp_path):
    raise FileNotFoundError(f"BrowserMob Proxy 路径未找到: {bmp_path}")

# 启动 browsermob-proxy 服务器
print(f"正在使用路径启动 BrowserMob Proxy: {bmp_path}")
server = Server(bmp_path)
try:
    server.start()
    print("BrowserMob Proxy 服务器已启动")
    proxy = server.create_proxy()
    print(f"已创建代理: {proxy.proxy}")

    # 配置 Selenium WebDriver 使用代理
    proxy_address = "--proxy-server={0}".format(proxy.proxy)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(proxy_address)
    chrome_options.add_argument('--ignore-certificate-errors') # 拦截 HTTPS 时通常需要

    # --- 确保你的 ChromeDriver 路径正确或使用 WebDriverManager ---
    # 例如使用 WebDriverManager (需要 pip install webdriver-manager)
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    print("正在启动 Chrome 浏览器...")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    # 或者如果你手动指定 ChromeDriver 路径:
    # driver = webdriver.Chrome(executable_path='path/to/chromedriver', options=chrome_options)

    print("Chrome 浏览器已启动")

    # 开始记录网络请求
    proxy.new_har("baidu_page")
    print("已开始记录 HAR...")

    # 打开网页
    print("正在打开 baidu.com...")
    driver.get("https://baidu.com")
    print("页面加载中...")
    time.sleep(5) # 等待页面加载和一些可能的异步请求

    # 获取捕获的网络请求
    print("正在获取 HAR 数据...")
    har_data = proxy.har # 注意这里是 har 属性

    # 打印请求 URL (可以根据需要打印更详细的信息)
    print("\n--- 捕获到的请求 ---")
    if 'log' in har_data and 'entries' in har_data['log']:
        for entry in har_data['log']['entries']:
            print(f"请求 URL: {entry['request']['url']}")
            # 如果你想看响应状态码:
            # print(f"  响应状态: {entry['response']['status']}")
            # 谨慎打印响应内容，可能非常大
            # if 'content' in entry['response'] and 'text' in entry['response']['content']:
            #     print(f"  响应内容预览: {entry['response']['content']['text'][:100]}...") # 只预览前100个字符
    else:
        print("未能获取到有效的 HAR 日志条目。")

    print("\n等待 3 秒...")
    time.sleep(3)

except Exception as e:
    print(f"\n发生错误: {e}")

finally:
    # 关闭浏览器和 proxy 服务器
    if 'driver' in locals() and driver:
        print("正在关闭浏览器...")
        driver.quit()
    if 'server' in locals() and server:
        print("正在停止 BrowserMob Proxy 服务器...")
        server.stop()
    print("脚本执行完毕。")