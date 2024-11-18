import time
import math
from pydoc import browse

from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/find_link_text"

try:
    driver = webdriver.Chrome()
    driver.get(link)
    link = driver.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
    input1 = driver.find_element(By.TAG_NAME, "input")
    input1.send_keys("Pavel")
    input2 = driver.find_element(By.NAME, "last_name")
    input2.send_keys("Zavgorodniy")
    input3 = driver.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Moscow")
    input4 = driver.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    time.sleep(30)
    print("Done")
    driver.quit()
