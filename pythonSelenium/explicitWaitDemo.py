import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

lst = []
lst2 = []
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")


driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    lst.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(lst)

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver,6)
# Explicit wait - wait for 5 seconds only for a directed object in this case class name "promoCode"
wait.until(EC.presence_of_element_located((By.CLASS_NAME,"promoCode")))

vegetables = driver.find_elements_by_css_selector("p.product-name")
for veg in vegetables:
    lst2.append(veg.text)
print(lst2)
assert lst == lst2

originalAmount = driver.find_element_by_css_selector(".discountAmt").text
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
discountAmount = driver.find_element_by_css_selector(".discountAmt").text

assert float(discountAmount) < float(originalAmount)
print(driver.find_element_by_css_selector("span.promoInfo").text)

amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
sum = 0
for amount in amounts:
    sum = sum + int(amount.text)
print(sum)

totalAmount = int(driver.find_element_by_class_name("totAmt").text)

assert sum == totalAmount










