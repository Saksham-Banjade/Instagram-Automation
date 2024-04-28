import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Check if Chromium is installed
def is_chromium_installed():
    try:
        chrome_options = Options()
        chrome_options.binary_location = '/usr/bin/chromium'
        driver = webdriver.Chrome(service=Service('/path/to/chromedriver'), options=chrome_options)
        return True
    except Exception:
        return False

# Read credentials from a file
def read_credentials():
    with open('credentials.txt', 'r') as file:
        return file.readline().strip(), file.readline().strip()

# Main function
def main():
    username, password = read_credentials()
    use_chromium = is_chromium_installed()
    chrome_options = Options()
    if use_chromium:
        chrome_options.binary_location = '/usr/bin/chromium'
    driver = webdriver.Chrome(service=Service('/path/to/chromedriver'), options=chrome_options)

    driver.get('https://instagram.com/login')
    time.sleep(2)
    driver.find_element(By.ID, 'username').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password, Keys.RETURN)
    time.sleep(2)

    comments = driver.find_elements(By.CLASS_NAME, 'comment')
    for comment in comments:
        if 'specific keyword' in comment.text:
            comment.find_element(By.CLASS_NAME, 'reply-button').click()
            time.sleep(1)
            driver.find_element(By.ID, 'reply-textbox').send_keys('Your reply here', Keys.RETURN)
            time.sleep(1)

    driver.quit()

if __name__ == "__main__":
    main()

