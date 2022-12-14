from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("C:/Users/NAYEEM/Downloads/SEL/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)


driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
driver.find_element(By.ID,"userEmail").send_keys("nayeem0772@gmail.com")
driver.find_element(By.CSS_SELECTOR,"#userPassword").send_keys("N4yeem@552")
driver.find_element(By.CLASS_NAME,"forgot-password-link").click()

