import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import os
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary")
    button1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    button2.click()
finally:
    time.sleep(10)
    browser.quit()
