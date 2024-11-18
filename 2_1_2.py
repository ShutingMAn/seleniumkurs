from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/get_attribute.html")

try:
    img1 = browser.find_element(By.TAG_NAME, "img")
    img1_atribute = img1.get_attribute("valuex")
    x = img1_atribute
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(y)
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    Radio = browser.find_element(By.ID, "robotsRule")
    Radio.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    print(x)
    time.sleep(10)
    browser.quit()
