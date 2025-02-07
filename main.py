# Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Misc imports
from time import sleep
import os

def main():
    
    
    chrome_options = Options()
    # chrome_options.add_argument("--headless=new")
    cookies = []
    
    dir_path = os.getcwd()
    profile = os.path.join(dir_path, "profile", "wpp")
    
    chrome_options.add_argument(r"user-data-dir={}".format(profile))
    driver = webdriver.Chrome(options=chrome_options)
      
    driver.get("https://web.whatsapp.com/")
    sleep(5)
    driver.close()

if __name__ == "__main__":
    main()