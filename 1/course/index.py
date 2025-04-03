from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

# 使用 webdriver_manager 配置 Chrome Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.baidu.com/")
serviceList =["超星学习通","python"]
search =driver.find_element(By.ID,'kw')
button =driver.find_element(By.ID,"su")
for list in serviceList:
    search.clear()
    search.send_keys(list)
    time.sleep(2)
    button.click()
    search.clear()
time.sleep(10)    
