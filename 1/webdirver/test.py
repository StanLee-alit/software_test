from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

# 使用 webdriver_manager 配置 Chrome Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://news.baidu.com/")

# search = driver.find_element(By.ID,'kw')
# search.send_keys('py')
# button = driver.find_element(By.ID,'su')
# button.click()

# <a href="http://news.baidu.com" target="_blank" class="mnav c-font-normal c-color-t">新闻</a>
# link =driver.find_element(By.LINK_TEXT,'新闻')
# link.click()

link_content =driver.find_element(By.PARTIAL_LINK_TEXT,"春染茶山")
time.sleep(3)
link_content.click()
time.sleep(5)
