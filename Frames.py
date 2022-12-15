import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#from selenium.webdriver.support.select import Select

service_obj=Service("C:/Users/NAYEEM/Downloads/SEL/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Frames").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"iFrame").click()
time.sleep(2)
driver.switch_to.frame("mce_0_ifr")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"#tinymce").clear()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"#tinymce").send_keys("Hi, This is Nayeem")
time.sleep(2)
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3").text)


