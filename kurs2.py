

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver2 = webdriver.Chrome(service=service)
driver2.get("https://testautomationpractice.blogspot.com")

ELEMENT_ID = driver2.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
# ELEMENT_CLASS = driver.find_element(By.CLASS_NAME, "login")
# ELEMENT_TAG = driver.find_element(By.TAG_NAME, "input")
print(ELEMENT_ID)

SEARCH_BUTTON = driver2.find_element(By.CLASS_NAME, "class")
SEARCH_BUTTON.click()
