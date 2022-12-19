import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
actualstatus = "Success! Thank you! Your order will be delivered in next few weeks :-)."
#from selenium.webdriver.support.select import Select
service_obj=Service("C:/Users/NAYEEM/Downloads/SEL/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Shop").click()
time.sleep(1)
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for product in products :
    productName = product.find_element(By.XPATH,"div/h4/a").text
    if productName == "Nokia Edge":
        product.find_element(By.XPATH,"div/button").click()

driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.CSS_SELECTOR,"button[class*='btn-success']").click()
driver.find_element(By.XPATH,"//input[@id='country']").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()
driver.find_element(By.XPATH,"//a[text()='term & Conditions']").click()
driver.find_element(By.CSS_SELECTOR,"button[class*='btn btn-info']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"input[class*='btn-lg']").click()
finalstatus = driver.find_element(By.CSS_SELECTOR,"div[class*='alert alert-success alert-dismissible']").text

assert actualstatus in  finalstatus
print(finalstatus)

