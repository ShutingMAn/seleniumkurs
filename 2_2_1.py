import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    x_element = browser.find_element(By.ID, "num1")
    y_element = browser.find_element(By.ID, "num2")
    x = x_element.text
    y = y_element.text
    z = int(x) + int(y)

    select1 = Select(browser.find_element(By.TAG_NAME, "select"))
    select1.select_by_visible_text(str(z))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    print(z)
    time.sleep(10)
    browser.quit()
