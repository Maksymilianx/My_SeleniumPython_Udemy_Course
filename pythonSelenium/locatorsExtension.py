from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=eu")
driver.find_element_by_css_selector("#username").send_keys("Maksymilian")
driver.find_element_by_css_selector(".password").send_keys("Krajewski")
driver.find_element_by_css_selector(".password").clear()
# Find element by link works on anchor text like for example:
# <a href="/secur/forgotpassword.jsp?locale=eu&lqs=locale%3Deu"> Forgot Your Password? </a>
driver.find_element_by_link_text("Forgot Your Password?").click()
# //tagname[text()='xxx'] for anchor
# Xpath =//tagname[@Attribute=’value’]
driver.find_element_by_xpath("//input[@name='cancel']").click()
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(4)").text)