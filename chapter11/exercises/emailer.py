#! python3

import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def sendMessage(email, message):
    driver = webdriver.Edge()
    driver.get('https://mail.tslsmart.com/alimail')

    # 需要切换到 iframe
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe.login_pannel_iframe')))

    formElem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'form'))
    )
    if formElem:
        nameElem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]'))
        )
        passwordElem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]'))
        )
        if nameElem and passwordElem:
            nameElem.send_keys('zhang.weifeng@tslsmart.com')
            print('Enter the password: ')
            password = input()
            passwordElem.send_keys(password)
            passwordElem.submit()

            print('Logged in')

            addButton = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'span[aria-label="add-icon"]'))
            )
            addButton.click()
            print('button click')


# if len(sys.argv) >= 3:
#     email = sys.argv[1]
#     message = ' '.join(sys.argv[2:])
#     sendMessage(email, message)
# else:
#     print('enter email and message')


sendMessage('a', 'b')
