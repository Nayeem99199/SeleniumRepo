from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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


driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME,"name").send_keys("Nayeem")
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("nayeem0772@gmail.com")
driver.find_element(By.XPATH,"//input[@id='exampleInputPassword1']").send_keys("Nayeem552")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.XPATH,"//body[1]/app-root[1]/form-comp[1]/div[1]/form[1]/input[1]").click()
message=driver.find_element(By.XPATH,"//body/app-root[1]/form-comp[1]/div[1]/div[2]/div[1]").text
print(message)

#assert "asjcgjgc" in message



driver.find_element(By.ID,"inlineRadio1").click()
driver.find_element(By.XPATH,"//input[@class='ng-untouched ng-pristine ng-valid']").clear()



