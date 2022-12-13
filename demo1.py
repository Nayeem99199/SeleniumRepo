from selenium import webdriver

from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.edge.service import Service

# chrome driver
service_obj=Service("C:/Users/NAYEEM/Downloads/SEL/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)

#firefoxdriver
# service_obj=Service("C:/Users/NAYEEM/Downloads/SEL/geckodriver.exe")
# driver=webdriver.Firefox(service=service_obj)

#Edgedriver
# service_obj=Service("C:/Users/NAYEEM/Downloads/SEL/msedgedriver.exe")
# driver=webdriver.Edge(service=service_obj)

driver.maximize_window()
driver.get("https://www.facebook.com")
print(driver.title)
print(driver.current_url)
driver.get("https://www.twitter.com")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()
