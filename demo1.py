from selenium import webdriver
#chrome driver
from selenium.webdriver.chrome.service import Service


service_obj=Service("C:/Users/NAYEEM/Downloads/SEL/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.facebook.com")
print(driver.title)
print(driver.current_url)
driver.get("https://www.twitter.com")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()
