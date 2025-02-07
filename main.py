# Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Misc imports
from time import sleep
import os


def main():

    message = "This is a headless test message!"

    chrome_options = Options()
    chrome_options.add_argument("--headless=new")

    dir_path = os.getcwd()
    profile = os.path.join(dir_path, "profile", "wpp")

    chrome_options.add_argument(r"user-data-dir={}".format(profile))
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://web.whatsapp.com/")
    sleep(5)
    driver.find_element(
        By.XPATH,
        '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div/span[1]',
    ).click()
    driver.find_element(
        By.XPATH,
        '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]',
    ).send_keys(message)
    driver.find_element(
        By.XPATH,
        '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]',
    ).send_keys(Keys.RETURN)

    sleep(3)
    driver.close()


if __name__ == "__main__":
    main()
