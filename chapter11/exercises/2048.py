from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge()
driver.get('https://play2048.co/')
htmlElem = driver.find_element(by=By.CSS_SELECTOR,value='html')

keys = [
    Keys.UP,
    Keys.RIGHT,
    Keys.DOWN,
    Keys.LEFT
]

index = 0

while True:
    htmlElem.send_keys(keys[index])
    index += 1
    index = index % 4