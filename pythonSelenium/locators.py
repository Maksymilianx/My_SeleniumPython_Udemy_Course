from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

# Customized CSS Syntax
# tagname[attribute='value']
driver.find_element_by_css_selector("input[name='name']").send_keys("Maksymilian")
driver.find_element_by_name("email").send_keys("Krajewski")
driver.find_element_by_id("exampleCheck1").click()
# Generating xpath based on text
# //tagname[contains(text(),'actual-text')]
# driver.find_element_by_xpath("//button[contains(text(),'Zaloguj')]").click()

# select class provide the methods to handle the options
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element_by_xpath("//input[@type='submit']").click()
message = driver.find_element_by_class_name("alert-success").text

assert "success" in message