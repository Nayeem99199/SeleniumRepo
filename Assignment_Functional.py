import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList =[]
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
    actualList.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH,"div/button").click()

assert expectedList == actualList

driver.find_element(By.XPATH,"//header/div[1]/div[3]/a[4]/img[1]").click()

driver.find_element(By.XPATH,"//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy") #classname = .promoCode
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()  #classname = promoBtn
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

totalitems = driver.find_elements(By.XPATH,"//tbody/tr/td[3]")
sumitems = 0
for items in totalitems:
   sumitems = sumitems + int(items.text)
print(f"total no.of items are: {sumitems}")


priceofitems = driver.find_elements(By.XPATH,"//tbody/tr/td[5]")  # or we can use driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum=0
for price in priceofitems:
    sum = sum + int(price.text)
print(f"total price of the {sumitems} is {sum}")

p = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert p == sum


DiscountPercentage = driver.find_element(By.CSS_SELECTOR,".discountPerc").text
print(f"Discount applied : {DiscountPercentage}")

DiscountAmount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
print(f"Discounted amount : {DiscountAmount}")
assert sum > DiscountAmount

driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
time.sleep(2)




driver.close()
