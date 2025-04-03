
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# service =Service(
#     ChromeDriverManager().install()
# )
# options =webdriver.ChromeOptions()
# driver =webdriver.Chrome(
#     service=service,options=options
# )
# driver.maximize_window()
# driver.get("https://www.bilibili.com/")

# bilibili_search =driver.find_element_by_class_name(
#     'nav-search-input'
# )
# time.sleep(1)
# bilibili_search.send_keys("selenium")
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.baidu.com/")

baidu_search = driver.find_element(By.CSS_SELECTOR, "#kw") 
baidu_search.send_keys('selenium')
# content =baidu_search.get_attribute("value")
# baidu_search.send_keys(content)
baidu_button = driver.find_element(By.CSS_SELECTOR, "#su") 
baidu_button.click()
time.sleep(30)
driver.quit()

    
    