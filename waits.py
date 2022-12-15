import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select

service_obj=Service("C:/Users/NAYEEM/Downloads/SEL/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

#searching_items
driver.find_element(By.CLASS_NAME,"search-keyword").send_keys("ber")
assert driver.find_element(By.CLASS_NAME,"search-keyword").get_attribute("value") == "ber"
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
print(count)
assert count > 0
time.sleep(2)
for result in results:
    result.find_element(By.XPATH,"div/button").click()
time.sleep(2)

driver.find_element(By.XPATH,"//header/div[1]/div[3]/a[4]/img[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy") #classname = .promoCode
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()  #classname = promoBtn
time.sleep(5)
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
time.sleep(2)
driver.close()
