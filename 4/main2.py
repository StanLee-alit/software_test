from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


def main():
    driver = webdriver.Edge(service=Service(
        EdgeChromiumDriverManager().install()))
    driver.maximize_window()

    try:
        driver.get("https://www.baidu.com")
        driver.execute_script(
            "document.getElementById('su').style.visibility='hidden';"
        )
        time.sleep(5)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
