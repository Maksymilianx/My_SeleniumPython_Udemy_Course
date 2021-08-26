from selenium import webdriver
# Browser exposes an executable file
# Through Selenium test we need to invoke the executable file which will then invoke actual browser
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")  # get method to hit url on browser
print(driver.title)
print(driver.current_url)

# driver.quit() all the windows will be closed
# driver.close() only current window will close

driver.get("https://courses.rahulshettyacademy.com/courses")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()