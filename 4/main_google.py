from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

def main():
    driver = webdriver.Edge(service=Service(ChromeDriverManager().install())) 

    try:
        driver.get("https://www.google.com")
        driver.add_cookie({
            "name":"cookies谷歌测试",
            "value":"1234",
        })
        driver.refresh()
        cookies = driver.get_cookies()
        print("获取到的Cookies:")
        for cookie in cookies:
            print(f"{cookie['name']}: {cookie['value']}")
        
        with open('谷歌cookies.json', 'w') as file:
            json.dump(cookies, file, indent=4)
        
        print("\ncookies保存在脚本目录.json")
        print("自动化脚本执行成功！")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
