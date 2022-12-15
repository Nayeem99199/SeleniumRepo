import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#from selenium.webdriver.support.select import Select

service_obj=Service("C:/Users/NAYEEM/Downloads/SEL/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
FirstWindowTitle =driver.title
driver.find_element(By.CLASS_NAME,"blinkingText").click()

WindowsOpened = driver.window_handles
print(WindowsOpened)
driver.switch_to.window(WindowsOpened[1])

GrabbedText = driver.find_element(By.XPATH,"//body/div[1]/div[2]/div[1]/div[2]/p[2]").text

print(f"The Grabbed Text is:  {GrabbedText} ")

s=GrabbedText.split()
print(s)
# EmailId = s[4]
print(f"The Extracted Email Id is: {s[4]}")
driver.switch_to.window(WindowsOpened[0])
driver.find_element(By.CSS_SELECTOR,"#username").send_keys(s[4])
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Nayeem123")
driver.find_element(By.XPATH,"//label[2]//span[2]").click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"#okayBtn").click()

dropdown = Select(driver.find_element(By.XPATH,"//select[@class='form-control']"))
time.sleep(2)
dropdown.select_by_index(2)

driver.find_element(By.ID,"terms").click()
time.sleep(2)
driver.find_element(By.ID,"signInBtn").click()
time.sleep(2)