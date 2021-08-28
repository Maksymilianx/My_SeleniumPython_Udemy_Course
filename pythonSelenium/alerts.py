from selenium import webdriver

validateText = "Option3"
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys(validateText)
driver.find_element_by_id("alertbtn").click()
# if we want to select alerts that are made by JavaScript we have to switch driver to alert
alert = driver.switch_to.alert
alertText = alert.text
assert validateText in alertText
# if we want to click "yes" button on popup alert we use:
# alert.accept()
# if we want to click "no" button we use command:
alert.dismiss()