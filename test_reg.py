from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///C:/Users/munag/Documents/3-1/DEVOPSL/Q11/reg.html")
print("test case 1- success - opened the browser")

driver.find_element(By.NAME, "name").send_keys("Tom")
driver.find_element(By.NAME, "email").send_keys("tom@x.com")
print("name and email checked")
driver.find_element(By.TAG_NAME, "select").click()
driver.find_element(By.XPATH, "//option[.='Conference']").click()
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(2)
alert = driver.switch_to.alert
print(alert.text) 
alert.accept()

driver.quit()