from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager

import os, requests
# 初始化浏览器
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver = webdriver.Edge()
try:
    # 打开登录页
    driver.get("https://vueschool.io/login")
    wait = WebDriverWait(driver, 10)

    # 填写登录表单
    email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']")))
    email_input.send_keys("wulakaka@live.com")

    password_input = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    password_input.send_keys("zhang1323")

    # 提交表单
    login_button = driver.find_element(By.TAG_NAME, "button")
    login_button.click()

    # 等待登录成功
    print(EC.url_contains("courses"))
    wait.until(EC.url_contains("courses"))  # 假设跳转到仪表盘页

    # 导航到目标页面（例如课程页）
    driver.get("https://vueschool.io/lessons/create-supabase-database-migration-files-in-vue-js")

    os.makedirs('VueSchool', exist_ok=True)  # store videos in ./VueSchool

    # 获取下载链接
    # download_links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".download-link")))
    # for link in download_links:
    #     print(link.get_attribute("href"))
    containerElem = driver.find_element(by=By.CSS_SELECTOR, value='a[href^="Download the video"]')

    if not containerElem:
        print('Could not find image container.')
    else:
        videoUrl = containerElem.get_dom_attribute('href')
        # Download the image.
        print('Downloading image %s...' % videoUrl)
        res = requests.get(videoUrl)
        res.raise_for_status()

        # Save the image to ./xkcd.
        imageFile = open(os.path.join('VueSchool', os.path.basename(videoUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

finally:
    driver.quit()