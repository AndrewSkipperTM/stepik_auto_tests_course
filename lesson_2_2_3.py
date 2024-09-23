from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "https://suninjuly.github.io/selects1.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "num1").text
    y = browser.find_element(By.ID, "num2").text
    z = int(x) + int(y)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(z))
    button1 = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button1.click()
finally:
    time.sleep(10)
    browser.quit()
