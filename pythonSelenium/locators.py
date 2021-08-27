from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://lms.coderslab.pl/login")

# Customized CSS Syntax
# tagname[attribute='value']
driver.find_element_by_css_selector("input[name='_username']").send_keys("krajewski.maksymilian@gmail.com")
driver.find_element_by_name("_password").send_keys("jakiestamhaslo")
driver.find_element_by_id("rememberMe").click()
# Generating xpath based on text
# //tagname[contains(text(),'actual-text')]
driver.find_element_by_xpath("//button[contains(text(),'Zaloguj')]").click()

