from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link =  "https://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    box1 = browser.find_element(By.ID, "treasure")
    x = box1.get_attribute("valuex")
    y = calc(x)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    check1 = browser.find_element(By.ID, "robotCheckbox")
    check1.click()
    radio1 = browser.find_element(By.ID, "robotsRule")
    radio1.click()
    button1 = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button1.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

