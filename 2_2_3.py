from selenium import webdriver
from selenium.webdriver.common.by import By
import os

import time

    link = "https://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    input1 = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")
    for i in input1:
        i.send_keys("pavel")


    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    button1 = browser.find_element(By.ID, "file")
    button1.send_keys(file_path)

    button2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button2.click()

finally:
    time.sleep(20)
    browser.quit()




