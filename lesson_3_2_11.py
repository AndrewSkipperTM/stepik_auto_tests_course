import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestForm(unittest.TestCase):
    def test_form1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        FirstName = browser.find_element(By.CSS_SELECTOR, 'input.first:required')
        FirstName.send_keys("Andruxa")

        SecondName = browser.find_element(By.CSS_SELECTOR, 'input.second:required')
        SecondName.send_keys("Solo")

        Email = browser.find_element(By.CSS_SELECTOR, 'input.third:required')
        Email.send_keys("111@andrey.test")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Something gone wrong")

    def test_form2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        FirstName = browser.find_element(By.CSS_SELECTOR, 'input.first:required')
        FirstName.send_keys("Andruxa")

        SecondName = browser.find_element(By.CSS_SELECTOR, 'input.second:required')
        SecondName.send_keys("Solo")

        Email = browser.find_element(By.CSS_SELECTOR, 'input.third:required')
        Email.send_keys("111@andrey.test")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Something gone wrong")

if __name__ == "__main__":
    unittest.main()

