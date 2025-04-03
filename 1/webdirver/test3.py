from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.baidu.com/")

search_box = driver.find_element(By.CSS_SELECTOR, "#kw") 
search_box.send_keys('vscode.py')


search_button = driver.find_element(By.CSS_SELECTOR, "#su") 
search_button.click()


wait = WebDriverWait(driver, 10)  
try:
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".result")))
    print("搜索结果页面加载完成!")
except TimeoutError:
    print("搜索结果页面加载超时!")

time.sleep(10)
driver.quit() 