# Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Misc imports
from time import sleep

def main():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://web.whatsapp.com/")
    sleep(5)
    driver.close()
if __name__ == "__main__":
    main()