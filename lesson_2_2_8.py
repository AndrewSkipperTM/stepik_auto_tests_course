import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import os


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("111@andrey.test")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    file1 = browser.find_element(By.ID, "file")
    file1.send_keys(file_path)

    button1 = browser.find_element(By.TAG_NAME, "button")
    button1.click()


finally:
    time.sleep(10)
    browser.quit()
