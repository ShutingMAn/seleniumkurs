from webbrowser import Chrome

from selenium import  webdriver
from selenium.webdriver.common.by import By
import math
import time
link = "https://suninjuly.github.io/math.html"

browser = webdriver.Chrome()

browser.get(link)

try:
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(y)

    CheckBox = browser.find_element(By.ID, "robotCheckbox")
    CheckBox.click()

    Radio = browser.find_element(By.ID, "robotsRule")
    Radio.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(20)
    browser.quit()

