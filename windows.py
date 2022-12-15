import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#from selenium.webdriver.support.select import Select

service_obj=Service("C:/Users/NAYEEM/Downloads/SEL/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
FirstWindowTitle =driver.title
driver.find_element(By.LINK_TEXT,"Click Here").click()

WindowsOpened = driver.window_handles
print(WindowsOpened)
driver.switch_to.window(WindowsOpened[1])

SecondWindowTitle = driver.title
assert not FirstWindowTitle == SecondWindowTitle

driver.switch_to.window(WindowsOpened[0])

ThirdWindowTitle = driver.title
assert FirstWindowTitle == ThirdWindowTitle




time.sleep(5)