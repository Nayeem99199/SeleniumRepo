import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support.select import Select
browserSortedVeggies =[]

service_obj=Service("C:/Users/NAYEEM/Downloads/SEL/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
#click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
# collect all veggie names -> BrowserSortedveggieList ( A,B, C)
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy()

# Sort this BrowserSortedveggieList => newSortedList -> (A,B,C)
browserSortedVeggies.sort()

print("The Actual Veggies List:")
print(originalBrowserSortedList)
print("---------------------------------------------")
print("The Sorted Veggies List:")
print(browserSortedVeggies)


