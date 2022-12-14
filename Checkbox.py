
import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select


service_obj=Service("C:/Users/NAYEEM/Downloads/SEL/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

#Checkboxes
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        print(checkbox.is_selected())
        assert checkbox.is_selected()
        break


#RadioButtons
radiobuttons = driver.find_elements(By.XPATH,"//input[@type='radio']")
print(len(radiobuttons))
radiobuttons[2].click()
assert radiobuttons[2].is_selected()


#hide_show textbox
assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()


#alertbox
name="amigo"
driver.find_element(By.XPATH,"//input[@id='name']").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert=driver.switch_to.alert
alertText = alert.text
assert name in alertText
print(alertText)
alert.accept()
#alert.dismiss()


